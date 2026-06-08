---
name: "spec-executor"
description: "Executes spec-driven tasks from requirements, design, and tasks docs. Invoke when user asks to implement an existing spec."
---

# Spec Executor

## Purpose

Execute an existing spec-driven plan safely and traceably. Use this skill when the user asks to implement, continue, or verify work from a spec folder such as `docs/specs-v2/YYYY-MM-DD-<slug>/` or another user-provided spec directory.

This skill treats spec files as the source of truth:

```text
requirements.md or bugfix.md
        ↓
design.md
        ↓
tasks.md
        ↓
implementation task loop
        ↓
lint / typecheck / tests
        ↓
traceability report
```

The executor must not improvise beyond the spec. If implementation requires behavior, files, or product decisions not covered by the spec, stop and ask for clarification.

## When to Invoke

Invoke this skill when the user asks to:

- Implement a spec-driven plan
- Execute tasks from a spec folder
- Continue a partially completed spec
- Verify a completed spec implementation
- Build from `requirements.md`, `bugfix.md`, `design.md`, and `tasks.md`
- Convert spec tasks into working code

Do not invoke this skill to generate new specs from scratch. Use `spec-generator` for that.

## Core Execution Principles

- Spec is source of truth
- Requirements define behavior
- Design defines architecture and constraints
- Tasks define execution order
- Implement one task at a time
- Keep task scope narrow
- Preserve explicitly listed unchanged behavior
- Run verification after meaningful changes
- Do not commit unless the user explicitly asks
- Do not widen scope without asking

## General Project Alignment

Every implementation should enforce common production-quality rules:

- Deterministic workflows over hidden inference
- Human approval for approval workflows and AI output persistence when applicable
- Visible ownership for important decisions
- Immutable audit logs for meaningful state changes where auditability is required
- API boundary enforces authorization when authorization is involved
- Frontend reflects backend state where backend state is the source of truth
- No hidden automation
- No business logic in controllers or UI
- Schema first when backend data changes are involved
- Backend layering such as Controller → Service → Repository when the architecture uses layered boundaries

If a spec conflicts with project rules, stop and report the conflict before implementation.

## Required Inputs

The executor needs a spec folder, normally:

```text
docs/specs-v2/YYYY-MM-DD-<slug>/
```

Slug format is mandatory for default spec folders: `YYYY-MM-DD-<slug>`, where the date is the local creation date and `<slug>` is lowercase kebab-case.

A different user-provided spec folder is also valid if it contains equivalent files.

Expected files for a feature spec:

```text
requirements.md
design.md
tasks.md
.config
```

Expected files for a bugfix spec:

```text
bugfix.md
design.md
tasks.md
.config
```

If required files are missing, ask whether to generate or repair the spec before implementation.

---

# Execution Workflow

## Step 1: Load and Understand the Spec

Read in this order:

1. `AGENTS.md`
2. `DESIGN.md` when frontend, UI, or interaction behavior is involved
3. Relevant workspace architecture or conventions rules when available
4. `.config`, if present
5. `requirements.md` or `bugfix.md`
6. `design.md`
7. `tasks.md`
8. Every file in scope for the active task before editing

Extract:

- Spec type: feature, bugfix, UI enhancement, backend workflow, refactor
- Actors and roles
- Ownership rules
- State transitions
- Authorization rules
- Audit obligations
- AI involvement and human-review gates
- API contracts
- Data model changes
- Explicit preserved behavior
- Correctness properties
- Task dependency graph

Before coding, state a concise context-loaded summary that confirms:

- spec folder loaded
- active task identified
- files in scope identified
- any Goverone-sensitive flags such as approval, RBAC, audit logging, or AI review

Do not start coding before this extraction is clear.

## Step 2: Build an Execution Todo List

Convert `tasks.md` into an active task list.

Use one active task at a time.

For each task, follow this loop:

1. Mark the current task in progress
2. Confirm files in scope
3. Read all in-scope files before editing
4. State a concise implementation plan for the active task
5. Implement only that task
6. Run self-review and verification
7. Mark only that task complete in `tasks.md`
8. Report task outcome before moving to the next task

Mark a task complete only after:

- Code changes are done
- Relevant tests pass or verification is complete
- Requirement references are satisfied
- No unresolved errors remain
- Self-review checks pass

If a task is too large, split it into smaller execution steps while preserving its requirement references.

## Step 3: Scope Gate

