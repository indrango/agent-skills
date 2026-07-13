---
name: "browser-quality-check"
description: "Executes approved browser QA plans in a headed browser and produces traceable evidence-backed reports with annotated screenshots. Use after a browser-quality-plan is approved, or when the user explicitly asks to run browser QA now with a URL, test case, or test case file."
---

# Browser Quality Check

## Purpose

Use this skill to execute browser QA in a real headed browser using the installed `agent-browser` CLI.

Preferred flow:

1. Use an approved `browser-quality-plan` as the source of truth.
2. Execute only the approved scope, checks, safety gates, and evidence plan.
3. Produce a completed report, raw evidence, and annotated screenshot attachments.

If no approved plan exists and the user explicitly asks to run QA now, create a proper inline QA plan before browser execution. The inline plan must follow the same structure and safeguards as `browser-quality-plan`.

## Required Dependency

This skill depends on the installed `agent-browser` skill and CLI from:

`https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser`

Use `agent-browser` commands for all browser interaction. Default to headed mode:

```bash
AGENT_BROWSER_HEADED=1 agent-browser open <url>
```

or:

```bash
agent-browser --headed open <url>
```

## Execution Inputs

Accept:

- An approved browser QA plan
- A URL plus explicit instruction to run without separate planning
- A chat test case or test case file plus explicit instruction to run

If a test case file is referenced, read it before planning or execution. Preserve test case IDs, step numbering, expected results, result criteria, and evidence requirements in the report.

## Plan Intake and Execution Gate

Before launching `agent-browser`, resolve the execution baseline:

- Approved plan reference or inline plan
- Target URL and environment
- Scope and out-of-scope items
- Preconditions, test data, auth approach, and access constraints
- Viewports/devices
- Requirement/risk traceability
- Planned checks and result criteria
- Evidence naming conventions and artifact directory
- Data mutation risk and safety gates
- Planning blockers, assumptions, and limitations

Do not execute if the plan has unresolved blockers. Ask a concise clarification question when execution cannot be performed safely or expected results are too ambiguous to validate.

## Required Inline QA Plan

When executing without an approved `browser-quality-plan`, create an inline QA plan before launching `agent-browser`.

The inline plan must include:

- Objective and planned mode: `Simple Journey` or `Full Browser QA`
- Target URL, environment, and test source
- In-scope and out-of-scope behavior
- Preconditions, test data, authentication approach, and access constraints
- Viewports/devices to execute
- Requirement/risk traceability
- Step-level checks or URL-only smoke checklist
- Expected result and result criteria for each planned check
- Evidence plan with artifact naming
- Data mutation risk, destructive action risk, and safety gates
- Security/privacy handling for screenshots, logs, tokens, credentials, payment data, and personal data
- Assumptions, blockers, and limitations

Use this compact inline plan format:

```markdown
# Inline Browser QA Plan

## Intent
- Objective: <objective>
- Mode: Simple Journey | Full Browser QA
- URL: <url>
- Test Source: <URL-only / chat test case / file test case>
- Environment: <local/staging/production/unknown>

## Scope
- In Scope: <items>
- Out of Scope: <items>

## Preconditions and Safety
- Auth: <not required/manual/session/user-provided/blocked>
- Test Data: <redacted data or none>
- Viewports: <viewport list>
- Data Mutation Risk: <none/read-only/creates/updates/destructive>
- Safety Gates: stop before submit, purchase/payment, delete/update, email/SMS sending, permission grant, or irreversible action unless approved.

## Requirement and Risk Traceability
| ID | Requirement / Risk | Expected Result or Control | Planned Validation | Planned Evidence | Priority |
| --- | --- | --- | --- | --- | --- |
| R-01 | <requirement/risk> | <expected/control> | <validation> | <evidence> | High/Medium/Low |

## Planned Checks
| ID | Check / Step | Expected Result | Evidence | Result Criteria |
| --- | --- | --- | --- | --- |
| TC-01 | <step> | <expected> | <raw screenshot/network/timing> | PASS if <condition>; FAIL if <condition>; BLOCKED if <condition> |

## Evidence Plan
- Artifact Directory: `browser-qa-artifacts/<slug>-<YYYYMMDD-HHMM>/`
- Raw Screenshot Naming: `TC-<id>-step-<nn>-<viewport>.png`
- Annotated Screenshot Naming: `BUG-<id>-TC-<id>-step-<nn>-<viewport>.png`
- Network Evidence: `network.har` or `network-requests.md`
- Timing: <end-to-end/per-step/not measured>
- Recording: <planned/not needed>

## Risks and Assumptions
- Risks: <risks>
- Assumptions: <assumptions>
- Blockers: <blockers or none>
```

