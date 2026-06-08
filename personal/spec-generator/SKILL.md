---
name: "spec-generator"
description: "Generates spec-driven requirements, design, and tasks docs. Invoke when user asks to create or plan a feature/bugfix spec."
---

# Spec Generator

## Purpose

Generate spec-driven artifacts before implementation. Use this skill when the user wants to turn a product idea, feature request, UI enhancement, backend workflow, refactor, or bugfix into structured specs.

This skill follows a spec-driven development approach:

```text
requirements.md or bugfix.md
        ↓
design.md
        ↓
tasks.md
        ↓
implementation
        ↓
verification
```

The goal is to make specification the source of truth. Code should be treated as an artifact of the spec, not the other way around.

## When to Invoke

Invoke this skill when the user asks to:

- Create a new spec
- Generate requirements, design, or tasks
- Plan a feature using a spec-driven workflow
- Convert an idea into implementation-ready documentation
- Structure a bugfix before coding
- Create `docs/specs-v2/YYYY-MM-DD-<slug>/requirements.md`, `bugfix.md`, `design.md`, or `tasks.md`
- Improve a specification-first workflow

Do not invoke this skill for direct implementation unless the user first asks for specs or planning artifacts.

## Core Principles

- Problem before solution
- Outcomes over output
- Smallest thing that proves value
- Evidence over intuition
- Requirements before design
- Design before tasks
- Tasks before implementation
- Trace every implementation task back to requirements
- Preserve existing behavior explicitly
- Do not fill important product, ownership, RBAC, approval, or audit gaps with assumptions

## General Project Alignment

All generated specs should respect common production-quality project rules:

- Deterministic workflows over hidden intelligence
- Human-in-the-loop for approvals and AI-generated outputs
- Visible ownership for important decisions
- Immutable audit logs for meaningful state changes where auditability is required
- Backend state is the source of truth
- Frontend reflects backend permissions and state; it does not enforce authorization independently
- No hidden state transitions
- No business logic in controllers or UI
- Schema-first backend implementation when data models are involved
- Controller → Service → Repository layering when the architecture uses layered backend boundaries

If a requested feature involves approval, ownership, RBAC, audit logging, AI drafting, state transitions, or compliance records, the spec must explicitly address those areas.

## Template Files

This skill uses separate template documents. Always read the relevant template file before generating the corresponding spec artifact.

| Artifact to Generate | Template File | Use When |
|---|---|---|
| `requirements.md` | `templates/requirements.md` | New feature, UI enhancement, backend workflow, behavior-changing refactor |
| `bugfix.md` | `templates/bugfix.md` | Defect, regression, broken flow, incorrect behavior, API mismatch |
| `design.md` | `templates/design.md` | After `requirements.md` or `bugfix.md` exists or is drafted |
| `tasks.md` | `templates/tasks.md` | After `design.md` exists or is drafted |

## Routing Rules

### Feature or Enhancement

If the user asks for a new feature, UI enhancement, backend workflow, or behavior-changing refactor:

1. Read `templates/requirements.md`
2. Generate `docs/specs-v2/YYYY-MM-DD-<slug>/requirements.md`
3. Read `templates/design.md`
4. Generate `docs/specs-v2/YYYY-MM-DD-<slug>/design.md`
5. Read `templates/tasks.md`
6. Generate `docs/specs-v2/YYYY-MM-DD-<slug>/tasks.md`
7. Generate `docs/specs-v2/YYYY-MM-DD-<slug>/.config`

Expected output:

```text
docs/specs-v2/YYYY-MM-DD-<slug>/
  requirements.md
  design.md
  tasks.md
  .config
```

### Bugfix

If the user asks to fix a bug, regression, broken flow, incorrect behavior, or API mismatch:

1. Read `templates/bugfix.md`
2. Generate `docs/specs-v2/YYYY-MM-DD-<slug>/bugfix.md`
3. Read `templates/design.md`
4. Generate `docs/specs-v2/YYYY-MM-DD-<slug>/design.md`
5. Read `templates/tasks.md`
6. Generate `docs/specs-v2/YYYY-MM-DD-<slug>/tasks.md`
7. Generate `docs/specs-v2/YYYY-MM-DD-<slug>/.config`

Expected output:

```text
docs/specs-v2/YYYY-MM-DD-<slug>/
  bugfix.md
  design.md
  tasks.md
  .config
```

### Partial Artifact Request

If the user asks for only one artifact:

- For requirements only: use `templates/requirements.md`
- For bugfix only: use `templates/bugfix.md`
- For design only: use `templates/design.md`, but first read existing `requirements.md` or `bugfix.md` if present
- For tasks only: use `templates/tasks.md`, but first read existing `requirements.md` or `bugfix.md` and `design.md` if present

