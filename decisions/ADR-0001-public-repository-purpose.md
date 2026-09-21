# ADR-0001: Define the public repository as a specification and conformance project

## Status

Proposed

## Date

2026-09-20

## Context

Existing projects implement useful portions of the HAIO-GATS problem, but no
reviewed repository establishes the complete composition of human authority,
exact-action approval, outcome evidence, transparency, custody, recovery, and
independent verification. A public collaboration surface could improve the
specification and tests, but premature implementation claims could mislead
users and collapse distinct assurance properties.

## Proposed decision

Use the repository first for specification text, schemas, threat analysis,
conformance tests, interoperability research, and explicitly non-normative
examples. Do not present it as a production implementation, certification
service, or evidence custodian.

## Alternatives considered

### Publish an implementation-first repository

Rejected for the initial phase because storage or framework choices would
precede resolution of the authority, custody, and failure model.

### Keep all work private

Not preferred because independent criticism and interoperability feedback can
improve the design, provided disclosure, licensing, and governance gates are
completed first.

### Add the project to the existing workspace governance repository

Rejected because public specification collaboration must not expose or inherit
private workspace status, operational evidence, or unrelated governance data.

## Consequences

- Public status language must remain conservative.
- Draft schemas and examples must be visibly non-normative.
- Remote creation and publication require separate authorization.
- Implementations can later live here or in separate repositories only after an
  explicit architecture and licensing decision.
