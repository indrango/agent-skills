# Browser Quality Check Plan

## QA Intent

- Objective: <what this QA run will validate>
- Planned Mode: Simple Journey | Full Browser QA
- Target URL: <url>
- Test Source: URL-only exploratory smoke | Chat test case | Test case file: <path>
- Environment: local | staging | production | unknown

## Planned Scope

### In Scope

- \<behavior, page, journey, or validation area>

### Out of Scope

- <br />

## Preconditions, Data, and Access

- Preconditions: <required state>
- Test Data: \<data, redacted if sensitive>
- Authentication: not required | manual | existing session | user-provided | blocked
- Credentials/Sensitive Data Rules: redact secrets, tokens, credentials, payment data, and personal data from plan, report, screenshots, and logs.
- Locale/Timezone: \<locale/timezone or not specified>
- Feature Flags / Dependencies: \<flags/services or none known>

## Viewports and Devices

| Viewport / Device | Purpose                          | Required? |
| ----------------- | -------------------------------- | --------- |
| Desktop 1440x900  | Baseline desktop layout and flow | Yes/No    |
| Mobile 390x844    | Responsive sanity check          | Yes/No    |

## Essential Review Areas

| Area                   | Why It Matters                                   | Planned Validation                          | Planned Evidence                                  |
| ---------------------- | ------------------------------------------------ | ------------------------------------------- | ------------------------------------------------- |
| Page load              | Ensure page reaches a usable state               | Open URL and wait for stable content        | Final URL, title, raw screenshot                  |
| Main flow              | Validate requested user path                     | Execute provided steps or smoke journey     | Step screenshots and observations                 |
| UI/Visual              | Detect layout, clipping, or visible error states | Desktop/mobile visual check when applicable | Raw screenshots; annotated screenshots for issues |
| Network                | Detect relevant failed API/resource requests     | Inspect relevant 4xx/5xx or stuck requests  | Network request list or HAR when needed           |
| Error handling         | Confirm unexpected error states are reproducible | Observe UI and failed states                | Screenshot, finding, annotated evidence           |
| Accessibility smoke    | Check practical usability of major controls      | Keyboard/focus/label sanity where relevant  | Observation and screenshots when useful           |
| Security/privacy smoke | Avoid obvious sensitive exposure                 | Inspect URL/UI/captured evidence            | Redacted notes and screenshots                    |

## Requirement and Risk Traceability

Map every applicable requirement, test step, and material risk to planned validation and evidence.

| ID   | Requirement / Risk    | Expected Result or Control | Planned Validation | Planned Evidence                         | Priority        |
| ---- | --------------------- | -------------------------- | ------------------ | ---------------------------------------- | --------------- |
| R-01 | <requirement or risk> | \<expected/control>        | <how to validate>  | \<screenshot/network/timing/report note> | High/Medium/Low |

## Planned Checks

Use this table for test cases or journeys.

| ID    | Step / Requirement      | Expected Result | Planned Validation | Evidence Needed             | Result Criteria                                                  |
| ----- | ----------------------- | --------------- | ------------------ | --------------------------- | ---------------------------------------------------------------- |
| TC-01 | <action or requirement> | <expected>      | <how to validate>  | \<screenshot/network/notes> | PASS if <condition>; FAIL if <condition>; BLOCKED if <condition> |

For URL-only smoke checks, use this checklist.

| Check                  | Expected                                                              | Planned Evidence               |
| ---------------------- | --------------------------------------------------------------------- | ------------------------------ |
| Page loads             | URL loads without browser-level error                                 | Final URL, title, screenshot   |
| Main content           | Primary content is visible                                            | Screenshot and observation     |
| Navigation             | Header/menu/primary links are usable                                  | Step notes and screenshots     |
| Primary CTA            | Main call-to-action is discoverable and works safely                  | Step notes and screenshots     |
| Layout desktop         | No obvious broken layout at desktop viewport                          | Desktop screenshot             |
| Layout mobile          | No obvious broken layout at mobile viewport when applicable           | Mobile screenshot              |
| Forms                  | Visible forms validate basic required input when applicable           | Step notes and screenshots     |
| Network                | No relevant failed XHR/fetch requests                                 | Network request summary or HAR |
| Performance smoke      | Page becomes usable without excessive waiting or infinite loading     | Timing notes                   |
| Accessibility smoke    | Keyboard focus and labels are usable for major controls               | Observation                    |
| Security/privacy smoke | No obvious sensitive data exposure in URL, UI, or evidence            | Redacted observation           |
| State persistence      | Refresh/session behavior is sane for the checked flow when applicable | Step notes                     |
| Error states           | No unexpected user-facing error state                                 | Screenshot and observation     |

