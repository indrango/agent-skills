# Bugfix Requirements Document Template

## Purpose

Use this template for defects, regressions, broken flows, API mismatches, incorrect UI behavior, or any change where the safest path is to fix a specific bug while preserving non-bug behavior.

The bugfix spec must define the exact bug condition and preservation boundary before implementation.

## Spec Pattern

Bugfix specs use:

- Introduction
- Current Behavior (Defect)
- Expected Behavior (Correct)
- Unchanged Behavior (Regression Prevention)
- Formal Bug Condition
- Fix Checking Property
- Preservation Goal

This prevents broad, accidental changes.

## Bugfix Principles

- Define the bug before proposing the fix
- Fix only the bug condition
- Preserve all non-bug behavior
- Prefer the smallest targeted fix
- Write or identify tests that fail before the fix when feasible
- Re-run the same bug-condition tests after the fix
- Re-run preservation tests after the fix

## Template

```md
# Bugfix Requirements Document

## Introduction

[Describe the bug, affected surface, and impact.]

The issue occurs when [trigger/context]. This causes [bad outcome]. The fix should be [minimal/targeted/systemic] while preserving [important existing behaviors].

## Bug Analysis

### Current Behavior (Defect)

1.1 WHEN [bug trigger] THEN the system [incorrect behavior].

1.2 WHEN [related bug trigger] THEN the system [incorrect behavior].

1.3 WHEN [edge case] THEN the system [incorrect behavior].

### Expected Behavior (Correct)

2.1 WHEN [same trigger] THEN the system SHALL [correct behavior].

2.2 WHEN [related trigger] THEN the system SHALL [correct behavior].

2.3 IF [edge case], THEN the system SHALL [correct behavior].

### Unchanged Behavior (Regression Prevention)

3.1 WHEN [non-bug path] THEN the system SHALL CONTINUE TO [existing behavior].

3.2 WHEN [another non-bug path] THEN the system SHALL CONTINUE TO [existing behavior].

3.3 WHEN [existing API/component behavior] THEN the system SHALL CONTINUE TO [existing behavior].

---

## Bug Condition (Formal)

### Bug Condition Function

```pascal
FUNCTION isBugCondition(input)
  INPUT: input of type [InputType]
  OUTPUT: boolean

  RETURN [condition that identifies buggy input/context]
END FUNCTION
```

### Fix Checking Property

```pascal
FOR ALL X WHERE isBugCondition(X) DO
  result ← fixedBehavior(X)
  ASSERT result.[observable] = [expected value]
    AND result.[anotherObservable] = [expected value]
END FOR
```

### Preservation Goal

```pascal
FOR ALL X WHERE NOT isBugCondition(X) DO
  ASSERT originalBehavior(X) = fixedBehavior(X)
END FOR
```

## Evidence and Counterexamples

- **Known Counterexample 1**: [Concrete failing input/action and observed bad output]
- **Known Counterexample 2**: [Concrete failing input/action and observed bad output]
- **Non-Bug Example**: [Concrete input/action that must remain unchanged]

## Out of Scope

- [Explicit non-goal]
- [Explicit non-goal]

## Open Questions

- [Question]
```

## Quality Gate

Before saving `bugfix.md`, confirm:

- [ ] Current behavior is observable and specific
- [ ] Expected behavior is testable
- [ ] Non-bug behavior is explicitly protected
- [ ] Bug condition is narrow enough to prevent scope creep
- [ ] Preservation goal exists
- [ ] Edge cases are documented
- [ ] Open questions are listed rather than assumed
