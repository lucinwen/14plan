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

    # Every original resource has a real child tutorial, not only a raw link.
    guide_dir = ROOT / "STUDY_GUIDES"
    index = guide_dir / "README.md"
    if not index.is_file():
        errors.append("Missing independent study-guide index")
    for prefix, total in (("R", 22), ("P", 9)):
        for number in range(1, total + 1):
            tag = f"{prefix}{number:02d}"
            path = guide_dir / f"{tag}.md"
            if not path.is_file():
                errors.append(f"Missing resource tutorial: {tag}")
            elif len(path.read_text(encoding="utf-8").strip()) < 700:
                errors.append(f"Resource tutorial too short to guide study: {tag}")

    for day in days:
        if not day.is_file():
            continue
        doc = day.read_text(encoding="utf-8")
        if "../STUDY_GUIDES/" not in doc:
            errors.append(f"Daily page missing child-tutorial link: {day.name}")
        if "先打开资源子教程" not in doc and "资源子教程" not in doc:
            errors.append(f"Daily page lacks clear tutorial entry: {day.name}")

    # Catch former incorrect Bilibili links before reintroducing confusion.
    resources = (ROOT / "RESOURCES.md").read_text(encoding="utf-8")
    for should_exist in (
        "BV1zi421v7Dr",  # 3DGS first episode, not old fourth episode
        "BV1t34y1F7sV",  # SAR lecture 1
        "BV1VC4y1N7Uy",  # SAR lecture 3
        "BV1b4hSe4EEV",  # actual breathing demo, not Capon angle demo
    ):
        if should_exist not in resources:
            errors.append(f"RESOURCES.md missing corrected video: {should_exist}")

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
    print("PASS: 14 daily pages, 31 child tutorials, corrected courses and internal Markdown paths")
