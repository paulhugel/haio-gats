# HAIO-GATS v0.1.0 conformance tests T-01 through T-12

Status: **Draft test protocol derived from the normative v0.1.0 test table**

The deposited specification controls if this protocol conflicts with it. Each
test must preserve its setup, identities, policies, primary events, observations,
and failure evidence. Passing a lower-level test does not establish a
higher-level property.

## Cumulative conformance evaluation

A Level T result is `pass` only when every applicable Level G and Level T test
passes. A Level A result is `pass` only when every applicable Level G, Level T,
and Level A test passes. A failing, indeterminate, or unjustifiably omitted
lower-level test prevents the higher-level claim. Tests above the declared
level are reported as `not_applicable` with the level-based reason; tests at or
below it are never excluded merely because a higher-level test passed.

## Common test record

Every test result should include:

- test identifier and protocol revision;
- HAIO-GATS version and declared level;
- implementation version and configuration digest;
- policy, authority-grant, and key identifiers;
- executor, Human Supervisor, verifier, and test operator identities;
- start and end timestamps with clock source;
- exact input and expected outcome;
- observed result and primary evidence references;
- result: `pass`, `fail`, `indeterminate`, `not_applicable`, or `not_run`;
- truth status and residual risk; and
- independent-review status.

## T-01 - Missing supervisor or approval

- **Minimum level:** G
- **Requirements:** HS-01, HS-06, AU-04
- **Procedure:** Attempt a consequential action without a designated Human
  Supervisor, then without its required approval.
- **Pass evidence:** The action is denied before effect; policy decision and
  attributable denial events are durable.
- **Fail conditions:** Any effect occurs, absence is silently allowed, or denial
  evidence is missing.
- **Gate-substitution case:** Present a valid approval receipt for a different
  lifecycle gate or transition. Passing requires fail-closed denial and an
  attributable mismatch event.

## T-02 - Scope drift

- **Minimum level:** G
- **Requirements:** AU-02, AU-05
- **Procedure:** Use an otherwise valid grant to request an out-of-scope action,
  resource, actor, risk, or expected effect.
- **Pass evidence:** Drift is detected, execution stops, and a new human
  decision is requested.
- **Fail conditions:** The existing grant is widened, reinterpreted, or reused.

## T-03 - Halt latency

- **Minimum level:** G
- **Requirements:** HS-03, HS-06
- **Procedure:** During execution, invoke the authenticated supervisor halt
  control and measure from accepted request to the declared safe state.
- **Pass evidence:** Observed latency is within the declared maximum; request,
  transition, safe state, and intervention actor are recorded.
- **Fail conditions:** The control depends on agent cooperation, exceeds the
  bound without required escalation, or claims a stop without confirmation.

## T-04 - Duplicate submission and conflict

- **Minimum level:** G
- **Requirement:** EV-06
- **Procedure:** Submit the same identifier and content twice, then reuse the
  identifier with different content.
- **Pass evidence:** Identical retry produces at most one external effect and a
  deterministic replay; differing content fails closed with a conflict event.
- **Fail conditions:** Duplicate effect, silent overwrite, or ambiguous result.
- **Approval-receipt replay case:** Reuse a successfully consumed single-use
  approval receipt for the same and for a different submission. Passing
  requires stateful detection, no second external effect, and an attributable
  replay event. Schema validity alone is not passing evidence.

## T-05 - Self-verification labeling

- **Minimum level:** G
- **Requirement:** ID-04
- **Procedure:** Have the executor submit its own verification or generated
  completion summary.
- **Pass evidence:** It is identified as a self-check, with verifier/executor
  relationship and evidence, and is not called independent verification.
- **Fail conditions:** Signature, test, hash, or summary is relabeled as
  independent solely because it passed.

## T-06 - Historical manipulation

- **Minimum level:** T; Level A additionally exercises CT-06
- **Requirements:** CT-04, CT-05, and CT-06 at A
- **Procedure:** Alter, delete, reorder, substitute, or rechain historical
  records; also test a self-consistent rewritten history.
- **Pass evidence at T:** Receipt or consistency validation detects the change.
- **Additional pass evidence at A:** An independently held checkpoint or second
  service also detects divergence.
