# LDI-Research-Aide


Responsibilities and Instruction Manuals for the Research Aide Position

see [index.md](index.md) for more details.

## Training tickets

The `Training/` folder holds the CSVs used to create the practice Jira tickets that
new research aides work through. Two scripts manage them.

### 1. Regenerate the CSVs

`Training/emails.csv` is the list of current aides; each `Training/*-example.csv` is
generated from the matching file in `Training/templates/` by substituting every email
in turn.

**Just edit `Training/emails.csv` or a file in `Training/templates/` and push.** The
[Generate Training CSVs](.github/workflows/generate-training-csvs.yml) workflow
regenerates the three CSVs and commits them back to the branch, so you do not need to
run the generator yourself. On a pull request it cannot push, so it fails instead to
tell you the committed CSVs are stale.

To preview the result locally:

```bash
python3 scripts/generate_training_csvs.py
```

Never edit `Training/*-example.csv` by hand — the next run overwrites it.

### 2. Create the Jira tickets

`scripts/create_jira_tickets.py` creates one Jira issue per CSV row and moves it
from `Open` to `Assigned`. It replaces the manual "Import from CSV" flow in the Jira
UI, whose saved configuration is kept in
`Training/jira-import-mapping.txt`.

Prerequisites:

- `pip install jira` (already present if the `aea-editor-scripts` package is installed)
- `JIRA_USERNAME` — your Atlassian account email
- `JIRA_API_KEY` — an API token from <https://id.atlassian.com/manage-profile/security/api-tokens>
- The server URL, taken from `--jira-url`, else `$JIRA_URL`, else the constant exported
  by `aea_editor_scripts.jira_purge_query` if that package is installed.

Pick which set to create with `--example`:

```bash
# Dry run (the default) — verifies every column maps to a real Jira field, creates nothing
python3 scripts/create_jira_tickets.py --example stata

# Create one set
python3 scripts/create_jira_tickets.py --example matlab --execute
python3 scripts/create_jira_tickets.py --example confidential --execute

# Create all three
python3 scripts/create_jira_tickets.py --example all --execute
```

`--example` is repeatable (`--example stata --example matlab`), and explicit CSV paths
still work in place of it. **Nothing is created without `--execute`.**

Useful options:

| Option | Effect |
| --- | --- |
| `--execute` | Actually create issues; without it the run is a dry run |
| `--example NAME` | Import `Training/<NAME>-example.csv`; `all` selects every one |
| `--project KEY` | Override the project key (default comes from `jira-import-mapping.txt`) |
| `--limit N` | Process at most N rows per file — good for a first real test |
| `--no-skip-existing` | Create even if a ticket with the same summary and assignee exists |
| `--no-transition` | Leave new tickets in `Open` instead of moving them to `Assigned` |
| `--map 'Header=field'` | Point a CSV column at a specific Jira field name or id |
| `--allow-unmapped` | Drop columns with no matching Jira field instead of aborting |
| `--date-format FMT` | `strptime` format of date columns (default `%m/%d/%Y`) |

Notes:

- Tickets are always created as issue type **Task**, then transitioned to **Assigned**.
  A ticket whose workflow offers no route to `Assigned` is still created, but is
  reported as a warning and left in `Open`.
- Before creating anything, the script resolves every CSV header against the Task
  **create screen** of the target project and prints the mapping. A header with no
  matching field aborts the run. If a field exists in Jira but isn't offered here, it
  needs adding to the Task create screen in the Jira project settings.
- Assignees are matched from the `email` column to a Jira account assignable in the
  project; an unknown or ambiguous address fails that row and leaves the rest alone.
- Re-runs are safe: rows whose summary and assignee already exist in the project are
  skipped. Note that skipping means they are *not* updated, so if a template gains a
  column, existing tickets keep their old values.
