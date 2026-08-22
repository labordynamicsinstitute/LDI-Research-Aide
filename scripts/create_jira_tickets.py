#!/usr/bin/env python3
"""Bulk-create Jira issues from the Training CSVs.

This replaces the manual "Import from CSV" flow in the Jira UI (whose saved
configuration lives in Training/jira-import-mapping.txt) with a scripted loop.
Each row becomes one Task, which is then transitioned from "Open" to "Assigned".

Every CSV column is resolved to a real Jira field *before* anything is created,
by comparing the header against the create-screen metadata of the target
project/issue type. Unresolvable headers abort the run unless
--allow-unmapped is given.

Credentials come from the environment (as in the aea-editor-scripts package):

    JIRA_USERNAME - Atlassian account email
    JIRA_API_KEY  - API token from https://id.atlassian.com/manage-profile/security/api-tokens

The server URL is taken from --jira-url, else $JIRA_URL, else the constant
exported by aea_editor_scripts.jira_purge_query (if that package is installed).

Examples:
    # Verify header -> Jira field mapping only, create nothing (default):
    ./scripts/create_jira_tickets.py --example stata

    # Create just the Matlab tickets:
    ./scripts/create_jira_tickets.py --example matlab --execute

    # Create all three example sets:
    ./scripts/create_jira_tickets.py --example all --execute
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from jira import JIRA
from jira.exceptions import JIRAError

# CSV headers that the Jira CSV importer mapped by hand and that therefore do
# not match any Jira field name. Used only as a fallback when the mapping file
# does not cover the header; override with --map.
HEADER_ALIASES = {
    "subject": "summary",
    "email": "assignee",
    "openicpsr": "openICPSR Project Number",
}


REPO_ROOT = Path(__file__).resolve().parents[1]
TRAINING_DIR = REPO_ROOT / "Training"
EXAMPLE_SUFFIX = "-example.csv"

# The training tickets are always plain Tasks; subtasks are added later by hand.
ISSUE_TYPE = "Task"

# New issues open in "Open"; the aide is expected to find them already assigned.
TARGET_STATUS = "Assigned"


def discover_examples(training_dir: Path) -> dict[str, Path]:
    """{short name: path} for every Training/<name>-example.csv, e.g. 'stata'."""
    return {
        path.name[: -len(EXAMPLE_SUFFIX)].lower(): path
        for path in sorted(training_dir.glob(f"*{EXAMPLE_SUFFIX}"))
    }


def select_csv_files(args) -> list[Path]:
    """Combine explicit CSV paths with any --example selections, in that order."""
    examples = discover_examples(args.training_dir)
    available = ", ".join(sorted(examples)) or "none found"

    selected = list(args.csv_files)
    for name in args.example:
        if name.lower() == "all":
            selected.extend(examples[key] for key in sorted(examples))
            continue
        path = examples.get(name.lower())
        if not path:
            sys.exit(f"Error: unknown --example '{name}'. Available in {args.training_dir}: {available}")
        selected.append(path)

    if not selected:
        sys.exit(
            "Error: nothing to import. Pass CSV paths, or --example with one of: "
            f"{available} (or 'all')."
        )

    # Preserve order, drop repeats (e.g. --example stata alongside the same path,
    # which reach us as an absolute and a relative Path for the same file).
    unique: list[Path] = []
    seen_paths = set()
    for path in selected:
        resolved = path.resolve()
        if resolved not in seen_paths:
            seen_paths.add(resolved)
            unique.append(path)
    return unique


def default_base_url() -> str | None:
    """Server URL from $JIRA_URL, else from the aea-editor-scripts package."""
    from_env = os.environ.get("JIRA_URL")
    if from_env:
        return from_env
    try:
        from aea_editor_scripts.jira_purge_query import JIRA_BASE_URL
    except ImportError:
        return None
    return JIRA_BASE_URL


def get_jira_client(base_url: str) -> JIRA:
    username = os.environ.get("JIRA_USERNAME")
    api_key = os.environ.get("JIRA_API_KEY")
    if not username or not api_key:
        sys.exit("Error: JIRA_USERNAME and JIRA_API_KEY environment variables must be set")

    try:
        return JIRA(server=base_url, basic_auth=(username, api_key), options={"verify": True})
    except Exception as exc:  # noqa: BLE001 - surface any auth/network failure the same way
        sys.exit(
            f"Error connecting to Jira at {base_url}: {exc}\n"
            "Verify JIRA_API_KEY is an API token (not a password) and that your "
            "account has access to this site."
        )


def normalize(name: str) -> str:
    """Fold a field or header name for tolerant comparison ('Due date' -> 'duedate')."""
    return re.sub(r"[^a-z0-9]", "", name.lower())


def load_mapping_file(path: Path) -> dict:
    """Read the saved Jira CSV-importer configuration, if present."""
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Warning: could not read {path}: {exc}", file=sys.stderr)
        return {}


def mapping_file_targets(config: dict) -> dict[str, str]:
    """CSV header -> Jira field id, as recorded by the Jira CSV importer."""
    targets = {}
    for header, spec in (config.get("config.field.mappings") or {}).items():
        if spec.get("jira.field"):
            targets[header] = spec["jira.field"]
        elif spec.get("existing.custom.field"):
            targets[header] = f"customfield_{spec['existing.custom.field']}"
    return targets


def fetch_create_fields(jira: JIRA, project: str) -> dict:
    """Return {field id: field metadata} for the project's Task create screen."""
    meta = jira.createmeta(projectKeys=project, expand="projects.issuetypes.fields")
    projects = meta.get("projects") or []
    if not projects:
        sys.exit(f"Error: project '{project}' not found, or you cannot create issues in it")

    issue_types = projects[0]["issuetypes"]
    for candidate in issue_types:
        if candidate["name"].lower() == ISSUE_TYPE.lower():
            return candidate["fields"]

    names = ", ".join(sorted(it["name"] for it in issue_types))
    sys.exit(f"Error: issue type '{ISSUE_TYPE}' not available in {project}. Available: {names}")


