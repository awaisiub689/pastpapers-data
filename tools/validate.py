#!/usr/bin/env python3
"""Schema validation — galat data live na jaye."""
import json, sys, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

man = json.loads((ROOT / "manifest.json").read_text())
for key in ("schema_version", "content_version", "classes"):
    if key not in man:
        errors.append(f"manifest: '{key}' ghayab")

for c in man.get("classes", []):
    for s in c.get("subjects", []):
        p = ROOT / s["file"]
        if not p.exists():
            errors.append(f"file ghayab: {s['file']}")
            continue
        d = json.loads(p.read_text())
        if d.get("schema_version") != man["schema_version"]:
            errors.append(f"{s['file']}: schema_version mismatch")
        if d.get("class") != c["class"] or d.get("subject") != s["slug"]:
            errors.append(f"{s['file']}: class/subject manifest se match nahi")
        if len(d.get("questions", [])) != s["questions"]:
            errors.append(f"{s['file']}: questions count {len(d['questions'])} != manifest {s['questions']}")
        for q in d.get("questions", [])[:200]:
            for key in ("id", "text", "times", "papers"):
                if key not in q:
                    errors.append(f"{s['file']}: question may '{key}' ghayab")
                    break

if errors:
    print("FAIL")
    for e in errors[:20]:
        print("  -", e)
    sys.exit(1)
print(f"OK — {len(man['classes'])} classes, "
      f"{sum(len(c['subjects']) for c in man['classes'])} files validated")
