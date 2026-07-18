#!/usr/bin/env python3
"""Report Korean study-note progress across the curriculum.

Progress is DERIVED from the filesystem, never hand-maintained: a note at
`study/phase-NN/MM-slug.md` means that lesson is done. Nothing to tick off,
so nothing can drift out of sync. Same principle as `build_catalog.py`.

Lessons come from `catalog.json` (filesystem truth, rebuilt in CI). Notes are
matched to lessons by phase number + lesson slug, so a typo'd filename shows
up as an orphan instead of silently not counting.

Usage:
    python scripts/study_progress.py              # summary + next lesson
    python scripts/study_progress.py --phase 0    # one phase, lesson by lesson
    python scripts/study_progress.py --json       # machine-readable
    python scripts/study_progress.py --write      # regenerate study/PROGRESS.md

Exit codes:
    0 - always (this is a report, not a gate)
    1 - catalog.json missing, or orphan notes found under --strict

Stdlib only. Python 3.10+.

Note: stdout is reconfigured to UTF-8 so this runs on a Windows cp949 console
without needing PYTHONIOENCODING. Use `python`, not `python3` (on Windows the
latter is a Store alias that runs nothing and exits 0).
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "catalog.json"
STUDY_DIR = ROOT / "study"
PROGRESS_MD = STUDY_DIR / "PROGRESS.md"

BAR_WIDTH = 24


@dataclass
class PhaseProgress:
    num: int
    slug: str
    title: str
    total: int
    done_slugs: set[str] = field(default_factory=set)
    lessons: list[dict] = field(default_factory=list)

    @property
    def done(self) -> int:
        return len(self.done_slugs)

    @property
    def pct(self) -> float:
        return 100.0 * self.done / self.total if self.total else 0.0

    def bar(self, width: int = BAR_WIDTH) -> str:
        filled = round(width * self.done / self.total) if self.total else 0
        return "#" * filled + "." * (width - filled)


def load_catalog() -> dict:
    if not CATALOG_PATH.is_file():
        sys.stderr.write(
            "error: catalog.json not found. Run: python scripts/build_catalog.py\n"
        )
        raise SystemExit(1)
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def collect_notes() -> dict[int, set[str]]:
    """Map phase number -> set of lesson slugs that have a study note."""
    notes: dict[int, set[str]] = {}
    if not STUDY_DIR.is_dir():
        return notes
    for phase_dir in sorted(STUDY_DIR.glob("phase-*")):
        if not phase_dir.is_dir():
            continue
        try:
            phase_num = int(phase_dir.name.removeprefix("phase-"))
        except ValueError:
            continue
        for note in sorted(phase_dir.glob("*.md")):
            notes.setdefault(phase_num, set()).add(note.stem)
    return notes


def parse_frontmatter(text: str) -> dict[str, object] | None:
    """Minimal YAML-subset parser: scalars, inline lists, and block lists.

    `scripts/_lib.py` skips indented lines, so it cannot read the block-list
    `keywords:` used by study notes (error strings contain commas, which an
    inline list would split). This handles both forms.
    """
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    result: dict[str, object] = {}
    key: str | None = None
    for raw in text[4:end].split("\n"):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        stripped = raw.strip()
        if raw[0] in (" ", "\t") and stripped.startswith("- "):
            if key:
                result.setdefault(key, [])
                if isinstance(result[key], list):
                    result[key].append(stripped[2:].strip().strip("'\""))
            continue
        if ":" not in raw:
            continue
        key, _, value = raw.partition(":")
        key, value = key.strip(), value.strip()
        if not value:
            result[key] = []
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            result[key] = [i.strip().strip("'\"") for i in inner.split(",") if i.strip()]
        else:
            result[key] = value.strip("'\"")
    return result


REQUIRED_FM = ("title", "description", "date", "slug", "series")
LESSON_ONLY_FM = ("phase", "lesson")
TITLE_MAX = 60
DESC_MIN, DESC_MAX = 80, 200
TAGS_MIN, TAGS_MAX = 3, 6
KEYWORDS_MIN = 5

# Root-level study/*.md that are infrastructure, not published posts.
NON_POST_FILES = {"README.md", "PROGRESS.md", "glossary-ko.md", "tags-ko.md"}


def iter_posts() -> list[tuple[Path, bool]]:
    """Every publishable markdown file, flagged as (path, is_lesson_note).

    Lesson notes live in `study/phase-NN/`. Root-level posts (e.g. the series
    intro) are published too but carry no phase/lesson numbers.
    """
    posts: list[tuple[Path, bool]] = []
    if not STUDY_DIR.is_dir():
        return posts
    for md in sorted(STUDY_DIR.glob("*.md")):
        if md.name not in NON_POST_FILES:
            posts.append((md, False))
    for phase_dir in sorted(STUDY_DIR.glob("phase-*")):
        for note in sorted(phase_dir.glob("*.md")):
            posts.append((note, True))
    return posts


def collect_seo_issues() -> list[str]:
    """Frontmatter problems that would silently degrade search exposure."""
    issues: list[str] = []
    for note, is_lesson in iter_posts():
        rel = note.relative_to(ROOT).as_posix()
        fm = parse_frontmatter(note.read_text(encoding="utf-8"))
        if fm is None:
            issues.append(f"{rel}: no frontmatter")
            continue
        required = REQUIRED_FM + (LESSON_ONLY_FM if is_lesson else ())
        for field in required:
            if not fm.get(field):
                issues.append(f"{rel}: missing '{field}'")
        title = str(fm.get("title", ""))
        if len(title) > TITLE_MAX:
            issues.append(f"{rel}: title {len(title)} chars (max {TITLE_MAX})")
        desc = str(fm.get("description", ""))
        if desc and not (DESC_MIN <= len(desc) <= DESC_MAX):
            issues.append(
                f"{rel}: description {len(desc)} chars (want {DESC_MIN}-{DESC_MAX})"
            )
        tags = fm.get("tags") or []
        if not isinstance(tags, list) or not (TAGS_MIN <= len(tags) <= TAGS_MAX):
            issues.append(
                f"{rel}: {len(tags) if isinstance(tags, list) else 0} tags "
                f"(want {TAGS_MIN}-{TAGS_MAX})"
            )
        elif "AI엔지니어링" not in tags:
            issues.append(f"{rel}: tags missing the series tag 'AI엔지니어링'")
        kws = fm.get("keywords") or []
        if not isinstance(kws, list) or len(kws) < KEYWORDS_MIN:
            issues.append(
                f"{rel}: {len(kws) if isinstance(kws, list) else 0} keywords "
                f"(want >= {KEYWORDS_MIN})"
            )
    return issues


def build(catalog: dict, notes: dict[int, set[str]]) -> tuple[list[PhaseProgress], list[str]]:
    phases: list[PhaseProgress] = []
    matched: dict[int, set[str]] = {}

    for p in catalog["phases"]:
        pp = PhaseProgress(
            num=p["num"],
            slug=p["slug"],
            title=p["title"],
            total=p["lesson_count"],
            lessons=p["lessons"],
        )
        have = notes.get(p["num"], set())
        for lesson in p["lessons"]:
            if lesson["slug"] in have:
                pp.done_slugs.add(lesson["slug"])
                matched.setdefault(p["num"], set()).add(lesson["slug"])
        phases.append(pp)

    orphans = []
    for phase_num, slugs in notes.items():
        for slug in sorted(slugs - matched.get(phase_num, set())):
            orphans.append(f"study/phase-{phase_num:02d}/{slug}.md")
    return phases, sorted(orphans)


def next_lesson(phases: list[PhaseProgress]) -> dict | None:
    """First lesson, in curriculum order, without a note."""
    for pp in phases:
        for lesson in pp.lessons:
            if lesson["slug"] not in pp.done_slugs:
                return {
                    "phase": pp.num,
                    "phase_title": pp.title,
                    "num": lesson["num"],
                    "slug": lesson["slug"],
                    "title": lesson["title"],
                    "path": lesson["path"],
                    "note_path": f"study/phase-{pp.num:02d}/{lesson['slug']}.md",
                }
    return None


def render_text(
    phases: list[PhaseProgress],
    orphans: list[str],
    only: int | None,
    seo: list[str] | None = None,
) -> str:
    done = sum(p.done for p in phases)
    total = sum(p.total for p in phases)
    out: list[str] = []

    if only is None:
        pct = 100.0 * done / total if total else 0.0
        out.append("")
        out.append(f"  study progress: {done}/{total} lessons ({pct:.1f}%)")
        out.append("")
        for pp in phases:
            mark = "*" if 0 < pp.done < pp.total else (" " if pp.done == 0 else "+")
            out.append(
                f"  {mark} P{pp.num:02d} {pp.bar()} {pp.done:>3}/{pp.total:<3} {pp.title}"
            )
    else:
        pp = next((p for p in phases if p.num == only), None)
        if pp is None:
            out.append(f"  no such phase: {only}")
            return "\n".join(out) + "\n"
        out.append("")
        out.append(f"  Phase {pp.num:02d} - {pp.title}   {pp.done}/{pp.total} ({pp.pct:.0f}%)")
        out.append("")
        for lesson in pp.lessons:
            mark = "[x]" if lesson["slug"] in pp.done_slugs else "[ ]"
            out.append(f"  {mark} {lesson['num']:>2}. {lesson['title']}")

    nxt = next_lesson(phases)
    out.append("")
    if nxt:
        out.append(f"  next: P{nxt['phase']:02d} L{nxt['num']:02d} {nxt['title']}")
        out.append(f"        {nxt['path']}")
    else:
        out.append("  all lessons have notes.")

    if orphans:
        out.append("")
        out.append("  orphan notes (no matching lesson - check the filename):")
        for o in orphans:
            out.append(f"    ! {o}")

    if seo:
        out.append("")
        out.append("  SEO frontmatter issues:")
        for s in seo:
            out.append(f"    ! {s}")

    out.append("")
    return "\n".join(out) + "\n"


def render_markdown(phases: list[PhaseProgress], orphans: list[str]) -> str:
    done = sum(p.done for p in phases)
    total = sum(p.total for p in phases)
    pct = 100.0 * done / total if total else 0.0

    lines = [
        "# 학습 진행 상태",
        "",
        "> 이 파일은 `python scripts/study_progress.py --write`로 생성됩니다.",
        "> 직접 고치지 마세요. `study/`의 노트 파일이 유일한 진실원입니다.",
        "",
        f"**{done} / {total} 레슨 ({pct:.1f}%)**",
        "",
        "| Phase | 진행 | 완료 | 주제 |",
        "|---|---|---|---|",
    ]
    for pp in phases:
        lines.append(
            f"| {pp.num:02d} | `{pp.bar(16)}` | {pp.done}/{pp.total} | {pp.title} |"
        )

    nxt = next_lesson(phases)
    lines += ["", "## 다음 레슨", ""]
    if nxt:
        lines += [
            f"**Phase {nxt['phase']:02d} · Lesson {nxt['num']:02d} — {nxt['title']}**",
            "",
            f"- 원문: [`{nxt['path']}`](../{nxt['path']}/docs/en.md)",
            f"- 노트 예정 위치: `{nxt['note_path']}`",
        ]
    else:
        lines.append("모든 레슨에 노트가 있습니다.")

    for pp in phases:
        if pp.done == 0:
            continue
        lines += ["", f"## Phase {pp.num:02d} — {pp.title}", ""]
        for lesson in pp.lessons:
            if lesson["slug"] in pp.done_slugs:
                rel = f"phase-{pp.num:02d}/{lesson['slug']}.md"
                lines.append(f"- [x] {lesson['num']:02d}. [{lesson['title']}]({rel})")
            else:
                lines.append(f"- [ ] {lesson['num']:02d}. {lesson['title']}")

    if orphans:
        lines += ["", "## 짝 없는 노트", "", "파일명이 레슨 슬러그와 맞지 않습니다.", ""]
        lines += [f"- `{o}`" for o in orphans]

    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--phase", type=int, help="show one phase, lesson by lesson")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--write", action="store_true", help="regenerate study/PROGRESS.md")
    parser.add_argument(
        "--strict", action="store_true", help="exit 1 if orphan notes or SEO issues exist"
    )
    args = parser.parse_args(argv)

    phases, orphans = build(load_catalog(), collect_notes())
    seo = collect_seo_issues()

    if args.json:
        payload = {
            "done": sum(p.done for p in phases),
            "total": sum(p.total for p in phases),
            "seo_issues": seo,
            "phases": [
                {
                    "num": p.num,
                    "title": p.title,
                    "done": p.done,
                    "total": p.total,
                    "done_slugs": sorted(p.done_slugs),
                }
                for p in phases
            ],
            "next": next_lesson(phases),
            "orphans": orphans,
        }
        sys.stdout.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    else:
        sys.stdout.write(render_text(phases, orphans, args.phase, seo))

    if args.write:
        STUDY_DIR.mkdir(exist_ok=True)
        PROGRESS_MD.write_text(render_markdown(phases, orphans), encoding="utf-8")
        if not args.json:
            sys.stdout.write(f"  wrote {PROGRESS_MD.relative_to(ROOT).as_posix()}\n\n")

    return 1 if (args.strict and (orphans or seo)) else 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    sys.exit(main(sys.argv[1:]))
