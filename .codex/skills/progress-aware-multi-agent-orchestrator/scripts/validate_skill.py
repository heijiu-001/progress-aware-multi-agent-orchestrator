#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
skill = ROOT / "SKILL.md"
errors = []

if not skill.exists():
    errors.append("Missing exact-case SKILL.md")
else:
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append("Invalid YAML frontmatter")
    else:
        front = m.group(1)
        if not re.search(r"^name:\s*\S+", front, re.M):
            errors.append("Missing name")
        if not re.search(r"^description:\s*.+", front, re.M):
            errors.append("Missing description")

    required_phrases = [
        "Structured development task sheet",
        "Structured acceptance sheet",
        "REQUIREMENT_DEFECT",
        "SPECIFICATION_DEFECT",
        "IMPLEMENTATION_DEFECT",
        "OBSERVE",
        "REASSESS",
        "completion envelope",
    ]
    lower = text.lower()
    for phrase in required_phrases:
        if phrase.lower() not in lower:
            errors.append(f"Missing required concept: {phrase}")

required_files = [
    "references/development-task-sheet.md",
    "references/acceptance-sheet.md",
    "references/diagnosis-policy.md",
    "references/completion-envelope.md",
    "references/dispatch-policy.md",
    "references/github-delivery.md",
]
for rel in required_files:
    if not (ROOT / rel).exists():
        errors.append(f"Missing {rel}")

if errors:
    print("Skill validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Skill validation passed.")
print(f"Skill path: {skill}")
