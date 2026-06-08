---
name: "quality-assurance"
description: "Validates implemented specs with traceable QA plans and reports. Invoke after implementation review or when user asks for QA validation."
---

# Quality Assurance

## Purpose

Validate implemented work against approved `spec-generator` artifacts before release.

This skill is used after implementation is complete and manual review is approved. It verifies that the implementation:

- Works end-to-end
- Matches the approved spec artifacts
- Preserves explicitly unchanged behavior
- Meets functional and non-functional quality standards
- Is safe to release to staging or production

This skill does not design features, redefine requirements, expand scope, or refactor production code unless the user explicitly asks for fixes.

## Source of Truth

Validate against approved `spec-generator` artifacts in this order:

1. `requirements.md` **or** `bugfix.md`
2. `design.md`
3. `tasks.md`
4. `.config` when available

Treat these artifacts as the only source of truth for:

- Scope
- User stories
- Acceptance criteria
- Preserved behavior
- State transitions
- Authorization expectations
- Audit obligations
- Correctness properties
- Regression boundaries

If behavior exists that is not specified, flag it as **scope deviation**.

If specified behavior is missing, flag it as **implementation gap**.

If artifacts conflict with each other, flag **spec inconsistency** and mark QA as **BLOCKED** until resolved.

## QA Modes

### Feature / Enhancement Mode

Use when the spec directory contains `requirements.md`.

Validate:

- Numbered requirements
- User stories
- EARS-style acceptance criteria
- State model
- Authorization and ownership matrix
- Audit requirements
- Design correctness properties
- Task checklist and preservation expectations

### Bugfix Mode

Use when the spec directory contains `bugfix.md`.

Validate:

- Current defect behavior
- Expected corrected behavior
- Unchanged behavior
- Formal bug condition
- Fix checking property
- Preservation goal
- Design correctness properties
- Bugfix loop expectations in `tasks.md`

If the bug cannot be reproduced from the spec and implementation context, mark QA as **BLOCKED** due to insufficient defect definition.

## Required Validation Workflow

QA has two mandatory phases:

1. **Planning Phase** — inspect spec artifacts, build the traceability matrix, and create or update `qa_plan.md`.
2. **Execution Phase** — only after explicit user approval, execute validation and create or update `qa_report.md`.

The agent MUST stop after the Planning Phase and ask the user to approve the QA plan before executing tests, running automation, or producing the final QA report.

Do not execute QA from an unapproved plan.

### Execution Validation Order

After the user approves `qa_plan.md`, follow this deterministic order:

1. Functional validation
2. Edge case validation
3. Negative testing
4. Authorization and permission testing
5. UI behavior validation
6. Integration validation
7. Correctness property validation
8. Regression and preservation analysis

Do not skip steps. If a step is not applicable, state why.

## Spec Intake Contract

Accepted inputs:

- `requirements.md`
- `bugfix.md`
- `design.md`
- `tasks.md`
- `.config`

Planning order:

1. Determine spec type from available artifacts
2. Read `requirements.md` or `bugfix.md`
3. Read `design.md`
4. Read `tasks.md`
5. Build a traceability matrix
6. Create or update `qa_plan.md`
7. Present the plan summary to the user and wait for explicit approval

Execution may start only after the user approves the QA plan.

## Minimum Traceability Matrix

During the Planning Phase, construct a matrix with:

- Spec Artifact
- Reference ID / Section
- User Story or Behavior Statement
- Acceptance Criterion ID or Bugfix Clause
- Design Property / API / State / Error Case Reference
- Task Reference
- Test Case ID
- Test Type
- Result: Pass / Fail / Gap / Blocked
- Notes

## Core QA Skills

### Q1 — Spec Traceability Mapping

Map every testable requirement or bugfix behavior to at least one test case.

Also map:

- Design correctness properties to verification steps
- Preservation requirements to regression tests
- Task checklist items to coverage evidence

Identify:

- Untestable criteria
- Missing criteria
- Implemented behavior not covered by the approved spec

