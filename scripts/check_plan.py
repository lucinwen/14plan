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

    # V5: task-operations manuals must match each 10-hour DAILY schedule precisely.
    table_re = re.compile(
        r"^\| (\d{2}:\d{2}–\d{2}:\d{2}) \| (\d+(?:\.\d+)?)h \| .* \|$",
        re.MULTILINE,
    )
    stages_re = re.compile(
        r"^### 第(\d+)阶段｜(\d{2}:\d{2}–\d{2}:\d{2})（(\d+)分钟）$",
        re.MULTILINE,
    )
    task_index = ROOT / "TASK_GUIDES" / "README.md"
    worklog = ROOT / "TASK_GUIDES" / "WORKLOG_TEMPLATE.md"
    if not task_index.is_file():
        errors.append("Missing TASK_GUIDES/README.md")
    if not worklog.is_file():
        errors.append("Missing TASK_GUIDES/WORKLOG_TEMPLATE.md")
    for day_num in range(1, 15):
        id_ = f"{day_num:02d}"
        daily = ROOT / "DAILY" / f"day-{id_}.md"
        guide = ROOT / "TASK_GUIDES" / f"day-{id_}.md"
        answer = ROOT / "TASK_GUIDES" / "ANSWERS" / f"day-{id_}.md"
        if not guide.is_file():
            errors.append(f"Missing TASK_GUIDES/day-{id_}.md")
            continue
        if not answer.is_file():
            errors.append(f"Missing TASK_GUIDES/ANSWERS/day-{id_}.md")
            continue
        guide_text = guide.read_text(encoding="utf-8")
        answer_text = answer.read_text(encoding="utf-8")
        if len(guide_text.strip()) < 1800:
            errors.append(f"Day {id_} task manual too sparse")
        if len(answer_text.strip()) < 900:
            errors.append(f"Day {id_} answer manual too sparse")
        if f"ANSWERS/day-{id_}.md" not in guide_text:
            errors.append(f"Day {id_} guide does not link to its answer")
        if f"../day-{id_}.md" not in answer_text:
            errors.append(f"Day {id_} answer missing return link")
        if not daily.is_file():
            continue
        daily_text = daily.read_text(encoding="utf-8")
        if f"../TASK_GUIDES/day-{id_}.md" not in daily_text:
            errors.append(f"Day {id_} DAILY missing task guide link")
        if f"../TASK_GUIDES/ANSWERS/day-{id_}.md" not in daily_text:
            errors.append(f"Day {id_} DAILY missing answer link")
        expected = table_re.findall(daily_text)
        stages = stages_re.findall(guide_text)
        target_count = 8 if day_num == 14 else 7
        if len(expected) != target_count or len(stages) != target_count:
            errors.append(
                f"Day {id_}: stage count expected {target_count}, got "
                f"schedule={len(expected)}, tutorial={len(stages)}"
            )
            continue
        total = 0
        for i, ((time_range, hours), (stage_n, stage_range, minutes)) in enumerate(
            zip(expected, stages), 1
        ):
            delta_minutes = round(float(hours) * 60)
            total += delta_minutes
            if (
                int(stage_n) != i
                or time_range != stage_range
                or int(minutes) != delta_minutes
            ):
                errors.append(
                    f"Day {id_} stage {i}: schedule and task-guide time mismatch"
                )
        if total != 600:
            errors.append(f"Day {id_}: total is {total} min, expected 600")
        if "未运行" not in guide_text and "未实测" not in guide_text:
            errors.append(f"Day {id_}: no unverified-result warning")
    
    # V6 content sanity: each day needs a domain-specific worked practice
    # and original timers must not claim more practice than their stage budget.
    generic_phrases = (
        "如果输入、观测可靠性、机器人配置或预算改变，哪些假设可能失效？",
        "举一个改变初始条件后会失败的反例，并说谁负责报告或修复。",
        "哪一种输入改变会让这条回答不再成立？需什么验证来确认？",
    )
    for day_num in range(1, 15):
        ident = f"{day_num:02d}"
        guide = ROOT / "TASK_GUIDES" / f"day-{ident}.md"
        answer = ROOT / "TASK_GUIDES" / "ANSWERS" / f"day-{ident}.md"
        if not guide.is_file() or not answer.is_file():
            continue
        guide_content = guide.read_text(encoding="utf-8")
        answer_content = answer.read_text(encoding="utf-8")
        if "## 强化练习" not in guide_content:
            errors.append(f"Day {ident}: missing worked exercise")
        if f"## Day{ident}" not in answer_content:
            errors.append(f"Day {ident}: missing specific answer explanation")
        for phrase in generic_phrases:
            if phrase in answer_content:
                errors.append(f"Day {ident}: repeated generic answer instead of specific follow-up")
    interview13 = ROOT / "TASK_GUIDES" / "day-13.md"
    interview14 = ROOT / "TASK_GUIDES" / "day-14.md"
    if interview13.is_file() and "2. **45分钟｜认真操作：" not in interview13.read_text(encoding="utf-8"):
        errors.append("Day 13 needs an actual 45min interview block")
    if interview14.is_file() and interview14.read_text(encoding="utf-8").count("2. **45分钟｜认真操作：") < 2:
        errors.append("Day 14 needs two real 45min interview blocks")

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
    print("PASS: all 14 daily pages, 31 resources, 14 deep worked guides/answers, real 45min mocks and 600 min/day")