Before editing, identify files in scope from `tasks.md` and `design.md`.

If a task requires touching a file not listed in the spec:

1. Stop
2. Explain why the file is needed
3. Ask whether to expand scope

Exception: reading additional files for context is allowed.

## Step 4: Branch Gate

Before implementation, check branch requirements if the local process requires them.

If the spec or project rules require a fresh branch, confirm:

- Active branch is not `main`
- Branch name matches the feature or fix slug
- Branch is dedicated to the implementation scope

If branch creation is required and not satisfied, ask or create only if the user explicitly allowed branch management.

## Step 5: Implementation Order

When backend state, data, authorization, approval, or audit behavior is involved, follow this order:

1. Schema
2. Migration
3. Validation schemas
4. Repository/data access
5. Service layer business rules
6. Authorization guards at API boundary
7. Controller/API routes, thin only
8. Audit logging integrated with state changes
9. Frontend query/state awareness
10. Frontend forms and explicit confirmations
11. Frontend error, loading, empty, and unauthorized states
12. Tests and verification

For UI-only specs, follow the design component hierarchy and preserve existing API contracts.

For bugfix specs, follow the bugfix loop:

```text
1. Write or run bug-condition test that should fail on unfixed code
2. Write or run preservation tests that should pass on unfixed code
3. Implement the smallest targeted fix
4. Re-run the same bug-condition test and confirm it passes
5. Re-run preservation tests and confirm they still pass
6. Run final verification
```

If tests already exist in the spec, use those. Do not replace them with easier tests.

## Step 6: Implementation Rules by Layer

### TypeScript

- Never use `any`
- Keep public function signatures explicit when project conventions require it
- Follow existing import and typing conventions in nearby files
- Do not use unsafe casts to bypass type safety

### Schema and Database

- Schema changes come before API/controller work
- Approvable entities should include `status`, `approvedBy`, and `approvedAt` when approval workflows are involved
- Ownership fields such as `createdBy` should be preserved where relevant
- Use strong foreign keys where possible
- Prefer soft delete unless the spec explicitly permits hard deletion
- Generate and apply migrations using project-defined commands only

### Service Layer

- Business logic belongs here
- State transitions must be validated here
- Approval rules must be explicit
- Ownership must be assigned visibly
- Audit log writes must be part of meaningful state changes when auditability is required
- Reject invalid transitions deterministically

### Controller/API Layer

- Controllers are thin
- Validate input at the boundary, usually with schema validation
- Enforce authorization at the API boundary when authorization is involved
- Never trust frontend role claims
- Return explicit error codes and messages
- Do not move business logic into controllers

### Frontend

- Reflect backend state when backend state is authoritative
- Do not independently determine authorization when authorization is backend-owned
- Render actions from backend-provided state or permissions where available
- Use existing components before creating new ones
- Use existing form and validation conventions
- Use existing data-fetching conventions
- Show explicit confirmations for approvals and destructive actions
- Cover loading, empty, success, validation error, API error, and unauthorized states when the UI changes require them
- No auto-retry for approval/rejection failures

### Audit Logging

When auditability is required, every meaningful state change should log:

- actor ID
- actor role
- action
- entity type
- entity ID
- timestamp

If the spec requires stricter audit behavior, follow the spec.

Failure to log a required state change means the task is incomplete.

---

# Template Analysis Reference for Execution

## Feature Specs

Feature specs are structured as:

```text
Introduction
Glossary
Requirements
  Requirement N
    User Story
    Acceptance Criteria
```

Acceptance criteria use:

- `WHEN [condition], THE [component] SHALL [behavior]`
- `IF [condition], THEN THE [component] SHALL [behavior]`
- `WHILE [state], THE [component] SHALL [behavior]`

During execution, every implemented behavior must trace back to one or more acceptance criteria.

## Bugfix Specs

Bugfix specs are structured as:

```text
Current Behavior (Defect)
Expected Behavior (Correct)
Unchanged Behavior (Regression Prevention)
Formal Bug Condition
Fix Checking Property
Preservation Goal
```

During execution:

- Fix only the bug condition
- Preserve all non-bug behavior
- Use unchanged behavior as regression test scope
- Prefer smallest targeted fix

## Design Specs

Design specs commonly include:

- Overview
- Key Design Decisions
- Architecture
- Components and Interfaces
- Data Models
- State Machine
- API Contracts
- Correctness Properties
- Error Handling
- Testing Strategy

During execution:

- Follow key design decisions unless they conflict with code reality or project rules
- Treat correctness properties as invariants
- Use API contracts and data models to guide code shape
- Use error handling tables for response behavior
- Use testing strategy to decide what to run or write

## Task Specs

Task specs commonly include:

- Numbered task groups
- Subtasks with requirement references
- Optional property tests marked with `*`
- Checkpoints
- Dependency graph
- Notes

During execution:

- Respect dependency graph
- Complete checkpoints before moving to later waves
- Do not skip required tasks
- Optional tasks may be skipped only if the user or spec allows it
- Preserve requirement references in progress summaries

Task markers:

| Marker | Meaning |
|---|---|
| `[ ]` | Required pending |
| `[~]` | In progress or generated target task |
| `[x]` | Completed |
| `[ ]*` | Optional task |
| `[-]` | Blocked or deferred |

---

# Verification Workflow

## Before Coding

- Read relevant source files
- Identify existing conventions
- Check dependencies before using libraries
- Understand test commands from package scripts or existing docs
- For non-trivial bugfixes, confirm failing behavior if feasible

## During Coding

- Keep changes scoped to the active task
- Update task progress immediately after completion
- Run focused tests when available
- Run type diagnostics when useful
- Stop on ambiguous product behavior

## After Coding

Run verification appropriate to the project and changes:

1. Relevant unit tests
2. Relevant integration tests
3. Typecheck
4. Lint
5. Build, if the change affects build output or packaging

If commands are not known, inspect project scripts. If still unknown, ask the user for the correct commands.

## Self-Review Before Marking a Task Complete

Before declaring a task complete, confirm all applicable checks pass:

### Correctness

- Every relevant acceptance criterion or bugfix condition for the active task is satisfied
- Allowed state transitions work and forbidden ones are rejected where applicable
- RBAC is enforced at the API boundary where applicable
- Audit logging is present for required state changes
- No behavior outside the spec was introduced

### Code Quality

- No `any` introduced
- No dead code or commented-out code left behind
- No business logic moved into controllers or UI
- No unsafe shortcut that reduces audit clarity

### Scope

- Only files declared or clearly justified by the spec were changed
- Any newly required file outside the original task scope was explicitly surfaced before editing

### Verification

- Relevant tests pass
- Typecheck passes when applicable
- Lint passes when applicable
- Build passes when applicable
- No unresolved errors remain

If the same blocker persists after two focused fix attempts, stop and report:

- exact error
- what was tried
- current hypothesis
- what clarification or permission is needed

## Task Progress Update

After self-review and verification pass:

1. Read `tasks.md`
2. Mark only the current task complete
3. Preserve every other task state unchanged
4. Report that the task was updated in `tasks.md`

## Final Traceability Report

After each completed task, report:

- task completed
- files changed
- requirements or bugfix properties satisfied
- verification run and results
- Goverone-sensitive checks such as audit logging, RBAC, approval UI, or AI review
- out-of-scope observations
- assumptions made
- next task, if any

When the full spec is complete, include:

- spec folder executed
- tasks completed
- major files changed
- tests and verification run and results
- any skipped optional tasks
- any open questions or follow-up risks
- readiness for human review

Use concise but explicit reporting.

---

# Stop Conditions

Stop and ask for clarification if:

- Requirements conflict with design
- Tasks conflict with project rules
- A required file is missing
- Implementation needs broader scope than declared
- User-facing behavior would change beyond the spec
- Approval, ownership, authorization, or audit behavior is ambiguous
- A tempting shortcut would reduce audit clarity where auditability is required
- Tests reveal the spec assumption is false

Do not silently choose a path in these cases.

---

# Execution Checklist

Before implementation:

- [ ] Spec folder identified
- [ ] Requirements or bugfix spec read
- [ ] Design read
- [ ] Tasks read
- [ ] Todo list created from tasks
- [ ] Scope understood
- [ ] Open questions resolved or explicitly accepted

For each task:

- [ ] Task marked in progress
- [ ] Files in scope identified
- [ ] Existing code conventions reviewed
- [ ] Active task plan stated
- [ ] Code implemented
- [ ] Self-review completed
- [ ] Focused verification run
- [ ] Task updated in `tasks.md`
- [ ] Task marked complete

Final:

- [ ] Required tests run
- [ ] Lint run if available
- [ ] Typecheck run if available
- [ ] Build run if appropriate
- [ ] Traceability report provided
- [ ] Ready for human review reported