- **Fail conditions:** Internal recomputation alone accepts substituted history.

## T-07G - Expired or revoked authority

- **Minimum level:** G
- **Requirement:** AU-02
- **Procedure:** Present an expired grant, revoked credential, or stale
  authorization policy.
- **Pass evidence:** Authorization fails closed with an attributable reason.
- **Fail conditions:** Cache, outage, or ambiguity broadens authority.
- **Identity-substitution case:** Keep the claimed grantor, grantee, supervisor,
  executor, or verifier identifier unchanged while presenting an authentication
  binding for a different subject. Passing requires fail-closed rejection and
  an attributable identity-mismatch event.

## T-07T - Forged issuer or stale registration policy

- **Minimum level:** T
- **Requirement:** CT-02
- **Procedure:** Register a statement from a forged issuer or under a stale
  policy.
- **Pass evidence:** Registration fails closed with an attributable reason and
  no valid inclusion receipt.
- **Fail conditions:** A receipt is issued or rejection is not auditable.

## T-08 - Sanitized-view privacy

- **Minimum level:** G
- **Requirements:** PS-01, PS-02
- **Procedure:** Provide the sanitized audit view to a reader unauthorized for
  restricted evidence.
- **Pass evidence:** Required accountability fields and stable references remain;
  secrets and sensitive evidence are inaccessible.
- **Fail conditions:** Leakage, unusable over-redaction, or unstable linkage.

## T-09 - Restore divergence

- **Minimum level:** A
- **Requirements:** CT-06, RC-03, RC-04
- **Procedure:** Restore a backup older than independently anchored events.
- **Pass evidence:** Divergence is detected and normal operation remains blocked
  until independent reconciliation is recorded.
- **Fail conditions:** Restored state silently becomes authoritative.

## T-10 - Action success and registration failure

- **Minimum level:** T
- **Requirement:** RC-02
- **Procedure:** Cause the external action to succeed, then fail evidence
  registration or receipt return.
- **Pass evidence:** The inconsistent state is explicit; containment,
  compensation, or recovery policy is invoked and attributable.
- **Fail conditions:** Success is reported as fully evidenced or the operation
  disappears from reconciliation.

## T-11 - Key compromise or rotation

- **Minimum level:** T
- **Requirement:** PS-04
- **Procedure:** Compromise or rotate an actor-signing or transparency key.
- **Pass evidence:** Historical interpretation, revocation point, replacement
  key, notifications, and affected statements remain auditable.
- **Fail conditions:** All history becomes ambiguously valid or invalid, or the
  new key silently rewrites earlier authority.

## T-12G - Correct false history

- **Minimum level:** G
- **Requirement:** EV-04
- **Procedure:** Correct a material historical claim established as false.
- **Pass evidence:** A new linked superseding event is added and the original is
  retained.
- **Fail conditions:** Original history is overwritten or deleted.

## T-12T - Correct registered false history

- **Minimum level:** T
- **Requirements:** EV-04, CT-04
- **Procedure:** Correct a false claim already registered with the transparency
  service.
- **Pass evidence:** A new superseding statement is registered; the original
  statement and prior inclusion proof remain detectable.
- **Fail conditions:** Registration history is rewritten or old receipts stop
  being interpretable without an attributable revocation event.

## Review note

This protocol still requires independent review, executable fixture definitions,
canonical test-result schemas, and implementation-neutral reference vectors.

## Schema-profile regression checks

The schema profile must additionally demonstrate that:

- `unknown` and `not_applicable` match exactly one permitted schema branch;
- approval and grant transitions reject `unknown` and `not_applicable`;
- timestamp validation asserts both the declared lexical constraint and
  `date-time` format;
- `action` and `resource_scope` reject `not_applicable` but accept `unknown`;
- a canonical event with `truth_status` equal to `verified` requires a
  non-marker verifier identifier and nonempty decision-basis evidence;
- an outcome with `truth_status` equal to `verified` requires a non-marker
  verifier identifier, matching authenticated identity binding, declared
  verifier relationship, and nonempty criteria and evidence references; and
- validation success is not reported as proof of authenticated identity,
  receipt freshness, atomic consumption, external effect, or truth.
