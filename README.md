# Agent Skills

This repository contains a personal collection of Codex agent skills used to standardize planning, execution, QA, and session management workflows.

## What's in this repo

The skills live under [`personal/`](/Users/indranugraha/Documents/Codex/2026-06-08/please-check-codes-skills-personal/personal):

- `commit-session` - reviews current session changes, helps prepare branch and commit flow
- `create-plan` - writes structured execution plans as Markdown artifacts
- `quality-assurance` - builds QA plans and QA reports against approved specs
- `spec-executor` - implements work from an existing spec folder
- `spec-generator` - generates requirements, design, and task documents for new work

## Repository structure

```text
personal/
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

These folders follow the standard Codex skill layout:

1. Put the skill folder in your Codex skills directory, or keep this repo as a source-of-truth repo and sync from it.
2. Reference the skill by name in a request when the task matches its purpose.
3. Codex will open the skill's `SKILL.md` and follow the workflow described there.

Examples:

- "Use `spec-generator` to create a spec for this feature"
- "Use `spec-executor` to implement the approved spec"
- "Use `quality-assurance` to validate this completed spec"
- "Use `create-plan` to break this project into tasks"
- "Use `commit-session` to review and commit my current changes"

## Notes

- `spec-generator` includes reusable templates under `personal/spec-generator/templates/`.
- Each skill is plain Markdown, so it can be reviewed and edited easily.
- This repo is intended to version the skill definitions themselves, not the output artifacts they generate.
