---
name: "create-plan"
description: "Creates structured execution plans as timestamped Markdown files. Invoke when user asks to create a plan, implementation plan, rollout plan, migration plan, or any actionable task breakdown."
---

# Create Plan

Creates a structured, trackable execution plan as a Markdown file. Plans are the single source of truth for task breakdowns, decisions, and progress tracking.

## When to Invoke

- User asks to create a plan (implementation, rollout, migration, launch checklist, etc.)
- User asks for an actionable breakdown of work into tasks
- User says "make a plan", "create a plan", "break this down into tasks"

## Required Inputs

Collect from the user or infer from context:

1. **Plan topic** — what the plan covers (e.g., "auth-migration", "mvp-launch-checklist")
2. **Scope context** — PRD reference, feature description, or task summary
3. **Constraints** (optional) — deadlines, dependencies, team assignments
4. **Actor / owner context** — who initiates or owns the workflow outcome
5. **Affected surfaces** — backend, frontend, schema, shared contracts, integrations
6. **State or approval implications** — relevant transitions, forbidden transitions, audit impacts
7. **Acceptance constraints** — what must be true for the work to be considered complete
8. **Implementation branch codename** — feature slug or task codename that can be used to satisfy `BRANCH-START-001`

## Plan Directory

All plans are stored in:

```
{project_root}/docs/specs/
```

Where `{project_root}` is the root of the current working directory. Create a new subdirectory for each plan if it doesn't exist.

## File Naming Convention

Plan directory format: `{YYYY-MM-DD}-{feature-slug}/`

Plan file format: `plan.md`

Full path structure: `docs/specs/{YYYY-MM-DD}-{feature-slug}/plan.md`

- **Timestamp**: Current date in `YYYY-MM-DD` format (e.g., `2026-05-16`)
- **Feature slug**: kebab-case, short and descriptive (e.g., `auth-migration`, `documents-table-view`)
- Example: `docs/specs/2026-05-16-auth-migration/plan.md`

## Plan Markdown Format

Every plan file MUST follow this structure:

```markdown
# {Plan Title}

**Created:** {ISO 8601 date}
**Status:** Planning | In Progress | Completed | Cancelled
**Related PRD:** {link or reference, if applicable}
**Branch rule:** BRANCH-START-001
**Suggested branch:** {feat|fix|chore}/{feature-slug}

---

## Context

{Brief description of what this plan addresses and why. Include the current state, the target outcome, and the affected domain or workflow.}

## Objective

{Single clear outcome this work must achieve. State the actor, action, mechanism, and expected result.}

## Scope

### In Scope

- {Explicit behavior or deliverable included in this plan}
- {Additional included behavior, subsystem, or workflow}

### Out of Scope

- {Explicit exclusion to prevent scope drift}
- {Additional excluded behavior or follow-up work}

## Approach

{High-level strategy or methodology. Record key decisions, trade-offs, dependencies, and why this approach is preferred.}

## Technical Breakdown

### Functional Intent

- **Actor(s):** {Who performs the action}
- **Action:** {What they need to do}
- **Outcome owner:** {Who is accountable for the outcome}
- **Expected result:** {What changes in the system when the work is complete}

### State Model

- **Initial state:** {Relevant starting states}
- **Allowed transitions:** {State changes the implementation must support}
- **Forbidden transitions:** {State changes the implementation must prevent}
- **Approval / audit implications:** {How approvals, ownership, and audit logging are affected}

### Data Model

- **Entities affected:** {Tables, models, or domain objects}
- **Fields added/changed:** {Schema or payload changes}
- **Ownership / audit fields:** {Required approver, owner, or audit metadata}
- **Migration / compatibility notes:** {Backfill, fallback, or legacy handling if needed}

### API Contract

- **Endpoints / actions:** {Routes, commands, or public interfaces affected}
- **Input validation:** {Required validation rules and failure cases}
- **Authorization / RBAC:** {Who is allowed to perform which action}
- **Response / side effects:** {State changes, audit writes, downstream effects}

### Frontend Changes

- {UI surfaces, forms, queries, and error handling to update}
- {How the UI must reflect backend truth and approval/ownership state}

### Backend Changes

- {Schema, service, repository, controller, or integration work required}
- {Validation, authorization, and audit logging expectations}

### Branch Readiness

- **Codification:** `BRANCH-START-001`
- **Suggested branch:** {feat|fix|chore}/{feature-slug}
- **Why this branch name fits:** {Short justification tied to the feature/task scope}

### Testing

- **Positive cases:** {Allowed path that must succeed}
- **Negative cases:** {Forbidden path, invalid input, or unauthorized path that must fail}
- **Integration coverage:** {Cross-layer behavior that must be verified}
- **Regression focus:** {Areas likely to break and must be rechecked}

## Tasks

| # | Task | Status | Notes |
|---|------|--------|-------|
| 1 | {Task description} | ⬜ | {Details or sub-steps} |
| 2 | {Task description} | ⬜ | {Details or sub-steps} |
| 3 | {Task description} | ⬜ | {Details or sub-steps} |

Status icons: ⬜ Not started | 🔵 In progress | ✅ Done | ⛔ Blocked | ⏭ Skipped

## Risks & Open Questions

- {Risk or unknown 1}
- {Risk or unknown 2}

## Acceptance Criteria

- [ ] {Binary, testable outcome}
- [ ] {Required validation, authorization, state, or audit behavior}

## References

- {Related PRDs, specs, issues, or plans}

## Changelog

| Date | Change |
|------|--------|
| {ISO date} | Plan created |
```

