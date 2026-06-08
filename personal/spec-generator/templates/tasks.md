# Implementation Tasks Template

## Purpose

Use this template after `design.md` exists. The tasks document converts the design into an ordered, dependency-aware execution plan.

Tasks must be concrete enough for an executor agent to implement without guessing.

## Spec Pattern

Tasks use:

- Numbered implementation groups
- Subtasks with concrete actions
- Requirement references
- Optional property tests marked with `*`
- Checkpoints
- Task dependency graph
- Final verification notes

Recommended task markers:

| Marker | Meaning |
|---|---|
| `[ ]` | Required pending |
| `[~]` | In progress or generated target task |
| `[x]` | Completed |
| `[ ]*` | Optional task |
| `[-]` | Blocked or deferred |

## Recommended Implementation Order

When backend state, RBAC, approval, ownership, or audit behavior is involved, tasks should follow this order:

1. Schema
2. Migration
3. Validation schemas
4. Repository/data access
5. Service layer business rules
6. RBAC guards at API boundary
7. Controller/API routes, thin only
8. Audit logging integrated with state changes
9. Frontend query/state awareness
10. Frontend forms and explicit confirmations
11. Frontend error, loading, empty, and unauthorized states
12. Tests and verification

For UI-only specs, preserve existing API contracts and follow component hierarchy from `design.md`.

For bugfix specs, include the bugfix loop:

1. Write or run bug-condition test that should fail on unfixed code
2. Write or run preservation tests that should pass on unfixed code
3. Implement the smallest targeted fix
4. Re-run the same bug-condition test and confirm it passes
5. Re-run preservation tests and confirm they still pass
6. Run final verification

## Template

```md
# Implementation Plan: [Feature / Fix Name]

## Overview

This plan implements [feature/fix] following this order:

1. [Layer 1]
2. [Layer 2]
3. [Layer 3]
4. [Verification]

## Tasks

- [ ] 1. [Major workstream]
  - [ ] 1.1 [Specific implementation task]
    - [Concrete implementation step]
    - [Concrete implementation step]
    - [Concrete implementation step]
    - _Requirements: [1.1, 1.2]_

  - [ ] 1.2 [Specific implementation task]
    - [Concrete implementation step]
    - [Concrete implementation step]
    - _Requirements: [2.1]_

- [ ] 2. [Testing workstream]
  - [ ] 2.1 Write behavior tests
    - [Test case]
    - [Expected assertion]
    - _Requirements: [x.y]_

  - [ ]* 2.2 Write optional property-based tests
    - **Property [N]: [Property name]**
    - Generate [input domain]
    - Assert [invariant]
    - **Validates: Requirements [x.y]**

- [~] 3. Checkpoint — [Scope]
  - Ensure relevant tests pass
  - Verify requirement traceability
  - Ask the user if questions arise

- [ ] 4. Final verification
  - Run lint
  - Run typecheck
  - Run relevant tests
  - Run build if appropriate
  - Verify no regression to preserved behavior
  - Verify implementation satisfies all referenced requirements

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1", "1.2"] },
    { "id": 1, "tasks": ["2.1", "2.2"] },
    { "id": 2, "tasks": ["4"] }
  ]
}
```

## Testing Checklist

- [ ] Positive test: allowed behavior succeeds
- [ ] Negative test: forbidden behavior is rejected with correct error
- [ ] Role test: unauthorized role receives 403 where applicable
- [ ] Ownership test: owner fields are correct where applicable
- [ ] Audit test: state change creates correct audit log entry where applicable
- [ ] Preservation test: explicitly unchanged behavior still works

## Notes

- Tasks marked with `*` are optional.
- Every implementation task should reference requirements.
- Every state-changing backend feature must include audit behavior if applicable.
- Every approval or ownership feature must preserve explicit owner visibility.
- Frontend should reflect backend state, not independently enforce authorization.
```

## Quality Gate

Before saving `tasks.md`, confirm:

- [ ] Tasks are dependency-aware
- [ ] Tasks follow backend-first implementation order when backend state is involved
- [ ] Every task references requirements
- [ ] Tests are tied to correctness properties where applicable
- [ ] Checkpoints are included
- [ ] Final verification includes lint, typecheck, and relevant tests
- [ ] Bugfix tasks include bug-condition and preservation verification
- [ ] Optional tasks are clearly marked