Do not generate downstream artifacts if the user explicitly requests only one artifact.

### Existing Spec Update

If the target `docs/specs-v2/YYYY-MM-DD-<slug>/` already exists:

1. Read existing spec files first
2. Identify whether the user asked for append, update, or replacement
3. Do not overwrite existing files without clear intent
4. Preserve existing requirement IDs where possible
5. Preserve traceability from tasks to requirements

## Classification Step

Before generating files, classify the work as one of:

| Type | Generate |
|---|---|
| Feature | `requirements.md`, `design.md`, `tasks.md` |
| Bugfix | `bugfix.md`, `design.md`, `tasks.md` |
| UI enhancement | `requirements.md`, `design.md`, `tasks.md`, usually lighter backend scope |
| Backend workflow | `requirements.md`, `design.md`, `tasks.md`, with state/API/audit detail |
| Refactor | `requirements.md` or `bugfix.md` if behavior changes, otherwise `design.md` and `tasks.md` |

If classification is ambiguous, ask before generating artifacts.

## Clarification Before Generation

Clarification is mandatory before generating any artifact.

Before writing `requirements.md`, `bugfix.md`, `design.md`, or `tasks.md`, do one of the following:

1. Ask focused clarification questions when important ambiguity remains, or
2. If the request already appears detailed enough, present a structured understanding summary and ask the user to confirm it before proceeding.

Do not generate any artifact until the user confirms the understanding.

Ask at most 5 questions at a time, prioritizing the highest-impact unknowns first.

Prefer this clarification structure:

1. Actor — Who is the primary actor and what role do they have?
2. Action — What exact action or workflow change is needed?
3. Problem — What problem is this solving?
4. Outcome — What result proves this is successful?
5. Scope — What is explicitly in scope and out of scope?
6. Preservation — What must remain unchanged?
7. Risk — What is most likely to be misunderstood, break, or conflict with existing behavior?

When terminology is vague, overloaded, or inconsistent, call it out and ask for a precise meaning.

When ambiguity remains, use a concrete scenario or edge case to force precision.

If a clarification can be answered from the codebase or existing specs, inspect those first before asking.

Do not generate implementation tasks until the problem, desired behavior, preservation boundaries, and critical constraints are clear.

## Output Location

For spec-driven artifacts, write files under:

```text
docs/specs-v2/YYYY-MM-DD-<slug>/
```

Slug format is mandatory: `YYYY-MM-DD-<slug>`, where the date uses the current local date and `<slug>` is lowercase kebab-case.

If the user asks to use another destination, follow the requested destination but keep the same document structure and slug format unless they explicitly override it.

## `.config` Template

For features:

```json
{
  "type": "feature",
  "status": "draft",
  "createdBy": "codex-agent",
  "phase": "tasks",
  "artifacts": {
    "requirements": true,
    "bugfix": false,
    "design": true,
    "tasks": true
  }
}
```

For bugfixes:

```json
{
  "type": "bugfix",
  "status": "draft",
  "createdBy": "codex-agent",
  "phase": "tasks",
  "artifacts": {
    "requirements": false,
    "bugfix": true,
    "design": true,
    "tasks": true
  }
}
```

## Template Analysis Reference

Spec-driven documents use a traceability-first format:

```text
1. Define problem or desired behavior
2. Define terminology
3. Convert behavior into numbered requirements or bug conditions
4. Convert requirements into design decisions
5. Define components, data, APIs, states, and transitions
6. Define correctness properties
7. Define test strategy
8. Convert everything into traceable implementation tasks
9. Add checkpoints
10. Preserve behavior explicitly
```

For bugfixes:

```text
1. Describe the defect
2. Describe current broken behavior
3. Describe expected corrected behavior
4. Describe unchanged behavior
5. Define formal bug condition
6. Define fix-checking property
7. Define preservation-checking property
8. Design the smallest targeted fix
9. Write or identify tests that fail before the fix
10. Apply fix
11. Re-run bug tests and preservation tests
```

## Generation Procedure

### Step 1: Clarify and Confirm Scope

Before any document generation, establish shared understanding.

If the request is ambiguous, ask focused clarification questions one at a time, prioritizing the highest-impact unknown first.

If the request appears sufficiently detailed, do not skip clarification. Instead, present a confirmation summary that reflects your understanding of:

- actor
- problem
- requested change
- desired outcome
- in-scope behavior
- out-of-scope behavior
- unchanged behavior
- approval, ownership, RBAC, audit, or AI-review implications where relevant
- primary risk or unresolved ambiguity

Also confirm:

- feature or bugfix slug
- destination folder
- whether to generate all artifacts, one artifact, or only missing artifacts
- whether the user wants review checkpoints after each artifact or end-to-end generation

