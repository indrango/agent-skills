# Browser Quality Check Report

## Summary

- Result: PASS | PASS WITH ISSUES | FAIL | BLOCKED
- Release Recommendation: Release | Release with known issues | Do not release | QA blocked
- Target URL: <url>
- Final URL: <url after redirects>
- Approved Plan: <inline summary or path/reference>
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

Summarize the approved browser-quality-plan or inline plan used for execution.

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

### Planned Evidence

- Raw Screenshots: <planned/not needed>
- Annotated Screenshots for Failed Checks: <planned/not needed>
- Network Evidence: <planned/not needed>
- Console/UI Error Notes: <planned/not needed>
- Timing Evidence: <end-to-end / per step / not measured>

## Test Inputs

- Preconditions: <preconditions>
- Test Data: <test data, redact secrets>
- Viewports/Devices: <viewport list>
- Locale/Timezone: <locale/timezone or not specified>
- Authentication: <not required/session/profile/user-provided/manual/blocked>
- Data Mutation Risk: <none/read-only/creates data/updates data/destructive confirmed>
- Cleanup: <complete/not needed/pending>

## Traceability Matrix

| ID | Requirement / Test Step | Expected Result | Validation Performed | Duration | Evidence | Status |
| --- | --- | --- | --- | --- | --- | --- |
| TC-01 | <step or requirement> | <expected> | <actual validation> | <HH:MM:SS> | <screenshot/log/ref> | PASS/FAIL/BLOCKED |

## Execution Notes

| Step | Action | Expected | Observed | Duration | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | <action> | <expected> | <observed> | <HH:MM:SS> | PASS/FAIL/BLOCKED | <file/ref> |

## Findings

| ID | Severity | Title | Area | Steps to Reproduce | Expected | Actual | Evidence | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BUG-001 | Critical/High/Medium/Low/Info | <title> | <page/flow> | <steps> | <expected> | <actual> | <screenshot/HAR/request> | <concise recommendation> |

## Annotated Screenshot Attachments

Use this section for failed checks, visual defects, or UI issues. Keep the original screenshot path and include an annotated copy with red rectangles, highlight text, and finding ID callouts.

Preferred annotation method: local HTML/SVG overlay opened and captured with `agent-browser`. Fallbacks: ImageMagick `magick`, Python Pillow, or another deterministic local image annotation tool.

| Finding ID | Screenshot Type | Raw Screenshot | Annotation Source | Annotated Screenshot Attachment | Annotation Method | Visual Markers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BUG-001 | Error / UI defect / Failed step | <screenshots/TC-01-step-03-desktop.png> | <screenshots/annotated/BUG-001-TC-01-step-03-desktop.html> | <screenshots/annotated/BUG-001-TC-01-step-03-desktop.png> | HTML/SVG overlay captured with agent-browser | Red rectangle around affected area; highlighted label `BUG-001` | <what the marker shows> |

## Network and Console-Relevant Observations

- Failed Requests: <none/list>
- Slow or Stuck Requests: <none/list>
- Error States Shown in UI: <none/list>
- Console-Relevant Notes: <none/list when available>

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
- Other Artifacts: <paths>

## Limitations

- Not Executed: <coverage not executed and why>
- Partially Executed: <partial coverage and why>
- Blocked Evidence: <evidence unavailable and why>
- Assumptions: <assumptions used>

## Risks and Follow-Up

- Key Risks: <risks>
- Required Follow-Up: <actions>
- Owner / Next Step: <owner/action>
