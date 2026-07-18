# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A curriculum, not an application. 20 phases / 435 lesson directories under `phases/`,
each shipping runnable code plus a reusable artifact (prompt, skill, agent, MCP server).
There is no app to build or test suite to run — "verification" here means the invariant
scripts in `scripts/` pass and generated files are not stale.

## Commands

These are written for this machine (Windows): `python`, not `python3` — see the traps below.
Upstream docs and CI use `python3`; on Linux/macOS substitute it back.

```bash
PYTHONIOENCODING=utf-8 python scripts/audit_lessons.py   # lesson invariants L001–L010 (CI gate)
PYTHONIOENCODING=utf-8 python scripts/audit_lessons.py --phase 14   # --json, --strict too
PYTHONIOENCODING=utf-8 python scripts/build_catalog.py   # rewrite catalog.json (CI drift gate)
PYTHONIOENCODING=utf-8 python scripts/check_readme_counts.py   # README counts vs catalog; --fix rewrites
PYTHONIOENCODING=utf-8 python scripts/lesson_run.py      # byte-compile lesson .py; --execute to run
PYTHONIOENCODING=utf-8 python scripts/link_check.py --strict   # external links; caches 7d
python scripts/install_skills.py <target>   # export lesson outputs as skills/prompts/agents
node site/build.js                          # regenerate site/data.js from README/ROADMAP/glossary
scripts/scaffold-lesson.sh <phase-dir> <NN-slug> ["Title"]   # new lesson skeleton (bash)

python scripts/study_progress.py            # study-note progress + SEO frontmatter check
python scripts/study_progress.py --phase 0  # one phase, lesson by lesson
python scripts/study_progress.py --write    # regenerate study/PROGRESS.md
python scripts/study_progress.py --strict   # exit 1 on orphan notes or SEO issues
```

`study_progress.py` reconfigures its own stdout, so it needs no `PYTHONIOENCODING`.

All Python scripts are stdlib-only, Python 3.10+. `.github/workflows/curriculum.yml` runs
audit + catalog drift + README counts on any push touching `phases/`, `catalog.json`, or `README.md`.

**On Windows, two traps:**

1. The console is cp949, so `audit_lessons.py` and friends crash with `UnicodeEncodeError`
   on em-dashes. Prefix with `PYTHONIOENCODING=utf-8`.
2. **Never use `python3`.** It resolves to the Microsoft Store app-execution alias, which
   prints `Python`, runs nothing, and **exits 0** — so a gate appears to pass when it never
   ran. Use `python`. Verified: `python3 scripts/audit_lessons.py` → `Python`, exit 0.

## The two sources of truth

This is the thing to internalize before editing anything:

1. **The filesystem** (`phases/NN-slug/MM-slug/`) is truth for what exists.
   `scripts/build_catalog.py` walks it and emits `catalog.json`. CI rebuilds and diffs —
   **add or rename a lesson directory and you must re-run it and commit `catalog.json`.**
2. **`README.md` + `ROADMAP.md` + `glossary/terms.md`** are truth for the website.
   `site/build.js` parses them into `site/data.js` (generated but committed).

They are checked against each other only loosely: `check_readme_counts.py` pins a handful of
hardcoded README counts (badges, prose totals) to `catalog.json` `totals`. The per-lesson tables
are *not* reconciled — `site/build.js` currently parses 430 lessons out of the README while the
filesystem holds 435. Adding a lesson directory therefore means editing README/ROADMAP tables by
hand too; nothing will fail CI if you forget.

### Parser-fragile formats

`site/build.js` keys off exact characters. Do not "clean up" these:

- Phase headers: `### Phase N: Name \`X lessons\`` **or** the `<details><summary><b>Phase N — Name</b> … <code>X lessons</code> … <em>Description</em></summary>` form.
- Lesson tables: `| # | Lesson | Type | Lang |` (capstones use `| # | Project | Combines | Lang |`). The `Lang` column takes plain text or legacy emoji flags (🐍 🟦 🦀 🟣 ⚛️) — equivalent to the parser.
- ROADMAP status glyphs `✅` / `🚧` / `⬚` on phase headers and lesson rows. Never replace with text.

After touching those files run `node site/build.js`; `git diff site/data.js` should show only
the `Last built:` timestamp line if your edit was structure-safe.

## Lesson anatomy

```
phases/NN-phase-slug/MM-lesson-slug/
├── code/          at least one runnable file (required if the dir exists)
├── notebook/      optional
├── docs/en.md     required — H1, ≥200 bytes; translations are zh.md, ja.md, …
├── outputs/       {skill,prompt,agent}-*.md with YAML frontmatter
├── quiz.json      optional
└── mission.md     optional — first line becomes a "mission" artifact
```