Hard gate:

- Do not load templates for generation until clarification is complete
- Do not generate documents while shared understanding is still unresolved
- Do not proceed until the user confirms the understanding summary

Definition of done for this step:

- The response explicitly shows the interpreted problem, actor, scope, preserved behavior, and destination folder
- Any important ambiguity is surfaced, not assumed away
- The user confirms the understanding before artifact generation begins

## Clarification Rules

During clarification:

- Challenge vague or overloaded terms
- Ask for precise meanings when a term could mean multiple things
- Surface contradictions between the user's description, existing specs, and current code when found
- Prefer one high-value question at a time over a large batch of shallow questions
- Use concrete scenarios when they help resolve ambiguity faster
- Even when no clarification questions are needed, present an understanding summary and ask for confirmation before generating the first artifact

### Step 2: Load Proper Template

Display which template(s) will be used before proceeding.

Use the routing table:

- `requirements.md` → `templates/requirements.md`
- `bugfix.md` → `templates/bugfix.md`
- `design.md` → `templates/design.md`
- `tasks.md` → `templates/tasks.md`

Definition of done for this step:

- The response explicitly confirms the selected template path for each artifact to be generated
- The response explicitly confirms that generated documents will be written into the destination folder confirmed in Step 1

### Step 3: Generate Requirements or Bugfix Spec

Display a step confirmation before generation and a completion confirmation after generation.

For features, generate `requirements.md` into the confirmed destination folder.

For bugfixes, generate `bugfix.md` into the confirmed destination folder.

Quality gate:

- Every acceptance criterion is independently testable
- Actors and roles are explicit
- Ownership expectations are explicit where applicable
- State transitions are explicit if applicable
- Audit obligations are specified for every state change
- AI review implications are explicit if applicable
- Existing behavior preservation is explicit
- Open questions are listed rather than assumed
- Out of scope is explicit

Definition of done for this step:

- `requirements.md` or `bugfix.md` is generated in the confirmed destination folder
- The response explicitly confirms the generated file path
- The generated file passes the quality gate before advancing
- If review checkpoints are enabled, the response stops here and asks the user to review before continuing to design

### Step 4: Generate Design

Display a step confirmation before generation and a completion confirmation after generation.

Generate `design.md` from the requirements or bugfix spec using `templates/design.md`, and write it into the confirmed destination folder.

Quality gate:

- Design decisions are explicit
- Architecture and layering are clear
- Schema-first thinking is used when data model changes are involved
- Data model includes ownership and audit fields where applicable
- API contract has roles, side effects, errors, and validation expectations
- UI states are explicitly covered where frontend behavior is involved
- Approval UI requirements are explicit where approval actions exist
- Alternatives considered are captured when trade-offs matter
- Correctness properties validate requirements
- Testing strategy matches the feature type

Definition of done for this step:

- `design.md` is generated in the confirmed destination folder
- The response explicitly confirms the generated file path
- The generated file passes the quality gate before advancing
- If review checkpoints are enabled, the response stops here and asks the user to review before continuing to tasks

### Step 5: Generate Tasks

Display a step confirmation before generation and a completion confirmation after generation.

Generate `tasks.md` from the design using `templates/tasks.md`, and write it into the confirmed destination folder.

Quality gate:

- Tasks are dependency-aware
- Each task is one logical unit of work
- Tasks follow backend-first implementation order when backend state is involved
- Every task references requirements
- File scope is explicit when implementation precision matters
- Tests are tied to correctness properties
- Checkpoints are included
- Final verification includes lint, typecheck, and relevant tests

Definition of done for this step:

- `tasks.md` is generated in the confirmed destination folder
- The response explicitly confirms the generated file path
- The generated file passes the quality gate before advancing
- The response includes a concise implementation handoff summary after tasks generation

### Step 6: Save Files

Display a final save confirmation before completing the workflow.

Create or update the target `docs/specs-v2/YYYY-MM-DD-<slug>/` files.

Also create or update `.config` in the same destination folder so that it accurately reflects:

- spec type
- current status
- current phase
- which artifacts exist

Never overwrite existing spec files without checking whether the user expects update or replacement.

Definition of done for this step:

- Every requested artifact exists in the confirmed destination folder
- `.config` exists in the confirmed destination folder and matches the generated artifacts
- The response explicitly lists the final saved file paths
- The response explicitly confirms whether each file was created or updated

## Final Response

Summarize:

- Created or updated files
- Template files used
- Spec type
- Key assumptions or open questions
- If tasks were generated, include a concise handoff with spec path, generated artifacts, and recommended next step
- Recommended next step, usually invoking `spec-executor` after review
