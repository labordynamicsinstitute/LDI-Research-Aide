from __future__ import annotations

from pathlib import Path
import csv


ROOT = Path(__file__).resolve().parents[1]
TRAINING_DIR = ROOT / "Training"
EMAILS_FILE = TRAINING_DIR / "emails.csv"
TEMPLATES_DIR = TRAINING_DIR / "templates"

TARGETS = {
    "Confidential-example.csv": "Confidential-example.template.csv",
    "Matlab-example.csv": "Matlab-example.template.csv",
    "Stata-example.csv": "Stata-example.template.csv",
}


def read_emails(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if "email" not in (reader.fieldnames or []):
            raise ValueError(f"{path} must contain an 'email' column header")

        emails = [row["email"].strip() for row in reader if row.get("email", "").strip()]

    if not emails:
        raise ValueError(f"No emails found in {path}")

    return emails


def read_template(path: Path) -> tuple[str, str]:
    lines = [line.rstrip("\r\n") for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(lines) < 2:
        raise ValueError(f"Template file {path} must contain at least header and one template row")

    header = lines[0]
    row_template = lines[1]
    if "{email}" not in row_template:
        raise ValueError(f"Template row in {path} must include '{{email}}' placeholder")

    return header, row_template


def generate_csv(output_path: Path, header: str, row_template: str, emails: list[str]) -> None:
    rows = [row_template.replace("{email}", email) for email in emails]
    output = "\n".join([header, *rows]) + "\n"
    output_path.write_text(output, encoding="utf-8", newline="")


def main() -> None:
    emails = read_emails(EMAILS_FILE)

    for output_name, template_name in TARGETS.items():
        template_path = TEMPLATES_DIR / template_name
        output_path = TRAINING_DIR / output_name
        header, row_template = read_template(template_path)
        generate_csv(output_path, header, row_template, emails)
        print(f"Wrote {output_path.relative_to(ROOT)} ({len(emails)} rows)")


if __name__ == "__main__":
    main()