Directory names must match `NN-lowercase-kebab` (both phase and lesson). `audit_lessons.py`
enforces: L001 dir pattern, L002–L004 `docs/en.md` present/UTF-8/≥200B/has H1, L005 `code/`
non-empty, L006–L009 quiz schema, L010 internal markdown links resolve.

`outputs/` frontmatter drives both `site/build.js` artifact discovery and
`install_skills.py`, so `name` / `description` / `phase` / `lesson` / `tags` must be present.
The filename stem must start with `skill-`, `prompt-`, or `agent-` or it is silently ignored.

### quiz.json

Array of questions, or `{"questions": [...]}`. Canonical keys — `stage`, `question`,
`options`, `correct`, `explanation`. `correct` is a 0-based index into `options`;
`options` must have 2–6 entries. The legacy `q`/`choices`/`answer` keys fail audit rule L007.

`stage` is `pre` | `check` | `post`; `site/lesson.html` renders them as Pre-Lesson Check,
Mid-Lesson Check (between Build It and Use It), and Post-Lesson Quiz respectively.
The site fetches `quiz.json` from raw.githubusercontent on `main`, so quiz changes only
appear live after merge.

## Writing conventions

From `CONTRIBUTING.md` / `LESSON_TEMPLATE.md` — these are enforced by review, not tooling:

- **No comments in code.** Explanation belongs in `docs/en.md`.
- **Build from scratch first, framework second.** The doc section order is fixed:
  The Problem → The Concept → Build It → Use It → Ship It → Exercises (then optional
  Key Terms / Further Reading).
- Code must run as-is with the dependencies the lesson lists. `requirements.txt` at the
  root is the aggregate; heavy lessons declare deps via a `# requires: pkg1, pkg2` first-line
  comment, which `lesson_run.py --execute` uses to skip them.
- Pick the language that fits the topic (Python / TypeScript / Rust / Julia), don't force Python.
- Direct prose, no filler, no decorative emoji in headings (the `Lang` column flags are the
  one exception, and only because the parser maps them).
- One contribution per pull request.

## Korean study notes (`study/`)

This fork carries a Korean learning layer that upstream does not have. `study/phase-NN/MM-slug.md`
holds a natural-Korean rendering of a lesson plus verified environment gotchas — it is *not* a
translation, so it deliberately does not live in the `docs/ko.md` slot (that slot is upstream's
translation contract). See `study/README.md` for the note structure and `study/glossary-ko.md`
for the fixed Korean term spellings.

**Progress is derived, never hand-maintained.** A note file existing means that lesson is done;
`scripts/study_progress.py` matches notes against `catalog.json` by phase number + lesson slug.
Run it at the start of a study session to see where things stand and what's next. A note whose
filename doesn't match a lesson slug is reported as an orphan rather than silently not counting.
`study/PROGRESS.md` is generated output — never edit it by hand.

Nothing under `study/` affects CI: `build_catalog.py`, `audit_lessons.py`, and `site/build.js`
all read only `phases/**/docs/en.md`.

## Atlas tracking (`.atlas/`, gitignored)

This repo is registered in Atlas as project **36** ("AI Engineering from Scratch"), with one
WBS item per phase (ids 621–640, `phase-00`…`phase-19`). `study_progress.py` stays the
fine-grained truth; Atlas is the coarse, cross-project view.

**Do not call `atlas-cli` inline for routine tracking.** Append one JSON line per event to
`.atlas/ledger.jsonl`; a Stop/SessionEnd hook flushes it out of the model loop, so it costs
no tokens. Event shapes (`t` = type):

```jsonc
{"t":"start","slug":"phase-01","title":"Phase 01 - Math Foundations","start":"2026-07-20"}
{"t":"done","slug":"phase-00","title":"Phase 00 - Setup And Tooling","completed":"2026-07-25"}
{"t":"changelog","slug":"phase-00","contentFile":"study/phase-00/00-summary.md","impact":"Medium"}
```

**Log at phase boundaries only, never per lesson.** `study_progress.py` is the fine-grained
truth; 435 per-lesson changelogs would destroy the coarse view Atlas exists to give.

`slug` must be `phase-NN`. `.atlas/wbs-map.json` maps those to existing WBS ids, so a mapped
slug **updates** its item and never creates a duplicate. `.atlas/project.json` pins project 36
— it is required, because the hook's fallback resolves projects by repo folder name
(`ai-engineering-from-scratch`), which does not match the Atlas project name.

Check `.atlas/errors.log` and `.atlas/needs-confirm` if events seem not to land. Meetings are
deferred to the interactive `/atlas-meeting`; use `/atlas-log` for a full completed-work write-up.

## Skills

`.claude/skills/` ships two course-facing skills: `find-your-level` (placement across the
20 phases) and `check-understanding` (phase quiz driven by lesson `quiz.json` files).
Note the repo's own `.gitignore` lists `.claude/`, so local harness edits there stay untracked.