def resolve_headers(
    headers: list[str],
    fields: dict,
    file_targets: dict[str, str],
    overrides: dict[str, str],
) -> tuple[dict[str, str], list[str]]:
    """Map each CSV header to a Jira field id. Returns (mapping, unmapped headers)."""
    by_name = {normalize(meta["name"]): fid for fid, meta in fields.items()}

    def to_field_id(target: str) -> str | None:
        if target in fields:
            return target
        return by_name.get(normalize(target))

    mapping: dict[str, str] = {}
    unmapped: list[str] = []
    for header in headers:
        clean = header.strip()
        candidates = [
            overrides.get(clean),
            file_targets.get(clean),
            clean,
            HEADER_ALIASES.get(normalize(clean)),
        ]
        for candidate in candidates:
            if not candidate:
                continue
            field_id = to_field_id(candidate)
            if field_id:
                mapping[header] = field_id
                break
        else:
            unmapped.append(header)
    return mapping, unmapped


class UserResolver:
    """Resolve an email address to an accountId assignable in the project."""

    def __init__(self, jira: JIRA, base_url: str, project: str):
        self.jira = jira
        self.base_url = base_url.rstrip("/")
        self.project = project
        self.cache: dict[str, str] = {}

    def account_id(self, email: str) -> str:
        if email in self.cache:
            return self.cache[email]

        response = self.jira._session.get(
            f"{self.base_url}/rest/api/3/user/assignable/search",
            params={"project": self.project, "query": email, "maxResults": 5},
        )
        users = response.json()
        if not users:
            raise ValueError(f"no user assignable in {self.project} matches '{email}'")
        if len(users) > 1:
            names = ", ".join(u.get("displayName", u["accountId"]) for u in users)
            raise ValueError(f"'{email}' is ambiguous, matches: {names}")

        self.cache[email] = users[0]["accountId"]
        return self.cache[email]


def coerce(value: str, meta: dict, users: UserResolver, date_format: str):
    """Convert a CSV cell to the payload shape the field's schema expects."""
    schema = meta.get("schema", {})
    kind = schema.get("type")

    if kind == "user":
        return {"accountId": users.account_id(value)}

    if kind == "date":
        return datetime.strptime(value, date_format).date().isoformat()

    if kind == "datetime":
        return datetime.strptime(value, date_format).isoformat()

    if kind == "number":
        number = float(value)
        return int(number) if number.is_integer() else number

    if kind == "option":
        return {"value": allowed_value(value, meta)}

    if kind == "array":
        items = [item.strip() for item in value.split(";") if item.strip()]
        if schema.get("items") == "option":
            return [{"value": allowed_value(item, meta)} for item in items]
        return items

    return value


def allowed_value(value: str, meta: dict) -> str:
    """Return the canonical option value, or raise if the field does not offer it."""
    allowed = [option["value"] for option in meta.get("allowedValues", []) if "value" in option]
    for option in allowed:
        if option.lower() == value.lower():
            return option
    raise ValueError(f"'{value}' is not an allowed value for '{meta['name']}'. Allowed: {', '.join(allowed)}")


