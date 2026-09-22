#!/usr/bin/env python
"""Validate a deck against the slides.mightora.io / Reveal.js parsing rules.

Usage:
    python validate-deck.py                       # validate every deck
    python validate-deck.py <deck-id> [...]       # validate named decks

Checks the things that actually break on stage:
  - meta.json exists and is valid JSON, with a known theme
  - slides.md is UTF-8 with no BOM (a BOM breaks the first slide's directive)
  - separators (--- and --) have blank lines around them, or slides merge
  - exactly one "Notes:" block per slide, or notes leak onto the screen
  - fenced code blocks are closed, and diagram fences are spelled correctly
  - no relative image/video paths (they resolve against slides.mightora.io)
Exit code is non-zero if any ERROR is found. WARNINGs do not fail.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DECKS = ROOT / "decks"
THEMES = {
    "black", "white", "league", "beige", "sky", "night",
    "serif", "simple", "solarized", "blood", "moon", "dracula",
}
errors = 0
warnings = 0


def err(msg):
    global errors
    errors += 1
    print(f"  ERROR   {msg}")


def warn(msg):
    global warnings
    warnings += 1
    print(f"  WARN    {msg}")


def check_meta(path):
    if not path.exists():
        err("meta.json missing - the platform will report 'metadata not found'")
        return
    raw = path.read_bytes()
    if raw[:3] == b"\xef\xbb\xbf":
        err("meta.json has a UTF-8 BOM - strip it")
    try:
        meta = json.loads(raw.decode("utf-8-sig"))
    except Exception as exc:
        err(f"meta.json is not valid JSON: {exc}")
        return
    for field in ("title", "description"):
        if not meta.get(field):
            warn(f"meta.json has no '{field}' - it shows on the landing page")
    theme = meta.get("theme")
    if theme and theme not in THEMES:
        err(f"theme '{theme}' is not a Reveal theme. One of: {', '.join(sorted(THEMES))}")
    if meta.get("published") is not True:
        warn("published is not true - the deck is hidden from the list (URL still works)")


def check_slides(path):
    if not path.exists():
        err("slides.md missing - only slides.md is supported for remote decks")
        return
    raw = path.read_bytes()
    if raw[:3] == b"\xef\xbb\xbf":
        err("slides.md has a UTF-8 BOM - it breaks the first slide's directive")
    try:
        src = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        err(f"slides.md is not valid UTF-8: {exc}")
        return

    lines = src.split("\n")
    if src.count("```") % 2:
        err("unclosed fenced code block (odd number of ```)")

    # Mask fenced code so separators inside it are ignored.
    masked, in_fence = [], False
    for line in lines:
        if line.startswith("```"):
            in_fence = not in_fence
            masked.append(None)
            continue
        masked.append(None if in_fence else line)

    h = [i for i, l in enumerate(masked) if l == "---"]
    v = [i for i, l in enumerate(masked) if l == "--"]

    for i in sorted(h + v):
        if i > 0 and masked[i - 1] not in (None, ""):
            err(f"line {i + 1}: separator needs a blank line BEFORE it, "
                f"or the slides merge (previous line: {lines[i - 1][:40]!r})")
        if i + 1 < len(masked) and masked[i + 1] not in (None, ""):
            err(f"line {i + 1}: separator needs a blank line AFTER it "
                f"(next line: {lines[i + 1][:40]!r})")

    # Split into slides and check speaker notes.
    cuts = sorted(h + v)
    slides, prev = [], 0
    for c in cuts:
        slides.append(lines[prev:c])
        prev = c + 1
    slides.append(lines[prev:])

    for n, slide in enumerate(slides, 1):
        count = sum(1 for l in slide if l.startswith("Notes:"))
        head = next((l for l in slide if l.strip().startswith("#")), "(no heading)")
        if count > 1:
            err(f"slide {n} ({head[:40]}) has {count} 'Notes:' blocks - only the "
                "first is notes, the rest render on screen")
        elif count == 0:
            warn(f"slide {n} ({head[:40]}) has no speaker notes")

    for lang in set(re.findall(r"^```(\w+)", src, re.M)):
        if lang.lower() in {"mermaidjs", "mmd", "puml", "plant-uml", "plantuml_"}:
            err(f"fence language '{lang}' will render blank - use exactly "
                "'mermaid' or 'plantuml'")

    # Relative asset paths break on remote decks.
    for m in re.finditer(r'!\[[^\]]*\]\((?!https?://|data:)([^)]+)\)', src):
        err(f"relative image path '{m.group(1)}' - remote decks need absolute URLs")
    for m in re.finditer(r'data-background-(?:image|video)="(?!https?://)([^"]+)"', src):
        warn(f"relative background asset '{m.group(1)}' - resolves against "
             "slides.mightora.io, not your repo. Use an absolute URL.")

    print(f"  {len(h) + 1} horizontal slides, {len(v)} vertical children, "
          f"{len(slides)} total")


def main():
    wanted = sys.argv[1:]
    if not DECKS.is_dir():
        print("No decks/ directory found.")
        return 1
    found = sorted(d for d in DECKS.iterdir() if d.is_dir())
    if wanted:
        found = [d for d in found if d.name in wanted]
        missing = set(wanted) - {d.name for d in found}
        for m in missing:
            print(f"{m}\n  ERROR   no such deck in decks/")
            globals()["errors"] = errors + 1
    if not found:
        print("No decks to validate.")
        return 1
    for deck in found:
        print(f"\n{deck.name}")
        if not re.fullmatch(r"[a-z0-9-]+", deck.name):
            err("deck id must be lowercase letters, numbers and hyphens only")
        check_meta(deck / "meta.json")
        check_slides(deck / "slides.md")
    print(f"\n{'-' * 52}\n{errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
