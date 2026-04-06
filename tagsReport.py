#!/usr/bin/env python3
from pathlib import Path
import re
from collections import Counter

VAULT_DIR = Path(__file__).resolve().parent  # raíz del vault (mismo directorio que este script)

TAG_PATTERN = re.compile(r'#[A-Za-z0-9/_\-]+')
counter = Counter()

for md in VAULT_DIR.rglob("*.md"):
    # saltar carpetas ocultas (.obsidian, .git, etc)
    if any(part.startswith(".") for part in md.parts):
        continue
    text = md.read_text(encoding="utf-8", errors="ignore")
    for tag in TAG_PATTERN.findall(text):
        counter[tag.lower()] += 1

# Top 100 tags
lines = ["# Tag report (top 100)\n\n"]
for tag, cnt in counter.most_common(100):
    lines.append(f"{tag}: {cnt}\n")

out_path = VAULT_DIR / "tag_report.txt"
out_path.write_text("".join(lines), encoding="utf-8")

print(f"Generado: {out_path}")