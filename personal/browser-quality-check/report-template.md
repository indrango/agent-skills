# Browser Quality Check Report

## Summary

- Result: PASS | PASS WITH ISSUES | FAIL | BLOCKED
- Release Recommendation: Release | Release with known issues | Do not release | QA blocked
- Target URL: <url>
- Final URL: <url after redirects>
- Approved Plan: <inline summary or path/reference>
- Plan Conformance: conformant | deviations | blocked
- Test Source: URL-only smoke check | Chat test case | Test case file: <path>
- Browser Mode: Headed via agent-browser
- Browser Engine: Chromium via agent-browser unless otherwise stated
- Environment: <local/staging/production/unknown>
- Executed At: <YYYY-MM-DD HH:mm timezone>
- Tester: AI agent
- Artifact Directory: <path or not saved>
- Journey Start Time: <timestamp>
- Journey End Time: <timestamp>
- Total End-to-End Duration: <HH:MM:SS>

## Approved Plan Baseline

Summarize the approved `browser-quality-plan` or inline plan used for execution.

### QA Intent

- Objective: <what this QA run validated>
- Mode: Simple Journey | Full Browser QA
- Approval Source: <user/chat/request>
- Approval Notes: <notes>

### Planned Scope

#### In Scope

- <checked behavior or flow>

#### Out of Scope

- <explicitly skipped behavior>

### Planned Safety Gates

- Data Mutation Risk: <none/read-only/creates data/updates data/destructive confirmed>
- Safety Gates: <submit/payment/delete/update/email/SMS/permission/irreversible gates or none>
- Approval for Safety Gates: <approved/not approved/not applicable>

### Planned Evidence and Naming

- Raw Screenshot Naming: `TC-<id>-step-<nn>-<viewport>.png`
- Annotated Screenshot Naming: `BUG-<id>-TC-<id>-step-<nn>-<viewport>.png`
- Annotation Source Naming: `BUG-<id>-TC-<id>-step-<nn>-<viewport>.html` or `.svg`
- Network Evidence Naming: `network.har` or `network-requests.md`
- Recording Naming: `recording-<flow-or-finding-id>.webm`
- Report File: `qa-report.md`

## Plan Conformance and Deviations

| Area | Planned | Executed | Status | Reason / Approval |
| --- | --- | --- | --- | --- |
| Scope | <planned scope> | <executed scope> | conformant/deviation/blocked | <reason> |
| Viewports | <planned> | <executed> | conformant/deviation/blocked | <reason> |
| Evidence | <planned> | <captured> | conformant/deviation/blocked | <reason> |
| Safety Gates | <planned> | <observed> | conformant/deviation/blocked | <reason> |
| Quality Dimensions | <planned> | <executed> | conformant/deviation/blocked | <reason> |

## Test Inputs

- Preconditions: <preconditions>
- Test Data: <test data, redact secrets>
- Viewports/Devices: <viewport list>
- Locale/Timezone: <locale/timezone or not specified>
- Authentication: <not required/session/profile/user-provided/manual/blocked>
- Feature Flags / Dependencies: <flags/services or none known>
- Cleanup: <complete/not needed/pending>

## Requirement and Risk Traceability Matrix

Map each planned requirement, test step, or material risk to observed validation and evidence.

| ID | Requirement / Risk | Expected Result or Control | Planned Validation | Actual Validation | Duration | Evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | <requirement or risk> | <expected/control> | <planned validation> | <actual validation> | <HH:MM:SS> | <screenshot/network/timing/report note> | PASS/FAIL/BLOCKED |

## Execution Notes

| Step | Traceability ID | Action | Expected | Result Criteria | Observed | Duration | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | R-01 / TC-01 | <action> | <expected> | PASS if <condition>; FAIL if <condition>; BLOCKED if <condition> | <observed> | <HH:MM:SS> | PASS/FAIL/BLOCKED | <file/ref> |

## Findings

| ID | Severity | Title | Area | Traceability ID | Steps to Reproduce | Expected | Actual | Evidence | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BUG-001 | Critical/High/Medium/Low/Info | <title> | <page/flow> | R-01 / TC-01 | <steps> | <expected> | <actual> | <screenshot/HAR/request> | <concise recommendation> |

## Annotated Screenshot Attachments

Use this section for failed checks, visual defects, or UI issues. Keep the original screenshot path and include an annotated copy with red rectangles, high-contrast labels, and finding ID callouts.

Preferred annotation method: local HTML/SVG overlay opened and captured with `agent-browser`. Fallbacks: ImageMagick `magick`, Python Pillow, or another deterministic local image annotation tool.

| Finding ID | Traceability ID | Screenshot Type | Raw Screenshot | Annotation Source | Annotated Screenshot Attachment | Annotation Method | Visual Markers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BUG-001 | R-01 / TC-01 | Error / UI defect / Failed step | <screenshots/TC-01-step-03-desktop.png> | <screenshots/annotated/BUG-001-TC-01-step-03-desktop.html> | <screenshots/annotated/BUG-001-TC-01-step-03-desktop.png> | HTML/SVG overlay captured with agent-browser | Red rectangle around affected area; highlighted label `BUG-001` | <what the marker shows> |

## Network and Console-Relevant Observations

- Failed Requests: <none/list>
- Slow or Stuck Requests: <none/list>
- Error States Shown in UI: <none/list>
- Console-Relevant Notes: <none/list when available>
- Network Evidence: <network.har/network-requests.md/not captured + reason>

## Quality Dimension Results

- Functional Behavior: <pass/issues/not checked + reason>
- UI and Visual Quality: <pass/issues/not checked + reason>
- Responsive Behavior: <pass/issues/not checked + reason>
- Navigation and Routing: <pass/issues/not checked + reason>
- Forms and Validation: <pass/issues/not checked + reason>
- Network and Integration: <pass/issues/not checked + reason>
- Accessibility Smoke: <pass/issues/not checked + reason>
- Error Handling: <pass/issues/not checked + reason>
- Performance Smoke: <pass/issues/not checked + reason>
- Cross-Browser/Device Coverage: <pass/issues/not checked + reason>
- State and Persistence: <pass/issues/not checked + reason>
- Permissions/Downloads/Uploads: <pass/issues/not checked + reason>
- Internationalization/Content: <pass/issues/not checked + reason>
- Security and Privacy Smoke: <pass/issues/not checked + reason>
- Reproducibility/Flakiness: <pass/issues/not checked + reason>
- Cleanup: <complete/not needed/pending>

## Evidence and Attachments

- Raw Screenshots: <paths>
- Annotated Screenshot Attachments: <paths, or none>
- Annotation Sources / Methods: <HTML/SVG source paths, ImageMagick/Pillow command notes, or none>
- HAR / Network Logs: <paths>
- Recordings: <paths>
- Console/UI Error Notes: <paths or inline notes>
- Other Artifacts: <paths>

## Limitations

- Not Executed: <coverage not executed and why>
- Partially Executed: <partial coverage and why>
- Blocked Evidence: <evidence unavailable and why>
- Deviations from Plan: <deviations and approval/reason>
- Assumptions: <assumptions used>

## Risks and Follow-Up

- Key Risks: <risks>
- Required Follow-Up: <actions>
- Owner / Next Step: <owner/action>
