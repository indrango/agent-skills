# Requirements Document Template

## Purpose

Use this template for new features, UI enhancements, backend workflows, and behavior-changing refactors.

The requirements document defines what must be true from the user, business, compliance, and system perspective. It should not prescribe implementation details unless they are product constraints.

## Spec Pattern

Feature requirements use:

- Introduction
- Glossary
- Numbered requirements
- User stories
- Acceptance criteria using EARS-style language
- Explicit preserved behavior when relevant

Acceptance criteria should use:

- `WHEN [condition], THE [component] SHALL [behavior]`
- `IF [condition], THEN THE [component] SHALL [behavior]`
- `WHILE [state], THE [component] SHALL [behavior]`

Components should be named explicitly, such as `Document_Version_Service`, `Access_Control_Guard`, or `Document_UI`.

## Requirements Checklist

Every requirements document must address the following when applicable:

- Actor and role
- Ownership of outcome
- Whether ownership becomes immutable after approval
- Initial state
- Allowed state transitions
- Forbidden state transitions
- RBAC/API authorization boundary
- Audit log obligations
- AI involvement and human review gate
- Backend as source of truth
- Existing behavior that must be preserved
- Explicit out-of-scope items
- Open questions instead of assumptions

## Template

```md
# Requirements Document

## Introduction

[Describe the feature or initiative.]

This feature enables [actor/user] to [capability] so that [business/user outcome]. It supports [relevant product principle, compliance requirement, operational goal, or user workflow].

## Glossary

- **[Term_Name]**: [Definition]
- **[Component_Name]**: [Definition]
- **[Role_Name]**: [Definition]
- **[State_Name]**: [Definition]

## Requirements

### Requirement 1: [Capability Name]

**User Story:** As a [role], I want [capability], so that [outcome].

#### Acceptance Criteria

1. WHEN [condition/event], THE [system/component/service/UI] SHALL [expected behavior].
2. IF [condition], THEN THE [system/component/service/UI] SHALL [expected behavior].
3. WHILE [state], THE [system/component/service/UI] SHALL [expected behavior].
4. THE [system/component/service/UI] SHALL [always-true requirement].

### Requirement 2: [Capability Name]

**User Story:** As a [role], I want [capability], so that [outcome].

#### Acceptance Criteria

1. WHEN [condition/event], THE [system/component/service/UI] SHALL [expected behavior].
2. IF [condition], THEN THE [system/component/service/UI] SHALL [expected behavior].

### Requirement 3: Preserve Existing Behavior

**User Story:** As a [role], I want existing behavior to remain unchanged, so that [workflow/system expectation] is not disrupted.

#### Acceptance Criteria

1. WHEN [existing behavior condition], THE [system/component] SHALL CONTINUE TO [existing behavior].
2. WHEN [another existing path], THE [system/component] SHALL CONTINUE TO [existing behavior].

## State Model

| State | Meaning | Allowed Transitions | Forbidden Transitions |
|-------|---------|---------------------|-----------------------|
| [State] | [Meaning] | [Transitions] | [Forbidden transitions] |

## Authorization and Ownership

| Role | Allowed Actions | Owns Outcome | Notes |
|------|-----------------|--------------|-------|
| [Role] | [Actions] | [Yes/No] | [Notes] |

## Audit Requirements

| Action | Actor | Entity | Required Audit Fields |
|--------|-------|--------|-----------------------|
| [Action] | [Actor] | [Entity] | actor ID, actor role, action, entity type, entity ID, timestamp |

## Out of Scope

- [Explicit non-goal]
- [Explicit non-goal]

## Open Questions

- [Question]
- [Question]
```

## Quality Gate

Before saving `requirements.md`, confirm:

- [ ] Every acceptance criterion is independently testable
- [ ] Actors and roles are explicit
- [ ] Ownership is explicit where decisions or approvals exist
- [ ] State transitions are explicit where lifecycle exists
- [ ] Forbidden transitions are listed where lifecycle exists
- [ ] Audit requirements are listed for meaningful state changes
- [ ] Existing behavior preservation is explicit
- [ ] Out-of-scope section prevents scope creep
- [ ] Open questions are listed rather than assumed
