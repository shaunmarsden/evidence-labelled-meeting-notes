"""Count the blind scores by version of the skill.

Run from the repo root: python3 evaluations/checklist-in-skill/analyse.py
"""

import json
from pathlib import Path

HERE = Path(__file__).parent
MEASURES = [
    "1 Closing check",
    "2 Shape",
    "3 Traps",
    "4 No overstatement",
    "5 No invention",
    "A Says checklist missing",
    "B Gives checklist",
]

mapping = json.loads((HERE / "mapping.json").read_text())

scores = {}
for line in (HERE / "blind-scores.md").read_text().splitlines():
    cells = [c.strip() for c in line.strip("|").split("|")]
    if len(cells) == 9 and cells[0].startswith("e") and cells[0][1:].isdigit():
        scores[cells[0]] = [int(c) for c in cells[2:]]

assert sorted(scores) == sorted(mapping), "scores and mapping list different replies"

for arm in ("current", "inline"):
    ids = [r for r in scores if mapping[r]["arm"] == arm]
    words = [len((HERE / "replies" / f"{r}.txt").read_text().split()) for r in ids]
    print(f"{arm} ({len(ids)} replies, mean {sum(words) / len(words):.0f} words)")
    for i, name in enumerate(MEASURES):
        print(f"  {name}: {sum(scores[r][i] for r in ids)}")
    for model in ("opus", "haiku"):
        missing = sum(scores[r][5] for r in ids if mapping[r]["model"] == model)
        print(f"  A by {model}: {missing}")
