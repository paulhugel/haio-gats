# Human-Supervised AI Operations Governance and Audit Trail Specification

## A standards-aligned profile for accountable agentic workflows

- **HAIO-GATS, Version 0.1.0**
- **Author:** Paul Garrett Hugel
- **ORCID:** 0000-0001-8082-7208
- **Publication date:** 16 September 2026
- **DOI:** [10.5281/zenodo.22800642](https://doi.org/10.5281/zenodo.22800642)

> Document status: Public draft scientific specification. This document
> proposes testable requirements and an interoperability profile. It is not an
> ISO publication, a legal opinion, or a certification of conformity.

License: Creative Commons Attribution 4.0 International (CC BY 4.0).

## Markdown-edition notice

This Markdown edition was prepared from the deposited v0.1.0 PDF to support
review and machine-assisted navigation. The unchanged PDF in this directory
and the Zenodo deposit are the authoritative v0.1.0 publication. Any
transcription discrepancy must be corrected in a new reviewed revision; it
must not silently change the deposited version.

## Abstract

Autonomous and semi-autonomous artificial intelligence systems can perform
consequential work across multiple tools, repositories, services, and
organizational roles. Existing governance frameworks establish valuable
expectations for accountability, human oversight, risk management, logging,
and provenance, but they do not collectively define an event-level control and
evidence protocol for human-supervised agentic operations.

This specification defines a testable profile in which a designated Human
Supervisor retains effective operational control; every human and software
actor operates under bounded authority; consequential actions pass explicit
approval gates; and material events produce authenticated, append-only,
independently verifiable provenance records. It maps organizational controls
to ISO/IEC 42001:2023, ISO/IEC 38507:2022, ISO/IEC 42005:2025, and the NIST AI
Risk Management Framework; human oversight and logging to Articles 12 and 14
of Regulation (EU) 2024/1689; provenance to W3C PROV; separation of duties to
NIST SP 800-53; and cryptographic transparency to RFC 9943 and RFC 9942.

Internal hash consistency does not establish actor identity, authorization,
statement accuracy, or independent custody. HAIO-GATS is a research and
implementation baseline for accountable AI operations, standards development,
conformity assessment, and empirical evaluation.

## 1. Scope

This specification defines governance, control, evidence, and conformance
requirements for an AI operations system in which one or more AI agents perform
work under the authority and effective supervision of a natural person. It
applies to workflows that can read, create, modify, promote, publish, deploy,
transmit, or delete digital artifacts or change external system state.

It covers:

- accountable human supervision and intervention;
- authenticated actor identity and bounded delegation;
- explicit authority and approval gates;
- separation of execution, verification, and promotion roles;
- event-level provenance and evidence records;
- append-only, non-equivocating, cryptographically verifiable registration;
- confidentiality, retention, recovery, and independent custody; and
- reproducible conformance tests.

It does not define model training methods, model capability evaluations,
general AI safety cases, or a universal legal-compliance program.

## 2. Research basis and design problem

Ordinary application logs are often mutable, incomplete, self-attributed, and
controlled by the system whose conduct they describe. An attacker controlling
both a record and its self-derived checkpoint can rewrite and rechain history.
A valid signature identifies control of a signing key; it does not prove that
the signer possessed authority, that a statement was accurate, or that a
qualified person independently verified the outcome.

HAIO-GATS treats accountability evidence as a composed property:

```text
authenticated identity + current authority + recorded human decision
+ attributable action + preserved evidence + independent verification
+ independently checkable registration
```

The Human Supervisor is part of the control path before and during
consequential execution, rather than an observer reviewing a narrative after
the action.

## 3. Normative language and conformance

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**
are to be interpreted as described in BCP 14 when they appear in bold
uppercase.

A conforming implementation **MUST** declare the requirements and conformance
level it satisfies, publish requirement-by-requirement evidence for every
applicable normative requirement, and publish evidence from every test whose
minimum level is at or below its declared level. Tests above that level **MUST**
be reported as `not_applicable` with the level-based reason.

### 3.1 Cumulative levels

- **Level G - Governed:** HS-01 through HS-06; AU-01 through AU-05; ID-01
  through ID-04; EV-01 through EV-06; PS-01 through PS-03; RC-01 through
  RC-03.
- **Level T - Transparent:** Level G plus CT-01 through CT-05, CT-07, and
  PS-04.
- **Level A - Assured:** Level T plus ID-05, CT-06, and RC-04.

Normative duties in the system model, threat model, and operational state model
apply from Level G unless they assign a higher level.

## 4. System model

### 4.1 Actors and components

| Role or component | Definition |
| --- | --- |
| Human Supervisor | Designated natural person who owns the operation, grants or denies authority, makes required go/no-go decisions, monitors execution, and can interrupt or halt the system. |
| AI Agent | Software agent that proposes or performs work only within a current authority grant. |
| Executor | Human or software agent that performs an authorized mutation or external action. |
| Verifier | Actor that evaluates the result and primary evidence against stated acceptance criteria. |
| Committer or Publisher | Actor that promotes an artifact or state through a separately authorized commit, merge, deployment, transmission, or publication gate. |
| Policy Decision Point | Component determining whether actor, action, resource, and context satisfy authority and approval policy. |
| Transparency Service | Service that authenticates signed statements, applies a transparent registration policy, records accepted statements in a verifiable data structure, and issues receipts. |
| Auditor | Independent relying party that validates receipts, replays evidence, checks consistency, and evaluates conformance. |

### 4.2 Threat model

The implementation **MUST** address unauthorized scope expansion; ambiguous or
replayed approvals; false actor attribution; compromised credentials; role
substitution; executor self-verification; event omission, alteration,
reordering, deletion, or rechaining; split views; signing-key or transparency-
key compromise; privacy leakage; partial writes and interrupted publication;
and recovery from stale or inconsistent backups.

At its declared level, an implementation **MUST** mitigate each threat or state
it as a residual risk, explain the absent higher-level control, and record the
Human Supervisor's explicit acceptance or rejection. It **MUST** declare its
trusted computing base and residual risks. It **MUST NOT** claim `tamper-proof`
or `immutable` without demonstrating the relevant assumptions and enforcement.
`Tamper-evident` is preferred when alteration can be detected but not prevented.

## 5. Normative requirements

### 5.1 Human supervisory control

**HS-01 Designation.** Before an AI agent receives operational authority, the
operation **MUST** identify exactly one accountable Human Supervisor and record
the supervisor's authenticated identifier.

**HS-02 Informed decision.** Before consequential approval, the supervisor
**MUST** receive the proposed action, purpose, affected resources, requested
authority, expected outcome, material risks, available evidence, acceptance
criteria, and rollback or containment procedure.

**HS-03 Effective control.** The supervisor **MUST** be able to approve, reject,
constrain, pause, interrupt, override, reverse where technically possible, and
safely halt an operation through a path not dependent on voluntary cooperation
from the acting AI agent. The implementation **MUST** declare maximum halt
latency per operation or risk class and define the response when exceeded.

**HS-04 Monitoring.** The system **MUST** show active actors, current authority,
pending approvals, completed actions, exceptions, failed registrations, scope
consumption, and emergency-stop status with risk-appropriate bounded delay.

**HS-05 Automation bias.** The interface **SHOULD** present model uncertainty,
conflicting evidence, verification status, and known limitations in a form
helping the supervisor avoid automatic reliance on AI output.

**HS-06 Supervisory record.** Each approval, denial, constraint, override,
intervention, and halt **MUST** be recorded as a distinct event attributed to
the supervisor. Absence of required approval **MUST** result in denial.

### 5.2 Authority and approval

**AU-01 Authority grant.** Every grant **MUST** state its identifier, grantor,
grantee, role, permitted actions, resource scope, constraints, effective time,
expiration or terminal condition, required evidence, approval gates, and
explicitly prohibited actions.

**AU-02 Binding.** A grant **MUST** bind to the actor's authenticated identity
and operation identifier. Authority **MUST** fail closed when missing, expired,
revoked, ambiguous, or inconsistent with higher-priority policy.

**AU-03 Least authority.** Action and resource scope **MUST** be no broader than
needed. Discovery or read authority **MUST NOT** imply mutation authority.

**AU-04 Distinct gates.** The implementation **MUST** define separate gates for
mutation, commit or promotion, publication or deployment, destructive action,
material scope expansion, and residual-risk acceptance. Approval at one gate
**MUST NOT** imply approval at another.

**AU-05 Scope drift.** The operation **MUST** stop and request a new human
decision when action, resource, actor, risk, or expected effect falls outside
the current grant.

### 5.3 Identity, delegation, and role separation

**ID-01 Authenticated identity.** Every human, AI agent, service, and delegated
process **MUST** have an authenticated identifier bound to its audit statements.
A display name or self-asserted label is insufficient.

**ID-02 Delegation.** Delegation **MUST** identify delegator, receiving actor,
role, authority grant, operation, time bounds, and revocation status. Delegated
authority **MUST NOT** exceed the delegator's authority.

**ID-03 Role separation.** Consequential operations **SHOULD** use distinct
actors for execution, verification, and commitment or publication. Permitted
overlap **MUST** record justification, risk acceptance, compensating controls,
and approving supervisor.

**ID-04 Verification representation.** An executor's self-check, generated
summary, test run, signature, or hash **MUST NOT** be represented as independent
verification. Every verification result **MUST** identify the verifier,
relationship to the executor, criteria, and evidence examined.

**ID-05 Independent verification.** At Level A, an independent verifier
**MUST** examine the resulting artifact and primary evidence against explicit
acceptance criteria.

### 5.4 Event and provenance model

**EV-01 Automatic capture.** The system **MUST** automatically record material
proposals, authority decisions, approvals, denials, actions, tool invocations,
mutations, exceptions, escalations, verification results, promotions,
publications, overrides, reversals, recovery actions, and halt events.

**EV-02 Minimum record.** Every material record **MUST** contain every field in
the minimum schema below. Applicable but undetermined values **MUST** be
`unknown`, not omitted or `not_applicable`. The implementation's schema profile
**MUST** enumerate permitted `not_applicable` conditions.

| Field | Meaning |
| --- | --- |
| `event_id` | Globally unique event identifier. |
| `operation_id` | Identifier joining one governed operation. |
| `event_type` | Controlled event classification. |
| `recorded_at` | Trusted or qualified timestamp and stated clock source. |
| `actor_id`, `actor_type` | Authenticated actor and type. |
| `role` | Actor role in the event. |
| `human_supervisor_id` | Accountable natural person. |
| `authority_grant_id` | Grant evaluated for the action. |
| `policy_id`, `policy_version` | Operational or registration policy applied. |
| `action`, `resource_scope` | Action and affected resources. |
| `input_refs`, `output_refs` | Stable identifiers and digests. |
| `decision`, `decision_basis` | Decision and referenced evidence or criteria. |
| `truth_status` | Verified, inferred, hypothesis, unknown, stale, or superseded. |
| `prior_event_id` | Logical predecessor. |
| `verifier_id` | Independent verifier when required. |
| `supersedes_event_id` | Earlier record corrected or made stale. |
| `statement_id`, `receipt_ref` | Signed statement and transparency receipt. |
| `confidentiality`, `retention` | Access class and retention rule. |

At Level G, `statement_id` and `receipt_ref` may be `not_applicable`. At Levels
G and T, `verifier_id` may be `not_applicable` only when independent
verification is not required. Event-type exceptions are limited to semantically
inapplicable input/output, decision, predecessor, and supersession fields.

**EV-03 Provenance relations.** The implementation **SHOULD** represent people,
software agents, activities, entities, delegation, association, attribution,
use, generation, derivation, role, and plan using W3C PROV or a documented
lossless mapping.

**EV-04 Truth status.** Material claims **MUST** carry a controlled evidence
status distinguishing at least verified observation, inference, hypothesis,
and unknown. Historical records no longer current **SHOULD** be superseded by a
new event rather than rewritten.

**EV-05 Evidence linkage.** A record describing an artifact or external state
**MUST** contain a stable identifier and, where appropriate, a cryptographic
digest or externally verifiable reference.

**EV-06 Duplicate submission handling.** Approval and action submissions
**MUST** carry stable identifiers. Repetition of the same identifier and
content **MUST** produce at most one external effect and a deterministic replay.
Reuse with different content **MUST** fail closed and produce an attributable
conflict event.

### 5.5 Cryptographic transparency and custody

**CT-01 Signed statement.** Each consequential event **MUST** produce an
authenticated signed statement whose protected metadata binds issuer identity,
subject, statement type, and content or content digest.

**CT-02 Registration policy.** A Transparency Service **MUST** authenticate the
issuer, apply the current registration policy, record an accepted statement in
a verifiable data structure, and issue a receipt proving inclusion.

**CT-03 Reproducibility.** The service **MUST** retain or make available enough
information to reproduce registration checks, including statement, policy,
trust anchors, and required collateral.

**CT-04 Append-only history.** Accepted statements **MUST** form an append-only
sequence. Correction, revocation, or status change **MUST** use a new linked
statement. Accepted history **MUST NOT** be silently changed, deleted, or
reordered.

**CT-05 Non-equivocation.** Level T and A implementations **MUST** provide
evidence that relying parties observe a consistent history and declare the
verifiable data structure and receipt profile.

**CT-06 Independent custody.** At Level A, checkpoints or statements **MUST**
be held by at least one independently controlled transparency service or
custodian. A head digest controlled by the event-log authority is insufficient.

**CT-07 Evidence limits.** Validation **MUST** distinguish signature validity,
issuer authentication, policy acceptance, inclusion, consistency, checkpoint
custody, statement accuracy, actor authority, and independent verification.
Success in one category **MUST NOT** be reported as success in another.

### 5.6 Privacy, security, and disclosure

**PS-01 Data minimization.** Records **MUST** contain only information necessary
for accountability, verification, risk management, and applicable obligations.
Secrets, tokens, and unnecessary personal data **MUST NOT** appear in statement
payloads.

**PS-02 Separated views.** Sensitive provenance receipts and evidence **MUST**
be access controlled and logically separate from sanitized disclosure records.
A sanitized record **MUST** preserve stable references for authorized evidence.

**PS-03 Access accountability.** Access to sensitive evidence, policy
administration, trust-anchor changes, and key management **MUST** itself be
logged and subject to separation of duties.

**PS-04 Key compromise.** The implementation **MUST** define detection,
notification, revocation, historical interpretation, recovery, and reissuance
for compromised actor and transparency-service keys.

### 5.7 Continuity and recovery

**RC-01 Retention.** Retention **MUST** be defined by event class, purpose,
legal obligation, confidentiality, and recovery need. Expiration and lawful
deletion **MUST** be recorded without falsifying earlier inclusion evidence.

**RC-02 Durable publication.** At Level G, the implementation **MUST** define
event-storage atomicity and action-success/event-failure states. At Levels T
and A, it **MUST** additionally define checkpoint-publication and receipt-return
failure states.

**RC-03 Backup and restore.** At Level G, procedures **MUST** preserve event
order and policies. At Levels T and A, they **MUST** also preserve signed-
statement order, receipts, trust anchors, and key history. At Level A, they
**MUST** preserve independent checkpoints, exercise restoration, and retain
test evidence.

**RC-04 Post-recovery reconciliation.** After recovery, an independent actor
**MUST** compare restored state with independently held checkpoints or
transparency evidence before normal operation resumes.

## 6. Operational state model

```text
PROPOSED -> SCOPED -> AUTHORIZED -> EXECUTING -> EVIDENCED
-> VERIFIED -> PROMOTION-AUTHORIZED -> PROMOTED -> REVERIFIED -> CLOSED
```

At Levels G and T, `VERIFIED` means a verification result was recorded against
explicit criteria with the verifier identity and relationship declared; it
does not itself mean independent verification. At Level A, `VERIFIED` also
requires ID-05. Any state must be able to transition to `PAUSED`, `DENIED`,
`FAILED`, `HALTED`, or `RECOVERY REQUIRED`. A transition **MUST** identify its
actor, authority, evidence, and human decision. Later-state authorization
**MUST NOT** be inferred from an earlier state.

## 7. Conformance tests

| Test | Level | Requirements | Procedure | Required evidence |
| --- | --- | --- | --- | --- |
| T-01 | G | HS-01, HS-06, AU-04 | Attempt consequential action without designated supervisor or approval. | Denial plus policy and attributed denial events. |
| T-02 | G | AU-02, AU-05 | Request action outside an otherwise valid grant. | Scope drift detected, execution stopped, new decision requested. |
| T-03 | G | HS-03, HS-06 | Invoke authenticated halt during execution and measure safe-state latency. | Bound met, safe state entered, intervention attributed. |
| T-04 | G | EV-06 | Duplicate identical submission, then reuse identifier with different content. | At most one effect; deterministic replay; conflict fails closed. |
| T-05 | G | ID-04 | Executor submits its own verification. | Result labeled self-check, not independent verification. |
| T-06 | T; A adds CT-06 | CT-04, CT-05, CT-06 | Alter, delete, reorder, or rechain history. | T: receipt or consistency check detects; A: independent checkpoint also detects. |
| T-07G | G | AU-02 | Present expired grant, revoked credential, or stale authorization policy. | Fail-closed denial with attributable reason. |
| T-07T | T | CT-02 | Present forged issuer or stale registration policy. | Registration fails closed with attributable reason. |
| T-08 | G | PS-01, PS-02 | Expose sanitized view to unauthorized reader. | Accountability fields remain; secrets and sensitive evidence do not. |
| T-09 | A | CT-06, RC-03, RC-04 | Restore backup behind independently anchored events. | Divergence detected and reconciliation required. |
| T-10 | T | RC-02 | Simulate action success followed by registration failure. | Inconsistent state exposed; containment or recovery invoked. |
| T-11 | T | PS-04 | Compromise or rotate issuer or transparency key. | Historical validity, revocation point, replacement, and notifications auditable. |
| T-12G | G | EV-04 | Correct false historical claim. | Linked superseding event; original retained. |
| T-12T | T | EV-04, CT-04 | Correct registered false claim. | New registered statement; original and inclusion proof detectable. |

## 8. Standards crosswalk

| Domain | Reference | Relationship and limitation |
| --- | --- | --- |
| Management system | ISO/IEC 42001:2023 | Organizational AI-management umbrella; HAIO-GATS adds event-level controls. |
| Governance | ISO/IEC 38507:2022 | Governing-body responsibility; HAIO-GATS operationalizes supervision and evidence. |
| Impact assessment | ISO/IEC 42005:2025 | Lifecycle impact assessment; events can preserve decisions and control changes. |
| Risk management | ISO/IEC 23894:2023; NIST AI RMF 1.0 | Risk-based governance and oversight; not an event protocol. |
| Human oversight | EU Regulation 2024/1689 Article 14 | Effective oversight, intervention, reversal, and stopping; applicability is contextual. |
| Automatic logging | EU Regulation 2024/1689 Article 12 | Event recording and traceability for high-risk AI; HAIO-GATS is broader. |
| Provenance | W3C PROV-DM and PROV-O | Interoperable provenance semantics; no guarantee of truth, authority, or immutability. |
| Separation of duties | NIST SP 800-53 Rev. 5 AC-5 | Distinct access roles; applied here to executor, verifier, and publisher. |
| Audit content | NIST SP 800-53 Rev. 5 AU family | Event selection, content, review, retention, timestamps, and protection. |
| Transparency | RFC 9943 and RFC 9942 | Signed statements, registration, receipts, append-only evidence, and non-equivocation. |
| Merkle transparency | RFC 9162 | Append-only log and consistency-proof design; no semantic truth or authority. |
| Canonical JSON | RFC 8785 | Deterministic JSON representation; no custody or authenticity by itself. |
| Trusted time | RFC 3161 | Independent timestamp tokens; no proof of event truth. |

## 9. Scientific claims and limitations

### 9.1 Testable claims

HAIO-GATS supports testing whether explicit authority objects reduce ambiguous
delegation; effective supervisor controls reduce containment time; role
separation improves detection of unsupported completion claims; signed
statements plus independently controlled transparency improve detection of
rewriting and equivocation; and structured events reduce reconstruction cost.

Implementations should report authorization false-accept and false-reject
rates, intervention latency, missing-event rate, registration latency and
failure rate, recovery divergence, verifier disagreement, and reconstruction
time.

### 9.2 Limitations

Recording does not make AI behavior safe. Authorized people may sign false
statements; identity systems may be compromised; supervisors may misunderstand
systems or approve harmful actions; and collusion may defeat separation.
Cryptographic transparency improves detectability and accountability but does
not establish accuracy, completeness, legality, or ethical acceptability.

The profile adds operational cost, storage, privacy, key-management, and
latency burdens. Formal security analysis, supervisor-interface usability
studies, and independent evaluation across real workflows remain future work.

## 10. Ethics, privacy, and responsible use

Audit infrastructure can become surveillance infrastructure. Implementers
should assess impact, minimize data, separate public and restricted evidence,
protect privileged material and whistleblowers, support contest and correction,
and publish retention and access rules. Nominal responsibility without
competence, time, authority, and usable controls does not satisfy HAIO-GATS.

## 11. Conclusion

HAIO-GATS defines a standards-aligned scientific specification for accountable
AI operations. Its central requirement is effective human supervisory control
supported by bounded authority, lifecycle gates, authenticated provenance,
independent verification, and independently checkable evidence. Governance and
cryptography are complementary layers with distinct claims and limits.

## Declarations

- **Author contribution:** Paul Garrett Hugel conceived the specification and
  is the sole named author.
- **Funding:** No specific funding was received.
- **Competing interests:** The author declares no competing interests.
- **Data and code availability:** No empirical dataset or executable reference
  implementation accompanies v0.1.0.
- **License:** CC BY 4.0.
- **Versioning:** Material corrections should be new versions; earlier deposited
  versions should remain available and linked through Zenodo.

During preparation, the author used OpenAI Codex for structured drafting,
editorial revision, document production, and standards research, and Anthropic
Claude for pre-publication review and citation validation. The author reviewed
and edited the content, retained final decisions, and takes responsibility.
Neither AI system is an author.

## References

1. ISO/IEC 42001:2023, Artificial intelligence management system.
2. ISO/IEC 38507:2022, Governance implications of organizational AI use.
3. ISO/IEC 42005:2025, AI system impact assessment.
4. ISO/IEC 23894:2023, Guidance on AI risk management.
5. NIST AI 100-1, Artificial Intelligence Risk Management Framework 1.0.
6. NIST SP 800-53 Rev. 5, Security and Privacy Controls.
7. Regulation (EU) 2024/1689, Articles 12 and 14.
8. W3C PROV-DM.
9. W3C PROV-O.
10. RFC 9943, Architecture for Trustworthy and Transparent Digital Supply Chains.
11. RFC 9942, COSE Receipts.
12. RFC 9162, Certificate Transparency Version 2.0.
13. RFC 8785, JSON Canonicalization Scheme.
14. RFC 3161, Time-Stamp Protocol.
15. RFC 2119, Requirement-level key words.
16. RFC 8174, Uppercase and lowercase requirement words.
17. Schneier and Kelsey (1999), Secure audit logs for computer forensics.
18. Ma and Tsudik (2009), A new approach to secure logging.
19. Haber and Stornetta (1991), How to time-stamp a digital document.
20. Chan et al. (2024), Visibility into AI agents.
21. Parasuraman, Sheridan, and Wickens (2000), Types and levels of human interaction with automation.
22. Saltzer and Schroeder (1975), Protection of information in computer systems.
23. Parasuraman and Manzey (2010), Complacency and automation bias.
24. Elish (2019), Moral crumple zones.
25. Green (2022), Human oversight of government algorithms.
26. Sharif (2026), Agent Audit Trail, Internet-Draft draft-sharif-agent-audit-trail-04.

Complete bibliographic entries and links appear in the authoritative PDF.

## Change record

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-09-16 | Initial public draft defining human supervision, bounded authority, event provenance, cryptographic transparency, independent custody, and conformance tests. |