def transition_to(jira: JIRA, issue, status: str) -> str | None:
    """Move `issue` into `status`. Returns None on success, else why it could not."""
    if issue.fields.status.name.lower() == status.lower():
        return None

    transitions = jira.transitions(issue)
    for transition in transitions:
        if transition["to"]["name"].lower() == status.lower():
            try:
                jira.transition_issue(issue, transition["id"])
            except JIRAError as exc:
                return f"transition '{transition['name']}' failed: {exc.text or exc}"
            return None

    offered = ", ".join(f"{t['name']} -> {t['to']['name']}" for t in transitions) or "none"
    return f"no transition to '{status}' from '{issue.fields.status.name}' (offered: {offered})"


def search_all_issues(jira: JIRA, jql: str, fields: list[str]):
    """Every issue matching `jql`, paging through the whole result set.

    Jira Cloud retired the startAt-paginated search endpoint, so prefer the
    token-paginated one; it returns None on a Server/Data Center instance, where
    the original endpoint still works. maxResults=False means "fetch every page".
    """
    issues = None
    if hasattr(jira, "enhanced_search_issues"):
        issues = jira.enhanced_search_issues(jql, maxResults=False, fields=fields)
    if issues is None:
        issues = jira.search_issues(jql, maxResults=False, fields=fields)
    return issues


def existing_issues(jira: JIRA, project: str) -> set[tuple[str, str]]:
    """(summary, assignee accountId) of every issue already in the project."""
    issues = search_all_issues(jira, f'project = "{project}"', ["summary", "assignee"])
    return {
        (issue.fields.summary, getattr(issue.fields.assignee, "accountId", ""))
        for issue in issues
    }


def build_payload(row: dict, mapping: dict[str, str], fields: dict, users: UserResolver, date_format: str) -> dict:
    payload = {}
    for header, field_id in mapping.items():
        value = (row.get(header) or "").strip()
        if not value:
            continue
        try:
            payload[field_id] = coerce(value, fields[field_id], users, date_format)
        except ValueError as exc:
            raise ValueError(f"column '{header}': {exc}") from exc
    return payload


