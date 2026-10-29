#!/usr/bin/env python3
"""Scan the repo for LeetCode solutions and regenerate the README stats.

What it does on every run:
  1. Finds solution files (any common language) anywhere in the repo.
  2. Works out each problem's number, title, difficulty and topic.
  3. Rewrites the Progress and Problem Log sections of README.md
     (between the <!-- ...:START --> and <!-- ...:END --> markers).
  4. Regenerates assets/progress.svg.

Problem pictures are linked next to the solution when they are found in the
problem's own folder (or an images/ subfolder), share the problem's file name
(0856-score-of-parentheses.png), or are named in a header line "Image: path".

Difficulty is detected in this order:
  1. A header comment in the file:   Difficulty: Medium
  2. A LeetHub-style README.md in the problem folder (<h3>Medium</h3>)
  3. A folder named Easy / Medium / Hard in the file's path
  4. scripts/problems_cache.json (remembered from earlier runs)
  5. The LeetCode website (looked up by the problem slug)

Run locally:  python scripts/update_readme.py            (add --offline to skip web lookups)
"""
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CACHE = ROOT / "scripts" / "problems_cache.json"
PROGRESS_SVG = ROOT / "assets" / "progress.svg"

CODE_EXT = {
    ".py", ".java", ".cpp", ".cc", ".c", ".cs", ".js", ".ts", ".go", ".rs",
    ".kt", ".swift", ".rb", ".php", ".scala", ".sql", ".dart", ".r",
}
SKIP_DIRS = {".git", ".github", "assets", "scripts", "node_modules", "venv", ".venv", "__pycache__"}
DIFFS = ("Easy", "Medium", "Hard")
LANG = {
    ".py": "Python", ".java": "Java", ".cpp": "C++", ".cc": "C++", ".c": "C",
    ".cs": "C#", ".js": "JavaScript", ".ts": "TypeScript", ".go": "Go",
    ".rs": "Rust", ".kt": "Kotlin", ".swift": "Swift", ".rb": "Ruby",
    ".php": "PHP", ".scala": "Scala", ".sql": "SQL", ".dart": "Dart", ".r": "R",
}
IMG_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
# folder names that only group files and are never used as a topic
GENERIC_DIRS = {"solutions", "solution", "src", "code", "leetcode", "problems"}
ICON = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
OFFLINE = "--offline" in sys.argv


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def pretty(slug):
    return " ".join(w.capitalize() for w in slug.split("-"))


def identify(path):
    """Return (number or None, slug) from the file name or its folder name."""
    for name in (path.stem, path.parent.name):
        m = re.match(r"^\s*(\d+)\s*[-_. ]+\s*(.+?)\s*$", name)
        if m:
            return int(m.group(1)), slugify(m.group(2))
    return None, slugify(path.stem)


def read_head(path, lines=40):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return "".join(next(f, "") for _ in range(lines))
    except OSError:
        return ""


def find_images(path, slug, head):
    """Images that belong to this solution.

    - Folder-per-problem layout: every image inside the problem folder
      (including an images/ subfolder) belongs to it.
    - Flat layout: images next to the file whose name starts with the
      problem name, e.g. 0856-score-of-parentheses.png or ...-2.png
    - Any layout: a header line   Image: ./path/to/picture.png
    """
    found = set()
    parent = path.parent
    folder_name = re.sub(r"^\d+[-_. ]+", "", parent.name)
    own_folder = parent != ROOT and slugify(folder_name) == slug
    if own_folder:
        for img in parent.rglob("*"):
            if img.is_file() and img.suffix.lower() in IMG_EXT:
                found.add(img)
    else:
        for d in (parent, parent / "images", parent / "img"):
            if not d.is_dir():
                continue
            for img in d.iterdir():
                stem = re.sub(r"^\d+[-_. ]+", "", img.stem)
                if img.is_file() and img.suffix.lower() in IMG_EXT and slugify(stem).startswith(slug):
                    found.add(img)
    for m in re.finditer(r"(?im)^\W*image\s*[:\-]\s*(\S+)\s*$", head):
        img = (parent / m.group(1)).resolve()
        if img.is_file() and img.suffix.lower() in IMG_EXT and ROOT in img.parents:
            found.add(img)
    return found


