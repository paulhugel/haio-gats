# Publication candidate manifest

Status: **Public preview; Issues open to invited contributors; Discussions disabled**

- Snapshot generated: 2026-09-20
- Repository: repository root (`.`)
- Snapshot branch: `fix/publication-readiness-v0.1.0`
- Historical payload files: 26

## Scope and non-circularity

This manifest records the candidate's scope, provenance, and validation
evidence. It covers every candidate payload file except itself and excludes
all `.git/` metadata. The retired digest table described the 2026-09-20
snapshot; it does not describe files after subsequent edits and remains
recoverable from Git history.

Current repository-content integrity is referenced through the
content-addressed Git history and its signed commit records. This reference
does not replace an independent custody or transparency service.

No Git digest or signature establishes authorship, authority, truth,
completeness, independent verification, independent custody, publication, or
conformance.

## Retired digest table

The SHA-256 payload-digest table for the 2026-09-20 snapshot is retired. It
was appropriate to an uncommitted correction candidate with no configured
remote; it became stale after later repository commits. The historical table
remains recoverable from Git history and is not regenerated as a current-state
record.

## Validation record

### Verified

- The PDF payload remains byte-for-byte identical to the deposited v0.1.0
  baseline identified by DOI `10.5281/zenodo.22800642`.
- The Markdown edition is an explicit correction candidate and intentionally
  differs from the deposited PDF as disclosed in its correction-candidate
  notice; the PDF remains authoritative pending a separate publication
  decision.
- The PDF has 19 physical pages and renders legibly in inspected pages 1, 6,
  10, and 19.
- Requirement identifiers in the Markdown edition match the identifiers
  extracted from the PDF.
- Conformance-test identifiers in the protocol match those extracted from the
  PDF.
- Local Markdown link targets resolve.
- The external DOI resolves.
- Three Mermaid blocks render with Mermaid CLI 11.17.0; generated validation
  artifacts are stored only under `/tmp`.
- Markdown text passes the candidate's ASCII-only check.
- A basic secret-pattern scan found no candidate credential material.
- At the 2026-09-20 snapshot, the correction candidate was on local branch
  `fix/publication-readiness-v0.1.0`, derived from signed baseline commit
  `9b02a9dd286bccb08f29df3a79ed6b26fb761ba2`; the snapshot recorded no
  configured remote and uncommitted correction changes. These are historical
  checkout facts, not current remote or worktree claims.

### Unknown or pending

- A Draft 2020-12 meta-schema validation of the four JSON schemas was recorded
  at publication as passing under Ajv 8.6.3. The invocation, script, and output
  were not retained, and no validator is configured in this repository. The
  result is therefore not independently reproducible and should be re-
  established before any conformance claim depends on it.
- Focused positive and negative instance checks were recorded as performed
  against the schema profile covering gate binding, marker exclusion, timestamp
  validation, EV-02 action and scope semantics, identity-binding structure, and
  verified-event and verified-outcome evidence duties. The fixtures and
  invocation were not retained, so this result is not independently
  reproducible and should be re-established before any conformance claim
  depends on it.
- The Markdown transcription has not received independent line-by-line review
  against the deposited PDF.
- Contributor-IP mechanism, maintainer assignments, code owners, security
  response and coordinated-disclosure procedures, and normative voting rules
  are unresolved. GitHub Private Vulnerability Reporting is enabled; channel
  availability does not settle those procedures.
- Independent design, disclosure, security, and publication review are pending.
- No implementation, operational conformance, independent custody, or
  transparency-service integration is claimed.