Use `knowledge-base/api-prd-template.md` as the reference for the level of technical specificity. Do not copy it section-for-section blindly; adapt its rigor to the implementation plan so the plan remains execution-oriented.

## Execution Steps

### Step 1: Gather information

- Clarify the plan topic and scope if not already provided
- Identify related artifacts (PRDs, Linear issues, existing plans)
- Inspect any referenced PRD, template, or spec before writing the plan
- Identify the affected layers: schema, backend services, API contracts, frontend surfaces, audit/RBAC
- Check `plan/` directory for existing plans on the same topic

### Step 2: Check for duplicates

- Check `docs/specs/` directory for existing plans on the same topic
- Use Glob to search: `docs/specs/*{keyword}*/plan.md`
- If a plan already exists for the same topic, **update it** rather than creating a new one

### Step 3: Produce the technical breakdown

- Decompose the work into functional intent, state model, data model, and API contract
- Add frontend, backend, migration, and audit/RBAC details when they are relevant
- Capture assumptions explicitly rather than leaving them implied
- Document negative cases, forbidden transitions, and approval behavior where applicable
- Include branch readiness details needed to satisfy `BRANCH-START-001`

### Step 4: Derive implementation tasks

- Convert the technical breakdown into concrete implementation tasks
- Group tasks by phase or subsystem when it improves clarity
- Ensure tasks cover schema, service, controller/API, UI, audit logging, and tests when applicable
- Ensure each task is specific enough to execute without reopening planning

### Step 5: Generate timestamp

- Use the current date in `YYYY-MM-DD` format

### Step 6: Write the plan file

- Create directory structure: `docs/specs/{YYYY-MM-DD}-{feature-slug}/`
- Write the plan file as `plan.md` in the created directory
- Use the appropriate file editing tool to create or update the file at the correct path
- Ensure all sections are filled in with meaningful content
- Tasks must be specific and actionable; shallow plans are not acceptable
- Capture all reasoning, trade-offs, and decisions in the plan document itself

### Step 7: Present to user

- Report the full file path as a clickable link
- Present a summary of the plan
- **STOP and ask for approval** before executing any tasks in the plan

## Rules

1. **Always write the plan file** — The plan file is the single source of truth. Every reasoning step, trade-off, and decision must be reflected in the document
2. **Never execute without approval** — After writing or updating a plan, stop and ask the user for approval before taking any execution action (code changes, file operations, Linear issue creation, etc.)
3. **Always encode branch readiness** — Every implementation-oriented plan must include `BRANCH-START-001` and a suggested branch name before handoff to implementation