def fetch_leetcode(slug):
    if OFFLINE:
        return None
    query = {
        "query": "query q($s:String!){question(titleSlug:$s){questionFrontendId title difficulty topicTags{name}}}",
        "variables": {"s": slug},
    }
    req = urllib.request.Request(
        "https://leetcode.com/graphql",
        data=json.dumps(query).encode(),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Referer": f"https://leetcode.com/problems/{slug}/",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            q = json.load(resp)["data"]["question"]
        if not q:
            return None
        return {
            "number": int(q["questionFrontendId"]),
            "title": q["title"],
            "difficulty": q["difficulty"],
            "topic": (q["topicTags"][0]["name"] if q["topicTags"] else None),
        }
    except Exception as exc:  # network blocked, rate limited, bad slug...
        print(f"  ! lookup failed for {slug}: {exc}")
        return None


def collect():
    """Group solution files by problem slug."""
    problems = {}
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT)
        if not path.is_file() or path.suffix.lower() not in CODE_EXT:
            continue
        if any(part in SKIP_DIRS or part.startswith(".") for part in rel.parts[:-1]):
            continue
        number, slug = identify(path)
        if not slug:
            continue
        p = problems.setdefault(slug, {"slug": slug, "number": number, "files": [], "hints": {}, "images": set()})
        p["number"] = p["number"] or number
        p["files"].append(rel)

        # difficulty hint: header comment inside the file
        head = read_head(path)
        m = re.search(r"(?i)difficulty\s*[:\-]\s*(easy|medium|hard)", head)
        if m:
            p["hints"]["difficulty"] = m.group(1).capitalize()
        for img in find_images(path, slug, head):
            p["images"].add(img.relative_to(ROOT))
        # title hint: a header line like "856. Score of Parentheses"
        m = re.search(r"(?m)^\W*(\d+)\.\s+([A-Za-z][^\n]*?)\s*$", head)
        if m:
            p["number"] = p["number"] or int(m.group(1))
            p["hints"]["title"] = m.group(2)
        # topic hint: "Topic: Stack" in the header comment
        m = re.search(r"(?im)^\W*topic\s*[:\-]\s*(\S.*?)\s*$", head)
        if m:
            p["hints"]["topic"] = m.group(1)
        # difficulty hint: Easy/Medium/Hard folder in the path
        for part in rel.parts[:-1]:
            if part.capitalize() in DIFFS:
                p["hints"].setdefault("difficulty", part.capitalize())
        # topic hint: first folder that is not a difficulty or a numbered problem folder
        for part in rel.parts[:-1]:
            if (part.capitalize() in DIFFS or part.lower() in GENERIC_DIRS
                    or re.match(r"^\d+[-_. ]", part)):
                continue
            p["hints"].setdefault("topic", pretty(slugify(part)))
            break

        # LeetHub-style README in the problem folder
        folder_readme = path.parent / "README.md"
        if path.parent != ROOT and folder_readme.exists():
            text = read_head(folder_readme, 20)
            m = re.search(r"<h3>\s*(Easy|Medium|Hard)\s*</h3>", text, re.I)
            if m:
                p["hints"]["difficulty"] = m.group(1).capitalize()
            m = re.search(r"<h2>.*?>\s*(\d+)\.\s*([^<]+?)\s*</a>", text, re.S)
            if m:
                p["number"] = p["number"] or int(m.group(1))
                p["hints"].setdefault("title", m.group(2))
    return problems


def resolve(problems, cache):
    for slug, p in problems.items():
        info = dict(cache.get(slug, {}))
        hints = p["hints"]
        # fill gaps from the web only if something is missing
        if not (info.get("difficulty") or hints.get("difficulty")) or not info.get("title"):
            fetched = fetch_leetcode(slug)
            if fetched:
                info.update({k: v for k, v in fetched.items() if v})
        p["difficulty"] = hints.get("difficulty") or info.get("difficulty") or "Unknown"
        p["title"] = info.get("title") or hints.get("title") or pretty(slug)
        p["number"] = p["number"] or info.get("number")
        p["topic"] = hints.get("topic") or info.get("topic") or "—"
        cache[slug] = {
            "number": p["number"],
            "title": p["title"],
            "difficulty": p["difficulty"] if p["difficulty"] != "Unknown" else None,
            "topic": info.get("topic"),
        }
    return problems


def solution_links(files, images=()):
    links = []
    for f in sorted(files, key=str):
        label = LANG.get(f.suffix.lower(), f.suffix.lstrip("."))
        links.append(f"[{label}](./{quote(f.as_posix())})")
    images = sorted(images, key=str)
    for i, img in enumerate(images, 1):
        label = "🖼️ Image" if len(images) == 1 else f"🖼️ Image {i}"
        links.append(f"[{label}](./{quote(img.as_posix())})")
    return " · ".join(links)


