---
name: "commit-session"
description: "Checks current session code changes, provides commit messages, and creates branches following Goverone commit rules. Invoke when user asks to review, commit, or manage session code changes."
---

# Commit Session

Checks current session code changes, provides structured commit messages, creates feature branches, and commits following the repository's commit and branch rules.

## Purpose

- Verify current git status and session code changes
- Create appropriate feature branches if needed
- Generate conventional commit messages following Goverone guidelines
- Ensure all changes are properly committed with proper documentation

## When to Use

- User requests to check current session changes
- User wants to commit code changes
- User needs to create a new branch for work
- Before ending a session or task
- When switching between different tasks/features

## Step 1 — Current State Check

Check the current git status:

```bash
git status
git diff --stat
git branch
```

Verify:
- Current branch state
- Modified files
- Untracked files
- Staged vs unstaged changes

## Step 2 — Branch Management

### If no branch exists or branch needs creation:

```bash
git checkout -b <branch-name>
```

Branch naming convention:
- `feat/<domain>-<feature>`
- `fix/<domain>-<bug>`
- `refactor/<domain>-<area>`

Examples:
- `feat/risk-control-approval`
- `fix/client-workspace-transition`
- `refactor/api-controllers`

### Verify branch state:
- Confirm branch is dedicated to current task
- Ensure branch name matches implementation scope
- Check for any leftover changes from previous tasks

## Step 3 — Change Analysis

Review all changed files:
- Add new files: `git add <file>`
- Stage modified files: `git add <file>`
- Review staged changes: `git diff --staged`

For each changed file, document:
- What was changed
- Why it was changed
- Domain area affected
- Goverone compliance (if applicable)

## Step 4 — Commit Message Generation

Follow conventional commit format:

```
<type>(<scope>): <description under 60 chars>

- What was implemented (bullet per meaningful unit)
- Key decisions made (especially anything that deviated from spec — with reason)
- Goverone: audit log written for [action] on [entityType]
- Requirements addressed: [IDs from requirements.md]
```

### Commit Types
- `feat` — New feature
- `fix` — Bug fix
- `refactor` — Code refactoring
- `test` — Test additions/changes
- `chore` — Maintenance tasks
- `docs` — Documentation

### Commit Scopes
Domain areas touched:
- `risk-control`, `api/scope`, `audit-log`, `client-workspace`, `document`, `auth`, `ui`, `infra`

## Step 5 — Commit Execution

After staging changes and generating commit message:

```bash
git commit -m "commit-message-here"
```

## Step 6 — Task Completion Report

Provide a completion report in this format:

```
---
✅ Changes committed

Branch:
- [branch-name] — BRANCH-START-001 satisfied

Files changed:
- [file path] — [what changed in one line]
  ... (repeat for all files)

Checks:
- typecheck: ✅ clean / ⚠️ needs run
- lint: ✅ clean / ⚠️ needs run
- tests: ✅ [N] passing / ⚠️ needs run

Goverone compliance:
- Audit log: ✅ written for [action] on [entityType] / ⚠️ N/A for this change
- RBAC guard: ✅ enforced at [route] / ⚠️ N/A for this change
- Forbidden patterns: ✅ none introduced

Notes:
- [Any important context about this commit]
---
```

## Step 7 — Quality Checks (Optional but Recommended)

If user requests verification or if it's a critical change:

```bash
bun run typecheck
bun run lint
bun run test
```

Check for:
- TypeScript errors
- Linting issues
- Test failures
- Goverone compliance violations

## Example Workflow

1. User asks: "Check my changes and commit them"
2. Run `git status` and `git diff --stat`
3. Analyze changes and determine commit type/scope
4. Create branch if needed: `git checkout -b feat/user-auth-flow`
5. Stage all changes: `git add .`
6. Generate commit message following format
7. Commit: `git commit -m "feat(auth): add user authentication flow"`
8. Provide completion report with file changes

## Important Notes

- Always verify branch state before committing
- Follow conventional commit format strictly
- Document all meaningful changes
- Check Goverone compliance for domain-related changes
- Provide clear context in commit messages
- Don't bundle unrelated changes in one commit
