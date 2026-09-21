# Roadmap

This roadmap is non-normative. Each phase requires evidence review and a new
Human Supervisor authorization; completion does not authorize promotion.

## Phase 0 - Decision package and public specification foundation

- Review the v0.1.0 Markdown transcription against the deposited PDF.
- Resolve licensing and contributor-IP terms.
- Accept or amend the event contract, trust domains, custody alternatives,
  failure semantics, privacy model, key lifecycle, and conformance criteria.
- Obtain independent design and disclosure review.
- Decide whether to create and publish a remote repository.

Honest claim: the design basis is explicit and reviewable; no operational
audit-trail capability is claimed.

## Phase 1 - Read-only shadow evaluation

- Inventory capture surfaces and bypass paths.
- Evaluate historical or secret-free proposals without side effects.
- If TypeSafe/Jev is tested, retain its typed inputs, scores, confidence,
  abstentions, and Human Supervisor disposition as advisory evidence only.
- Measure capture coverage, calibration, override rate, and required-stop false
  negatives.

## Phase 2 - Bounded Level G vertical slice

- Select one reversible or containable workflow.
- Bind authenticated human authorization to an exact action.
- Record durable pre- and post-action events.
- Test denial, scope drift, duplicate submission, crash, retry, privacy,
  restart retrieval, halt latency, and self-verification labeling.

## Phase 3 - Level T transparency

- Register signed canonical events with an independently operated transparency
  service.
- Validate inclusion and consistency receipts.
- Test split-view detection, key rotation, key compromise, registration failure,
  and action-success/receipt-failure handling.

## Phase 4 - Level A assurance

- Establish independent custody and verifier roles.
- Exercise restoration and post-recovery reconciliation.
- Test collusion assumptions and recurring conformance evidence.
- Require separate authorization for each workflow, actor, event class, and
  deployment expansion.
