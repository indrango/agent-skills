---
name: "browser-quality-check"
description: "Executes approved browser QA plans in a headed browser and produces evidence-backed reports with annotated screenshots. Invoke after a browser-quality-plan is approved, or when the user explicitly asks to run browser QA now with a URL, test case, or test case file."
---

# Browser Quality Check

## Purpose

Use this skill to execute an approved browser QA plan in a real headed browser using the installed `agent-browser` CLI.

This skill produces a completed quality report, raw evidence, and annotated screenshot attachments for failed checks, visual defects, or UI issues.

If no approved plan exists, first use `browser-quality-plan` unless the user explicitly asks to skip planning and run now.

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

When executing without a separate plan, infer the minimal safe plan inline, label assumptions clearly, and keep scope limited to the user request.

## Operating Rules

- Validate against the approved plan, URL, and test case only.
- Do not expand scope unless the user asks or the approved plan requires it.
- Default to headed mode.
- Never assume credentials.
- Do not expose secrets in commands, reports, screenshots, logs, or annotations.
- Use persistent profile/session only with user approval.
- Prefer read-only checks for production URLs.
- Stop for confirmation before destructive actions.
- Preserve raw screenshots. Create annotated copies only when needed.
- If a dimension is not applicable or not requested, mark it `Not checked` with a short reason.

## Evidence Location

Create an evidence directory only when screenshots, HAR files, recordings, or a report will be saved.

Recommended structure:

```text
browser-qa-artifacts/<slug>-<YYYYMMDD-HHMM>/
  screenshots/
  screenshots/annotated/
  network.har
  recording.webm
  console-or-ui-errors.txt
  qa-report.md
```

Artifact rules:

- Name screenshots by step and viewport, for example `TC-01-step-03-desktop.png`.
- Save raw screenshot paths in the report.
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

### 2. Execute planned steps

For each step:

1. Use `agent-browser snapshot -i` to identify current element refs.
2. Start timing before interaction.
3. Perform the action using refs when possible.
4. Wait for URL, text, selector, network idle, or expected UI state.
5. Stop timing when expected state is reached or failure is confirmed.
6. Capture evidence after meaningful state changes.
7. Compare observed result against expected result.
8. Record status, duration, and evidence.

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

Apply only dimensions relevant to the approved plan and risks:

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

Use one final result:

- `PASS`: All scoped checks passed with no release-relevant issues.
- `PASS WITH ISSUES`: Core flow works, but non-blocking issues were found.
- `FAIL`: One or more scoped acceptance criteria or critical browser behaviors failed.
- `BLOCKED`: QA could not be completed due to missing access, missing data, unstable environment, ambiguous test case, or tooling failure.

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
- Approved plan reference or inline plan summary
- Scope and inputs
- Traceability matrix
- Execution notes
- Findings
- Annotated screenshot evidence table
- Network and console-relevant observations
- Quality dimension results
- Evidence paths and attachments
- Risks and follow-up

## Blocking Conditions

Mark the result as `BLOCKED` when:

- URL is missing or unreachable.
- Authentication is required and no approved method is available.
- Test case file cannot be read.
- Expected results are too ambiguous to validate.
- Environment is unstable enough that results are not trustworthy.
- Browser tooling cannot launch or interact with the page.

## Final Response Format

After completing QA, respond concisely:

```markdown
Browser QA completed: <PASS/PASS WITH ISSUES/FAIL/BLOCKED>

Report: <path if saved, otherwise inline summary>
Evidence: <artifact directory or key screenshots>
Annotated screenshots: <paths or none>
Top findings:
- <finding or "None">
```
