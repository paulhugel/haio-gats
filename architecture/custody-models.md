# Custody models

Status: **Draft, non-normative alternatives analysis**

## Objective

Define viable ways to satisfy HAIO-GATS CT-06 without treating a self-held
digest as independent custody. No model is selected by this document.

## Model A - Independent transparency service

Signed events are registered with a separately controlled service that returns
inclusion and consistency receipts.

- **Strengths:** direct Level T alignment; public or multi-party verification;
  explicit registration policy.
- **Risks:** metadata exposure, service availability, split views, policy drift,
  and concentration of trust.
- **Level A condition:** control and administration must be genuinely independent
  from executor and ledger operator, with independent retrieval.

## Model B - Dual transparency services

Each consequential statement or checkpoint is registered with two independently
controlled services.

- **Strengths:** improved equivocation and availability resilience.
- **Risks:** correlation of providers, increased latency and cost, complex
  reconciliation when one service rejects or lags.
- **Open question:** whether both registrations are fail-closed for every event
  class or whether one can enter a recorded degraded state.

## Model C - Independent evidence custodian

An external custodian receives signed statements, receipts, policies, trust
anchors, and checkpoints under retention and retrieval rules.

- **Strengths:** can preserve restricted evidence that should not enter a public
  log; can support recovery exercises.
- **Risks:** custodian administrator compromise, proprietary export formats,
  legal-jurisdiction issues, and unverifiable deletion or retention claims.
- **Requirement:** custody must preserve verifiability, not merely backup bytes.

## Model D - Public timestamp or ledger anchor

A digest or Merkle root is anchored in an independently observable timestamp or
public ledger.

- **Strengths:** evidence that a commitment existed before a time.
- **Risks:** does not establish identity, authority, completeness, inclusion of a
  particular private event without proof, or non-equivocation between anchors.
- **Conclusion:** useful supplemental evidence, insufficient alone for CT-06.

## Model E - Organizational witness quorum

Multiple independent witnesses retain and co-sign checkpoints and consistency
observations.

- **Strengths:** governance can be distributed among stakeholders.
- **Risks:** witness availability, collusion, inconsistent software, membership
  changes, and threshold-key recovery.
- **Requirement:** membership, quorum, key lifecycle, and dispute handling must
  be versioned and auditable.

## Selection criteria

| Criterion | Question |
| --- | --- |
| Control independence | Can executor or ledger administrators rewrite or delete the retained evidence? |
| Retrieval independence | Can an auditor obtain evidence without the system under review? |
| Non-equivocation | How are inconsistent histories detected and shared? |
| Confidentiality | Can restricted evidence be committed without disclosure? |
| Recovery | Can custody evidence detect stale restoration before resume? |
| Key lifecycle | Are rotation, revocation, compromise, and historical interpretation supported? |
| Portability | Are statements and receipts independently parseable and exportable? |
| Availability | What happens when the custodian is unreachable? |
| Jurisdiction | Which legal, retention, and disclosure regimes apply? |
| Sustainability | Who pays, governs, and succeeds the custodian? |

## Decision still required

Select named operators only after evaluating their administrative control,
contracts, key custody, export formats, outage behavior, privacy exposure,
monitoring, and independent recovery process. Product branding or external
hosting alone is not evidence of independence.
