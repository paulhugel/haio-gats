# ADR-0002: Retain Human Supervisor authority over normative changes

## Status

Proposed

## Date

2026-09-20

## Context

Public participation can supply evidence, criticism, and implementation
experience. It does not itself identify the accountable actor for a normative
release. Repository administration, pull-request approval, automated checks,
and popularity are also distinct from operational authority.

## Proposed decision

Until a separately approved governance transition, Paul Garrett Hugel retains
final Human Supervisor authority over normative HAIO-GATS changes. Normative
changes require documented review and an affirmative, attributable decision.
Merging, tagging, publishing, implementing, and claiming conformance remain
separate lifecycle gates.

## Alternatives considered

### Maintainer-majority vote

Deferred until maintainer identity, eligibility, conflicts, quorum, appeals,
and accountability are defined.

### Unreviewed author discretion

Rejected for material changes because it would collapse author and reviewer
roles and weaken the evidence basis.

### Automated acceptance after tests pass

Rejected because tests cannot resolve normative intent, human-factors risk,
legal meaning, or acceptance of residual risk.

## Consequences

- Contributors advise but do not authorize normative releases.
- Independent review should be recorded for material changes.
- Future governance transition requires its own ADR and Human Supervisor
  approval.
