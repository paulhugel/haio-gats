# Security policy

## Current status

This repository is a local, unpublished specification candidate. It contains no
operational service and currently accepts no external vulnerability reports.

Before publication, the Human Supervisor must designate a private reporting
channel, response roles, service-level expectations, encryption requirements,
and coordinated-disclosure process.

## In-scope future reports

- Ambiguities that could authorize a broader action than intended.
- Replay, substitution, scope-drift, or identity-binding weaknesses.
- Missing-event, partial-write, or action/receipt atomicity failures.
- Signature, canonicalization, transparency, consistency, or custody defects.
- Key-compromise and recovery weaknesses.
- Privacy leakage from schemas, receipts, metadata, fixtures, or examples.
- Conformance tests that accept a system violating a normative requirement.

## Reporting constraints

Do not publish secrets, personal data, private deployment details, proof-of-
concept attacks against live systems, or uncoordinated vulnerabilities in a
public issue. A future security policy must provide a private channel before
the repository is opened to outside reports.

## Evidence limits

A security report, patch, passing test, signature, or hash does not constitute
independent verification. Remediation must identify the actor, evidence,
affected versions, residual risk, and review relationship.