### Q2 — Feature Requirements Validation

For feature specs, validate:

- Happy paths
- Multi-step workflows
- State transitions
- Data persistence behavior
- Explicitly preserved behavior
- Out-of-scope protections where accidental scope expansion may occur

Tests must verify frontend behavior and backend effects where applicable.

### Q3 — Bugfix Validation

For bugfix specs, validate:

- Defect reproduction using the bug condition or known counterexamples
- Corrected behavior against the expected behavior section
- Unchanged behavior remains unchanged
- Preservation goal still holds
- Fix remains narrow and does not introduce incidental behavior changes

### Q4 — Edge Case and Boundary Testing

Validate:

- Empty inputs
- Maximum values
- Invalid formats
- Unexpected state transitions
- Boundary states defined by the spec
- Concurrent actions where applicable
- Edge cases explicitly listed in `bugfix.md` or implied by acceptance criteria

### Q5 — Negative and Abuse Testing

Simulate:

- Unauthorized access attempts
- Invalid payload submissions
- Tampered requests
- Broken API contracts
- Forbidden state transitions
- Invalid role assumptions in UI or API flows

If the system fails unsafely, mark QA as **BLOCKED**.

### Q6 — Design Consistency Validation

Validate implementation against `design.md`, including:

- Key design decisions affecting observable behavior
- Components and interfaces that shape contracts
- Data models affecting persisted outcomes
- Allowed state transitions
- Forbidden state transitions
- API contracts
- Response and error shapes
- Frontend UI states
- Correctness properties

If implementation contradicts `design.md`, classify as either:

- implementation defect, or
- spec inconsistency requiring clarification

### Q7 — UI and UX Functional Validation

Use automation when applicable:

- Playwright preferred
- Cypress acceptable
- Selenium only for legacy contexts

UI validation must check:

- Element visibility
- State changes
- Disabled/enabled states
- Form validation behavior
- Error message accuracy
- Loading states
- Empty states
- Unauthorized / forbidden states
- Basic responsive behavior
- Alignment with UI states defined in `design.md`

Use stable selectors such as `data-testid`. Validate DOM behavior, not screenshots only.

### Q8 — End-to-End Workflow Testing

Validate complete user journeys:

- Login → Action → Result
- Multi-role flows where applicable
- State-changing flows with persistence verification
- Backend state after UI actions
- Audit logs where required

### Q9 — Task Coverage and Regression Risk Analysis

Evaluate:

- Whether implementation maps to intended tasks
- Whether `tasks.md` testing checklist is covered
- Affected modules
- Shared services
- Reused components
- Database schema impact
- Explicit preservation boundaries from upstream artifacts

List potential regression risks even if no failure is detected.

## Non-Functional Quality Standards

Validate these standards where applicable:

### Reliability

- No crashes under valid use
- Graceful degradation under failure
- Consistent state management
- No contradiction with declared state transitions

### Performance

- No obvious blocking UI operations
- No unbounded loops
- No obvious N+1 database query patterns

### Usability

- Clear error messages
- No confusing state transitions
- Required fields clearly enforced
- UI states match design expectations

### Maintainability Signals

- Test coverage present
- No duplicated logic that creates observable inconsistency
- Clear separation of concerns

### Observability

- Errors logged properly
- No sensitive data exposed in UI
- Clear status codes from API
- Audit events present where required by spec

## Automation Requirements

### UI Testing

When UI exists and automation is available:

- Generate Playwright tests where useful
- Use stable selectors, preferably `data-testid`
- Avoid brittle selectors
- Align test names to requirement IDs, bugfix clauses, or correctness properties

### API Testing

Generate or identify automated API tests when applicable:

- Validate response schema and status codes
- Validate API behavior against `design.md` contracts
- Validate authorization, error, and side-effect behavior

### Contract Testing

Ensure frontend-backend contracts are validated:

- Detect breaking changes
- Validate error and authorization behavior
- Do not test success responses only

### TestDino Reporting

After the user approves `qa_plan.md` and Playwright scripts have been executed, run the configured bun script when available, for example:

```bash
bun run test:e2e:testdino
```

Use this to upload JSON test reports to TestDino for historical tracking and analysis.

## Required Outputs

Save QA outputs in the same spec artifact directory as `requirements.md`, `bugfix.md`, `design.md`, and `tasks.md`.

For a spec at:

```text
docs/specs-v2/YYYY-MM-DD-<slug>/
```

produce:

```text
docs/specs-v2/YYYY-MM-DD-<slug>/qa_plan.md
docs/specs-v2/YYYY-MM-DD-<slug>/qa_report.md
```

Every generated Markdown document must begin with:

```md
- **Version**: [version number]
- **Created**: [YYYY-MM-DD]
- **Last Updated**: [YYYY-MM-DD]
```

### QA Test Plan: `qa_plan.md`

Create or update this file during the Planning Phase before any QA execution.

Must contain:

- Plan status: PENDING USER APPROVAL / APPROVED
- Spec type: Feature / Bugfix
- Spec path
- Artifact inventory consumed
- Detailed QA strategy
- Traceability coverage table
- Test Case Inventory
- Preservation coverage
- Open coverage gaps
- Explicit approval checkpoint stating that QA execution must not begin until user approval is received

Traceability table fields:

- Spec Artifact
- Reference ID / Section
- Acceptance Criterion ID or Bugfix Clause
- Design Reference
- Task Reference
- Test Case ID
- Test Type
- Result

### QA Validation Report: `qa_report.md`

Create this file only after the user approves `qa_plan.md` and QA execution is complete.

Must contain:

- Overall Status: PASS / PASS WITH ISSUES / BLOCKED
- Spec type
- Spec path
- Coverage summary
- Traceability summary
- Correctness property validation summary
- Preservation / regression summary
- Scope deviation summary
- Identified issues

For each issue include:

- Severity: Low / Medium / High / Critical
- Category: Functional / UI / Integration / Regression / Authorization / Contract / Spec Inconsistency
- Spec reference
- Reproduction steps
- Expected vs Actual behavior

### Playwright Test Scripts

If UI tests are generated:

- Place scripts in the appropriate testing directory, not the spec directory
- Keep `qa_plan.md` and `qa_report.md` in the spec artifact directory
- Name and group tests to preserve traceability to spec references

## Blocking Conditions

Declare **BLOCKED** if:

- Acceptance criteria are not satisfied
- Authorization flaws exist
- Data corruption occurs
- UI flow breaks core workflow
- Feature crashes under normal usage
- Spec artifacts conflict in a way that prevents deterministic validation
- Bugfix defect definition is too ambiguous to reproduce or verify
- Required preserved behavior cannot be validated

## Non-Responsibilities

Do not:

- Redesign UX
- Change requirements
- Rewrite or reinterpret spec intent silently
- Refactor production code directly
- Silence failing tests
- Approve scope deviations without explicit human review

Propose fixes when useful, but do not implement them unless explicitly instructed.

## Success Criteria

QA is successful when:

- Every acceptance criterion or bugfix behavior is verifiably tested
- Traceability from spec artifacts to tests is complete
- UI and backend behavior are aligned
- Design correctness properties are validated where applicable
- Explicitly preserved behavior remains intact
- No critical or high-severity issues remain
- Automation coverage is sufficient for regression protection
- Manual test cases are synced to TestDino when tooling is available
- Automated test reports are uploaded to TestDino when tooling is available
- The feature or fix can be confidently released

## Invocation Pattern

Use this skill when the user asks to validate an implementation, run QA, generate a QA test plan, produce a QA validation report, or check whether a completed spec is release-ready.

Expected flow:

1. Read the spec directory
2. Determine feature or bugfix mode
3. Build traceability matrix
4. Generate or update `qa_plan.md`
5. Stop and ask the user to review and approve the QA plan
6. After explicit approval, execute or define tests according to the approved plan
7. Generate or update `qa_report.md`
8. Mark result as PASS, PASS WITH ISSUES, or BLOCKED