def process_csv(path: Path, args, jira, fields, file_targets, overrides, users, project, seen):
    """Create (or dry-run) one issue per row. Returns (created, skipped, failed)."""
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = [h for h in (reader.fieldnames or []) if h and h.strip()]
        rows = list(reader)

    mapping, unmapped = resolve_headers(headers, fields, file_targets, overrides)

    print(f"\n=== {path} ({len(rows)} rows)")
    for header in headers:
        if header in mapping:
            field_id = mapping[header]
            print(f"  {header:<32} -> {field_id:<20} ({fields[field_id]['name']})")
        else:
            print(f"  {header:<32} -> UNMAPPED")
    if unmapped:
        if not args.allow_unmapped:
            print(
                f"\nError: no Jira field on the '{ISSUE_TYPE}' create screen matches: "
                f"{', '.join(unmapped)}\nUse --map 'Header=field' to point them somewhere, "
                "or --allow-unmapped to drop them.",
                file=sys.stderr,
            )
            return 0, 0, len(rows), 0
        print(f"  (dropping unmapped columns: {', '.join(unmapped)})")

    created = skipped = failed = unmoved = 0
    for number, row in enumerate(rows, start=2):  # start=2: header is line 1
        if args.limit and created + skipped >= args.limit:
            break
        try:
            payload = build_payload(row, mapping, fields, users, args.date_format)
        except ValueError as exc:
            print(f"  line {number}: ERROR {exc}", file=sys.stderr)
            failed += 1
            continue

        summary = payload.get("summary", "")
        assignee = payload.get("assignee", {}).get("accountId", "")
        label = f"{summary} / {row.get('email', '').strip()}"

        if args.skip_existing and (summary, assignee) in seen:
            print(f"  line {number}: SKIP (already exists) {label}")
            skipped += 1
            continue

        payload.update({"project": {"key": project}, "issuetype": {"name": ISSUE_TYPE}})

        if not args.execute:
            destination = f" -> {TARGET_STATUS}" if args.transition else ""
            print(f"  line {number}: DRY-RUN would create{destination} {label}")
            created += 1
            continue

        try:
            issue = jira.create_issue(fields=payload)
        except JIRAError as exc:
            print(f"  line {number}: ERROR {exc.text or exc}", file=sys.stderr)
            failed += 1
            continue

        seen.add((summary, assignee))
        created += 1

        problem = transition_to(jira, issue, TARGET_STATUS) if args.transition else None
        if problem:
            unmoved += 1
            print(f"  line {number}: created {issue.key} {label}")
            print(f"  line {number}: WARNING {issue.key} left in '{issue.fields.status.name}': {problem}",
                  file=sys.stderr)
        else:
            status = TARGET_STATUS if args.transition else issue.fields.status.name
            print(f"  line {number}: created {issue.key} [{status}] {label}")

    return created, skipped, failed, unmoved


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Bulk-create Jira issues from the Training CSVs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("csv_files", nargs="*", type=Path, help="CSV file(s) to import")
    parser.add_argument(
        "--example",
        action="append",
        default=[],
        metavar="NAME",
        help="Import Training/<NAME>-example.csv (e.g. stata, matlab, confidential), "
        "or 'all' for every one of them; repeatable",
    )
    parser.add_argument(
        "--training-dir",
        type=Path,
        default=TRAINING_DIR,
        help="Directory searched by --example (default: %(default)s)",
    )
    parser.add_argument("--project", help="Jira project key (default: from --mapping-file)")
    parser.add_argument("--jira-url", default=default_base_url(), help="Jira server URL")
    parser.add_argument(
        "--mapping-file",
        type=Path,
        default=TRAINING_DIR / "jira-import-mapping.txt",
        help="Saved Jira CSV-importer configuration used for project key and header mappings",
    )
    parser.add_argument(
        "--map",
        action="append",
        default=[],
        metavar="HEADER=FIELD",
        help="Override one header's target (Jira field name or id); repeatable",
    )
    parser.add_argument(
        "--date-format",
        default="%m/%d/%Y",
        help="strptime format of date columns (default: %%m/%%d/%%Y, matching the Training CSVs)",
    )
    parser.add_argument("--allow-unmapped", action="store_true", help="Drop headers with no matching Jira field")
    parser.add_argument(
        "--no-skip-existing",
        dest="skip_existing",
        action="store_false",
        help="Create issues even if the project already has one with the same summary and assignee",
    )
    parser.add_argument(
        "--no-transition",
        dest="transition",
        action="store_false",
        help=f"Leave new issues in their initial status instead of moving them to '{TARGET_STATUS}'",
    )
    parser.add_argument("--limit", type=int, help="Process at most this many rows per file")
    parser.add_argument("--execute", action="store_true", help="Actually create issues (default: dry run)")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)

    csv_files = select_csv_files(args)

    if not args.jira_url:
        sys.exit("Error: no Jira URL. Pass --jira-url or set JIRA_URL.")

    overrides = {}
    for item in args.map:
        header, _, target = item.partition("=")
        if not target:
            sys.exit(f"Error: --map expects HEADER=FIELD, got '{item}'")
        overrides[header.strip()] = target.strip()

    config = load_mapping_file(args.mapping_file)
    file_targets = mapping_file_targets(config)
    project = args.project or (config.get("config.project") or {}).get("project.key")
    if not project:
        sys.exit("Error: no project key. Pass --project or provide a --mapping-file that names one.")

    jira = get_jira_client(args.jira_url)
    fields = fetch_create_fields(jira, project)
    users = UserResolver(jira, args.jira_url, project)

    print(f"Site:       {args.jira_url}")
    print(f"Project:    {project}")
    print(f"Issue type: {ISSUE_TYPE}")
    print(f"Transition: {TARGET_STATUS if args.transition else 'left as created'}")
    print(f"Mode:       {'EXECUTE' if args.execute else 'DRY RUN (use --execute to create)'}")

    seen = existing_issues(jira, project) if args.skip_existing else set()

    totals = [0, 0, 0, 0]
    for path in csv_files:
        if not path.is_file():
            print(f"\n=== {path}\n  ERROR: file not found", file=sys.stderr)
            totals[2] += 1
            continue
        counts = process_csv(path, args, jira, fields, file_targets, overrides, users, project, seen)
        totals = [total + count for total, count in zip(totals, counts)]

    verb = "created" if args.execute else "would create"
    summary = f"\nTotal: {totals[0]} {verb}, {totals[1]} skipped, {totals[2]} failed"
    if totals[3]:
        summary += f", {totals[3]} created but not moved to '{TARGET_STATUS}'"
    print(summary)
    return 1 if totals[2] or totals[3] else 0


if __name__ == "__main__":
    sys.exit(main())
