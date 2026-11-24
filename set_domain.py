#!/usr/bin/env python3
"""把站点内的老 WorkBuddy 域名替换为 Cloudflare Pages 域名。
用法: python set_domain.py [新域名，默认 chenread-install.pages.dev]
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NEW = sys.argv[1] if len(sys.argv) > 1 else "chenread-install.pages.dev"
if "://" in NEW:
    NEW = NEW.split("://", 1)[1].rstrip("/")

OLD_HOST = "chenread-install-75762.app.workbuddy.host"
OLD_SHARE = "?sharecode=G7H4LB75MQ"
OLD_NAMES = ["chenread-install.pages.dev"]
EXTS = {".html", ".js", ".json", ".css", ".txt", ".xml", ".webmanifest"}

changed = []
for p in ROOT.rglob("*"):
    if not p.is_file() or p.suffix.lower() not in EXTS:
        continue
    try:
        text = p.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    new = text.replace(OLD_HOST, NEW).replace(OLD_SHARE, "")
    for old in OLD_NAMES:
        if old != NEW:
            new = new.replace(old, NEW)
    if new != text:
        p.write_text(new, encoding="utf-8")
        changed.append(str(p.relative_to(ROOT)))

print(f"目标域名: https://{NEW}")
print(f"改写文件 {len(changed)} 个:")
for c in changed:
    print("  -", c)