def render_progress(counts, total):
    rows = [
        "| Difficulty | Solved |",
        "|---|---|",
    ]
    for d in DIFFS:
        rows.append(f"| {ICON[d]} {d} | {counts[d]} |")
    if counts["Unknown"]:
        rows.append(f"| ⚪ Unclassified | {counts['Unknown']} |")
    rows.append(f"| **Total** | **{total}** |")
    return "\n".join(rows)


def render_log(problems):
    def sort_key(p):
        return (p["number"] is None, p["number"] or 0, p["title"])

    rows = [
        "| # | Problem | Topic | Difficulty | Solution |",
        "|---|---|---|---|---|",
    ]
    for p in sorted(problems.values(), key=sort_key):
        num = p["number"] if p["number"] is not None else "–"
        link = f"[{p['title']}](https://leetcode.com/problems/{p['slug']}/)"
        diff = f"{ICON.get(p['difficulty'], '⚪')} {p['difficulty']}"
        rows.append(f"| {num} | {link} | {p['topic']} | {diff} | {solution_links(p['files'], p['images'])} |")
    if len(rows) == 2:
        rows.append("| – | _No solutions yet_ | | | |")
    return "\n".join(rows)


def render_svg(counts, total):
    colors = {"Easy": "#22c55e", "Medium": "#f59e0b", "Hard": "#ef4444"}
    bar_x, bar_w = 60, 1080
    parts, x = [], bar_x
    solved = sum(counts[d] for d in DIFFS)
    if solved:
        for i, d in enumerate(DIFFS):
            w = bar_w * counts[d] / solved
            if w > 0:
                parts.append(f'<rect x="{x:.1f}" y="92" width="{w:.1f}" height="26" fill="{colors[d]}"/>')
                x += w
    bar = "\n  ".join(parts)
    legend = []
    for i, d in enumerate(DIFFS):
        lx = 60 + i * 260
        legend.append(
            f'<circle cx="{lx + 8}" cy="152" r="8" fill="{colors[d]}"/>'
            f'<text x="{lx + 26}" y="158" font-size="18" fill="#e0e7ff">{d}: <tspan font-weight="700" fill="#ffffff">{counts[d]}</tspan></text>'
        )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="190" viewBox="0 0 1200 190">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <clipPath id="round"><rect x="{bar_x}" y="92" width="{bar_w}" height="26" rx="13"/></clipPath>
  </defs>
  <rect width="1200" height="190" rx="20" fill="url(#bg)"/>
  <g font-family="Segoe UI, Helvetica, Arial, sans-serif">
    <text x="60" y="56" font-size="24" font-weight="700" fill="#e0e7ff">Progress</text>
    <text x="1140" y="56" font-size="24" font-weight="800" fill="#5eead4" text-anchor="end">{total} solved</text>
    <rect x="{bar_x}" y="92" width="{bar_w}" height="26" rx="13" fill="#ffffff" fill-opacity="0.10"/>
    <g clip-path="url(#round)">
  {bar}
    </g>
    {''.join(legend)}
  </g>
</svg>
"""


def replace_block(text, name, body):
    pattern = re.compile(rf"(<!-- {name}:START -->)(.*?)(<!-- {name}:END -->)", re.S)
    if not pattern.search(text):
        print(f"  ! marker {name} not found in README.md, skipped")
        return text
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text)


def main():
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    problems = resolve(collect(), cache)

    counts = {d: 0 for d in DIFFS}
    counts["Unknown"] = 0
    for p in problems.values():
        counts[p["difficulty"] if p["difficulty"] in DIFFS else "Unknown"] += 1
    total = len(problems)

    text = README.read_text(encoding="utf-8")
    text = replace_block(text, "PROGRESS", render_progress(counts, total))
    text = replace_block(text, "LOG", render_log(problems))
    README.write_text(text, encoding="utf-8")

    PROGRESS_SVG.parent.mkdir(exist_ok=True)
    svg = render_svg(counts, total)
    PROGRESS_SVG.write_text(svg, encoding="utf-8")

    # GitHub and browsers cache README images, so a changed progress.svg can look stale.
    # A version tag that changes with the picture forces a fresh download.
    version = hashlib.md5(svg.encode("utf-8")).hexdigest()[:8]
    text = re.sub(r'src="\./assets/progress\.svg[^"]*"',
                  f'src="./assets/progress.svg?v={version}"', text)
    README.write_text(text, encoding="utf-8")
    CACHE.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")

    print(f"Updated README: {total} problems "
          f"(Easy {counts['Easy']}, Medium {counts['Medium']}, Hard {counts['Hard']}, unclassified {counts['Unknown']})")


if __name__ == "__main__":
    main()
