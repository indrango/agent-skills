---
name: "browser-quality-plan"
description: "Generates approval-ready browser QA execution plans before headed browser testing. Use when a user provides a URL, chat test case, test case file, or browser QA request and planning, scope alignment, evidence planning, or approval is needed before running UI QA, smoke checks, journey checks, or exploratory validation."
---

# Browser Quality Plan

## Purpose

Use this skill to turn a browser QA request into an approval-ready plan. Do not run `agent-browser` from this skill.

The output is a plan that can later be executed by `browser-quality-check`.

## Inputs

Accept:

- URL only
- URL plus chat test case
- URL plus test case file
- URL plus test data, expected behavior, viewport/device, auth, or QA scope

If a test case file is referenced, read it first. Treat user-provided test cases or files as the source of truth.

## Intake

Capture:

- Target URL
- Test source: URL-only, chat case, or file case
- Objective and expected result
- Environment: local, staging, production, or unknown
- Authentication approach and credential constraints
- Preconditions and test data
- Viewports/devices
- Data mutation risk and destructive actions
- Locale, timezone, feature flags, and third-party dependencies
- Required evidence: screenshots, annotated screenshots, HAR/network, recording, summary, or full report

Ask a concise clarification question only when planning is blocked.

## Mode Selection

Choose one planned execution mode:

- `Simple Journey`: short flow, smoke path, or small step list.
- `Full Browser QA`: comprehensive QA, release validation, regression, formal test case execution, auth/payment/sensitive flow, or broad browser quality review.

For URL-only input, label the run as exploratory smoke QA. Full Browser QA must still be risk-based: plan only the quality dimensions relevant to the supplied scope, risks, and expected behavior.

## Planning Rules

- Always produce a plan before execution unless the user explicitly asks to skip planning.
- Do not assume credentials, hidden requirements, or unsupported browsers.
- Prefer read-only checks for production URLs.
- Mark destructive actions as requiring explicit confirmation.
- Add a safety gate before submit, purchase/payment, delete/update, email/SMS sending, or any irreversible action.
- Validate only the provided URL, test case, and approved scope.
- Include traceability from requirement or risk to planned validation and planned evidence.
- Include raw screenshots in evidence planning.
- Include annotated screenshots for failed checks, visual defects, or UI issues; do not require annotation for passing checks.
- Define evidence naming conventions for screenshots, annotated screenshots, HAR/network, recordings, and report files.
- Do not expose secrets, tokens, personal data, payment data, or credentials in the plan.

## Plan Output

Use [plan-template.md](plan-template.md). Return the filled plan inline unless the user asks to save it.

The plan must include:

- Objective and mode
- Scope and out-of-scope
- Preconditions, data, auth, and safety constraints
- Viewports/devices
- Essential review areas
- Requirement/risk traceability
- Step-level validation plan or URL-only smoke checklist
- Planned result classification criteria
- Evidence plan, including annotation expectations and artifact names
- Data mutation and privacy handling
- Planning blockers and safety gates
- Risks, assumptions, blockers, and confirmation gate

## Blocking Conditions

Mark planning as blocked instead of inventing a plan when:

- The URL is missing or not specific enough.
- Authentication is required and no approved access method is available.
- A referenced test case file cannot be read.
- Expected results are too ambiguous to validate.
- A destructive or irreversible action is required but not approved.
- Required environment, test data, dependency, or decision is unavailable.

## Handoff to Quality Check

End with a clear confirmation gate and do not proceed to execution from this skill.

```markdown
Execution will start only after approval. If approved, use `browser-quality-check` with this plan as the source of truth.
```

The executor must not reinterpret scope, add unplanned coverage, or perform destructive actions without user approval. Any unplanned observation must be reported separately as out-of-scope unless approved.
