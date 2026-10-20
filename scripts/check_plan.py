"""Check internal Markdown links and key learning-plan consistency locally/CI."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def check() -> list[str]:
    errors: list[str] = []
    days = [ROOT / "DAILY" / f"day-{n:02d}.md" for n in range(1, 15)]
    for day in days:
        if not day.is_file():
            errors.append(f"Missing day: {day.relative_to(ROOT)}")
        elif "10h" not in day.read_text(encoding="utf-8"):
            errors.append(f"No 10h budget: {day.relative_to(ROOT)}")
    required = [
        "RELATED_WORK.md", "ADMISSION_PREP.md", "minilab/README.md",
        "minilab/validate.py", "minilab/tests/test_validate.py",
        "PLAN_14_DAYS.md", "PAPER_READING.md",
    ]
    for rel in required:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    matcher = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)]+)\)")
    md_files = list(ROOT.rglob("*.md"))
    for md in md_files:
        rel = md.relative_to(ROOT)
        contents = md.read_text(encoding="utf-8")
        # Ignore fenced code before scanning links.
        contents = re.sub(r"(?ms)^\x60\x60\x60.*?^\x60\x60\x60.*?$", "", contents)
        for raw in matcher.findall(contents):
            link = raw.split(" ", 1)[0].strip("<>").split("#", 1)[0]
            if not link or link.startswith(("http:", "https:", "mailto:", "/")):
                continue
            target = (md.parent / unquote(link)).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"{rel}: broken local link {raw}")
    admission = ROOT / "ADMISSION_PREP.md"
    if admission.is_file():
        page = admission.read_text(encoding="utf-8")
        if "10/30" not in page or "10/28" not in page:
            errors.append("Admission milestones 10/28 and 10/30 not both present")
    return errors


if __name__ == "__main__":
    issues = check()
    if issues:
        print("Plan checks failed:")
        for item in issues:
            print(" -", item)
        raise SystemExit(1)
    print("PASS: 14 day pages, admissions deadlines and internal Markdown paths")