## Planned Result Classification

- PASS: all scoped checks pass and no release-relevant findings are observed.
- PASS WITH ISSUES: required checks complete, core flow works, and only non-blocking issues remain.
- FAIL: one or more scoped expected results fail, or a critical browser behavior/regression is observed.
- BLOCKED: validation cannot be completed due to missing access, ambiguous expectations, unavailable environment/data, unsafe action, or browser tooling failure.

## Evidence Plan

- Artifact Directory: `browser-qa-artifacts/<slug>-<YYYYMMDD-HHMM>/` if saving artifacts
- Report File: `qa-report.md`
- Raw Screenshot Naming: `TC-<id>-step-<nn>-<viewport>.png`, for example `TC-01-step-03-desktop.png`
- Annotated Screenshot Naming: `BUG-<id>-TC-<id>-step-<nn>-<viewport>.png`, for example `BUG-001-TC-01-step-03-desktop.png`
- Annotation Source Naming: `BUG-<id>-TC-<id>-step-<nn>-<viewport>.html` or `.svg`
- Network Evidence Naming: `network.har` or `network-requests.md`
- Recording Naming: `recording-<flow-or-finding-id>.webm`
- Raw Screenshots: planned | not needed
- Annotated Screenshots: planned for failed checks, visual defects, and UI issues | not needed
- Annotation Method: HTML/SVG overlay captured with `agent-browser`; fallback ImageMagick, Python Pillow, or another deterministic local tool
- Network Evidence: request summary | HAR | not needed
- Console/UI Error Notes: planned | not needed
- Timing Evidence: end-to-end | per step | not measured
- Recording: planned for timing-sensitive or multi-step reproduction | not needed

## Data Mutation and Safety

- Data Mutation Risk: none | read-only | creates data | updates data | destructive
- Destructive Actions: none | requires explicit confirmation
- Safety Gates: stop before submit, purchase/payment, delete/update, email/SMS sending, permission grant, or irreversible action unless explicitly approved.
- Cleanup Plan: <cleanup or not needed>
- Production Safety: prefer read-only checks; stop before destructive actions.

## Planning Blockers

Mark planning or execution as blocked if any required item is unavailable.

| Blocker                                          | Status | Resolution Needed |
| ------------------------------------------------ | ------ | ----------------- |
| URL missing or unreachable                       | yes/no | <needed action>   |
| Authentication required but unavailable          | yes/no | <needed action>   |
| Test case file unreadable                        | yes/no | <needed action>   |
| Expected result ambiguous                        | yes/no | <needed action>   |
| Destructive action unapproved                    | yes/no | <needed action>   |
| Required environment/data/dependency unavailable | yes/no | <needed action>   |

## Risks, Assumptions, and Blockers

- Risks: <known risks>
- Assumptions: <assumptions>
- Open Questions: <questions or none>
- Blockers: <blockers or none>
- Scope Control: browser-quality-check must use this plan as the source of truth. Additional coverage, changed scope, or destructive actions require user approval.

## Confirmation Gate

- Status: Pending approval
- Approval Needed From: user
- Execution Instruction: After approval, execute this plan using `browser-quality-check` and produce a completed report with evidence and annotated screenshots for findings.
- Handoff Rule: executor must not reinterpret scope, add unplanned coverage, or perform destructive actions without explicit approval. Unplanned observations must be reported separately as out-of-scope unless approved.

