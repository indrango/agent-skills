# Agent Skills

This repository contains a personal collection of TRAE (Codex) agent skills used to standardize planning, execution, QA, browser testing, and session management workflows.

## What's in this repo

The skills live under [`personal/`](personal/):

| Skill | Description |
|---|---|
| `browser-quality-plan` | Generates approval-ready browser QA execution plans before headed browser testing |
| `browser-quality-check` | Executes approved browser QA plans in a headed browser with evidence-backed reports |
| `markdown-to-pdf-generator` | Converts Markdown documents into styled PDF files using the shared Python converter |
| `commit-session` | Reviews current session changes, helps prepare branch and commit flow |
| `create-plan` | Writes structured execution plans as Markdown artifacts |
| `quality-assurance` | Builds QA plans and QA reports against approved specs |
| `spec-executor` | Implements work from an existing spec folder |
| `spec-generator` | Generates requirements, design, and task documents for new work |

## Repository structure

```text
personal/
  browser-quality-check/
    SKILL.md
    report-template.md
  browser-quality-plan/
    SKILL.md
    plan-template.md
  markdown-to-pdf-generator/
    SKILL.md
    generate-pdf.py
  commit-session/
    SKILL.md
  create-plan/
    SKILL.md
  quality-assurance/
    SKILL.md
  spec-executor/
    SKILL.md
  spec-generator/
    SKILL.md
    templates/
      bugfix.md
      design.md
      requirements.md
      tasks.md
```

## How to use

These folders follow the standard TRAE skill layout:

1. Put the skill folder in your TRAE skills directory, or keep this repo as a source-of-truth repo and sync from it.
2. Reference the skill by name in a request when the task matches its purpose.
3. TRAE will open the skill's `SKILL.md` and follow the workflow described there.

Examples:

- "Use `browser-quality-plan` to plan QA for this page"
- "Use `browser-quality-check` to run the approved QA plan"
- "Use `markdown-to-pdf-generator` to export this Markdown file as PDF"
- "Use `spec-generator` to create a spec for this feature"
- "Use `spec-executor` to implement the approved spec"
- "Use `quality-assurance` to validate this completed spec"
- "Use `create-plan` to break this project into tasks"
- "Use `commit-session` to review and commit my current changes"

## Notes

- `browser-quality-check` includes `report-template.md` for evidence-backed QA reports.
- `browser-quality-plan` includes `plan-template.md` for structured QA planning.
- `markdown-to-pdf-generator` includes `generate-pdf.py` for styled Markdown-to-PDF conversion with WeasyPrint.
- `spec-generator` includes reusable templates under `personal/spec-generator/templates/`.
- Each skill is plain Markdown, so it can be reviewed and edited easily.
- This repo is intended to version the skill definitions themselves, not the output artifacts they generate.