For URL-only smoke QA, include the minimum checks from `browser-quality-plan`: page load, main content, navigation, primary CTA, desktop/mobile layout, forms, network, performance smoke, accessibility smoke, security/privacy smoke, state persistence, and error states.

## Operating Rules

- Validate against the approved plan, inline plan, URL, and test case only.
- Do not reinterpret scope, add unplanned coverage, or perform destructive actions without user approval.
- Record unplanned observations separately as out-of-scope unless approved.
- Execute only relevant quality dimensions from the plan and risks.
- Default to headed mode.
- Never assume credentials.
- Do not expose secrets in commands, reports, screenshots, logs, or annotations.
- Use persistent profile/session only with user approval.
- Prefer read-only checks for production URLs.
- Stop before submit, purchase/payment, delete/update, email/SMS sending, permission grant, or irreversible action unless explicitly approved.
- Preserve raw screenshots. Create annotated copies for failed checks, visual defects, and UI issues.
- If a dimension is not applicable or not requested, mark it `Not checked` with a short reason.

## Evidence Location and Naming

Create an evidence directory only when screenshots, HAR files, recordings, or a report will be saved.

Recommended structure:

```text
browser-qa-artifacts/<slug>-<YYYYMMDD-HHMM>/
  screenshots/
  screenshots/annotated/
  network.har
  network-requests.md
  recording-<flow-or-finding-id>.webm
  console-or-ui-errors.txt
  qa-report.md
```

Artifact rules:

- Raw screenshots: `TC-<id>-step-<nn>-<viewport>.png`, for example `TC-01-step-03-desktop.png`.
- Annotated screenshots: `BUG-<id>-TC-<id>-step-<nn>-<viewport>.png`.
- Annotation sources: `BUG-<id>-TC-<id>-step-<nn>-<viewport>.html` or `.svg`.
- Save raw evidence paths in the report.
- For each failed check, visual defect, or UI issue, create an annotated copy in `screenshots/annotated/`.
- Do not alter the original screenshot.
- Redact secrets, tokens, personal data, and payment data before recording evidence.
- Save HAR or network output when integration behavior is part of the check.
- Capture recordings only for multi-step, timing-sensitive, or visual reproduction issues.

## Browser Execution Workflow

### 1. Open target and establish baseline

```bash
AGENT_BROWSER_HEADED=1 agent-browser open <url>
agent-browser wait --load networkidle
agent-browser get url
agent-browser get title
agent-browser snapshot -i
agent-browser screenshot --full --screenshot-dir <artifact-dir>/screenshots
agent-browser network requests --status 400-599
```

Record final URL, page title, visible landmarks/content, interactive element refs, obvious broken states, and relevant failed network requests.

### 2. Execute planned checks

For each planned check:

1. Map the check to its requirement/risk traceability ID.
2. Confirm the check is in scope and no safety gate blocks it.
3. Use `agent-browser snapshot -i` to identify current element refs.
4. Start timing before interaction.
5. Perform the action using refs when possible.
6. Wait for URL, text, selector, network idle, or expected UI state.
7. Stop timing when expected state is reached or failure is confirmed.
8. Capture the planned evidence using the required artifact names.
9. Compare observed result against expected result and result criteria.
10. Record status, duration, evidence path, and deviations.

Common commands:

```bash
agent-browser click @e1
agent-browser fill @e2 "value"
agent-browser select @e3 "Option"
agent-browser check @e4
agent-browser press Enter
agent-browser wait --load networkidle
agent-browser wait --url "**/expected-path"
agent-browser wait --text "Success"
agent-browser screenshot --full --screenshot-dir <artifact-dir>/screenshots
```

Record end-to-end duration and per-step duration when relevant. Format durations as `HH:MM:SS`.

### 3. Validate relevant quality dimensions

Apply only dimensions relevant to the plan and risks:

- Functional behavior
- UI and visual quality
- Responsive behavior
- Navigation and routing
- Forms and validation
- Network and integration
- Accessibility smoke
- Error handling
- Performance smoke
- Cross-browser/device coverage actually executed
- State, session, and persistence
- Permissions, downloads, uploads, and browser dialogs
- Internationalization and content quality
- Security and privacy smoke
- Reproducibility and flakiness
- Cleanup

Use deterministic waits over fixed sleeps. Re-run a failed or flaky step once only when the failure may be timing-related. If attempts differ, mark the finding as flaky and include both observations.

## Annotated Screenshot Requirements

Create annotated screenshots for failed checks, visual defects, or UI issues.

Preferred method:

1. Capture and keep the raw screenshot, for example `screenshots/TC-01-step-03-desktop.png`.
2. Identify affected coordinates from the screenshot or browser-observed element location.
3. Create an annotation source artifact, for example `screenshots/annotated/BUG-001-TC-01-step-03-desktop.html` or `.svg`.
4. Draw red rectangles, high-contrast labels, and short callouts that map to finding IDs such as `BUG-001`.
5. Open the annotation source locally with `agent-browser` and capture the annotated result as `screenshots/annotated/BUG-001-TC-01-step-03-desktop.png`.
6. Record raw screenshot, annotation source, annotated screenshot, method, markers, and notes in the report.

Fallback methods: ImageMagick `magick`, Python Pillow, or another deterministic local annotation tool. Record the method used.

Do not depend on manual image editing apps. Do not annotate sensitive data; redact first if needed.

## Result Levels

Use the planned result criteria first, then classify the overall result:

- `PASS`: All scoped checks passed with no release-relevant issues.
- `PASS WITH ISSUES`: Required checks complete, core flow works, and only non-blocking issues remain.
- `FAIL`: One or more scoped expected results fail, or a critical browser behavior/regression is observed.
- `BLOCKED`: QA could not be completed due to missing access, missing data, unsafe action, unstable environment, ambiguous test case, or tooling failure.

## Issue Severity

Classify findings:

- `Critical`: Blocks core flow, data integrity, payment/auth, or safe release.
- `High`: Major user path broken or severe regression risk.
- `Medium`: Important behavior degraded but workaround exists.
- `Low`: Minor visual, copy, or polish issue.
- `Info`: Observation or improvement note, not a defect.

## Report Output

Use [report-template.md](report-template.md). Copy it into the artifact directory as `qa-report.md` when saving artifacts.

The report must include:

- Summary and final recommendation
- Approved plan reference or inline QA plan
- Plan conformance and deviations
- Scope and inputs
- Requirement/risk traceability matrix
- Execution notes with result criteria
- Findings
- Annotated screenshot attachment table
- Network and console-relevant observations
- Quality dimension results
- Evidence paths and attachments
- Limitations, risks, and follow-up

## Blocking Conditions

Mark the result as `BLOCKED` when:

- URL is missing or unreachable.
- Authentication is required and no approved method is available.
- Test case file cannot be read.
- Expected results are too ambiguous to validate.
- A required safety gate is not approved.
- Environment is unstable enough that results are not trustworthy.
- Browser tooling cannot launch or interact with the page.

## Final Response Format

After completing QA, respond concisely:

```markdown
Browser QA completed: <PASS/PASS WITH ISSUES/FAIL/BLOCKED>

Plan: <approved plan reference or inline plan summary>
Plan conformance: <conformant/deviations/blocked>
Report: <path if saved, otherwise inline summary>
Evidence: <artifact directory or key screenshots>
Annotated screenshots: <paths or none>
Top findings:
- <finding or "None">
```
