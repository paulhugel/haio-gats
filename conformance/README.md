# Conformance framework

Status: **Draft, non-normative implementation guidance**

The normative conformance duties are in HAIO-GATS v0.1.0. This directory
defines a future reproducible evidence format without claiming that a system,
repository, test runner, or vendor conforms.

## Required declaration

A conformance submission should identify:

- implementation name, version, source revision, and build provenance;
- declared HAIO-GATS version and cumulative level;
- system boundary and trusted computing base;
- deployment topology and every actor role;
- Human Supervisor identity assurance method;
- authority, policy, key, storage, transparency, and custody arrangements;
- applicable event classes and excluded workflows;
- requirement-by-requirement evidence;
- every applicable test result;
- residual risks and Human Supervisor disposition; and
- independent reviewer identity and relationship where claimed.

## Proposed result vocabulary

- `pass`: required behavior and evidence were observed.
- `fail`: required behavior or evidence was absent or contradicted.
- `indeterminate`: execution completed but evidence cannot establish pass/fail.
- `not_applicable`: test is above the declared level, with the level reason.
- `not_run`: test was applicable but not performed; this is not a pass.

## Evidence package principles

1. Preserve primary records, not only summaries.
2. Bind results to implementation and policy versions.
3. Identify who executed and who reviewed each test.
4. Distinguish self-check from independent review.
5. Preserve failed, partial, interrupted, and recovery-required outcomes.
6. Minimize sensitive content and provide stable restricted-evidence references.
7. Digest artifacts using a declared canonicalization and algorithm.
8. Register Level T/A statements and retain verifiable receipts.
9. Retain independent checkpoints and recovery evidence at Level A.

## Candidate schema-profile regression checks

These checks assess this repository's non-normative schema profile; they do
not add requirements to HAIO-GATS v0.1.0 or establish implementation
conformance. The schema profile should demonstrate that:

- `unknown` and `not_applicable` match exactly one permitted schema branch;
- approval and grant transitions reject `unknown` and `not_applicable`;
- `authority_grant_id` accepts an identifier or `unknown` when its value is
  undetermined, and rejects `not_applicable`;
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

## Future fixture layout

```text
conformance/fixtures/<implementation>/<run-id>/
  declaration.json
  requirement-evidence.json
  test-results.json
  artifacts/
  receipts/
  reviewer-statement.json
  manifest.json
```

No fixture in a repository should contain production credentials, tokens,
private keys, personal data, restricted endpoints, or unredacted sensitive
evidence.

## Validation limit

Schema validation proves only that an artifact has the expected structure. It
does not prove authentic identity, current authority, correct execution,
complete capture, independent custody, statement truth, or conformance.
