# Threat model

Status: **Draft, non-normative Phase 0 analysis**

## Objective

Define the adversaries, assets, trust assumptions, and failure modes that a
HAIO-GATS implementation must declare. This document does not assert that any
control is implemented.

## Assets

- Human Supervisor identity and intervention capability.
- Authority grants, revocation state, and lifecycle decisions.
- Canonical events, signed statements, receipts, and consistency evidence.
- Policy versions, trust anchors, and key history.
- Restricted evidence and sanitized disclosure records.
- External-system state and observed outcomes.
- Backups, recovery checkpoints, and reconciliation results.
- Conformance declarations and primary test evidence.

## Trust domains

The following domains should not be assumed independent merely because they are
separate processes or accounts:

1. Human identity and authority administration.
2. AI agent and executor runtime.
3. Policy decision and approval service.
4. Canonical recorder and query infrastructure.
5. Signing-key service.
6. Transparency service and monitor.
7. Evidence custodian and backup operator.
8. Independent verifier or auditor.
9. External system whose state is changed.

Organizational ownership, administrative access, shared credentials, shared
cloud control planes, common incident responders, and financial dependence may
create correlated compromise.

## Required threat classes

| Threat | Example | Required design response |
| --- | --- | --- |
| Scope expansion | Agent changes an additional repository | Exact resource binding and fail-closed drift detection |
| Approval replay | Old approval reused for a new action | Action digest, operation ID, nonce, expiration, atomic consumption |
| False attribution | Display name substituted for identity | Authenticated subject binding and issuer evidence |
| Compromised actor | Agent credential stolen | Revocation checks, bounded grants, monitoring, key-compromise process |
| Role substitution | Executor records itself as verifier | Relationship disclosure and independent-verifier rule at Level A |
| Capture bypass | Direct API avoids recorder | Complete path inventory, enforcement choke points, bypass detection |
| Record rewriting | Database and chain replaced | External registration, consistency proof, independent checkpoint |
| Split view | Transparency service presents two histories | Gossip, monitors, consistency exchange, or second service |
| Key compromise | Signer rewrites or forges statements | Rotation, revocation, historical interpretation, notification |
| Privacy leakage | Prompt or receipt exposes secrets | Minimization, separated views, access accountability |
| Partial outcome | Effect succeeds; record fails | Explicit inconsistent state, containment, compensation, reconciliation |
| Stale restoration | Backup predates registered events | Independent checkpoint comparison before resume |
| Human compromise | Supervisor coerced or deceived | Comprehensible preview, step-up controls, separation, contest, halt |
| Availability attack | Custodian outage blocks work | Declared fail-closed policy, bounded offline mode, no silent bypass |
| Supply-chain compromise | Signing library or build altered | Build provenance, dependency review, reproducible verification |

## Adversary capabilities

Each implementation must state whether the adversary may control:

- the AI model or its prompt/context;
- an agent credential or process;
- the executor and recorder together;
- a platform or database administrator;
- a signing key or key-service administrator;
- the transparency service;
- the network between services;
- backup or restore infrastructure;
- the Human Supervisor account;
- multiple nominally separate roles through collusion.

## Residual-risk record

At minimum, a residual-risk decision should identify the threat, affected
assets, current controls, missing higher-level control, likelihood and impact
basis, expiration/review date, accepting Human Supervisor, and linked event.

## Unknowns requiring resolution

- Identity provider and assurance level for the Human Supervisor.
- Named organizations and administrators in each trust domain.
- Independence and collusion criteria for Level A.
- Maximum acceptable halt latency by workflow.
- Offline and break-glass behavior.
- Key custody, compromise, and historical-validation process.
- External outcome-observation sources.
- Privacy jurisdiction and evidence-retention duties.
