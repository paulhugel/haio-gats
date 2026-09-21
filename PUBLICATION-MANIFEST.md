# Publication candidate manifest

Status: **Public read-only preview; issues and discussions disabled**

- Generated: 2026-09-20
- Repository: repository root (`.`)
- Branch: `fix/publication-readiness-v0.1.0`
- Payload files: 25
- Digest algorithm: SHA-256

## Scope and non-circularity

This manifest covers every candidate payload file except itself and excludes
all `.git/` metadata. Its own SHA-256 is reported separately after generation
to avoid a circular self-digest.

No digest establishes authorship, authority, truth, completeness, independent
verification, independent custody, publication, or conformance.

## File digests

| SHA-256 | Path |
| --- | --- |
| `83fb6029936a0f17ac0a3571367518564394798e20906d124b3ffd3cb197bd51` | `.gitignore` |
| `ce96bdcaee3cb8b8a6a140fea451d07fd269478a1369d8c560104297be46d896` | `CODE_OF_CONDUCT.md` |
| `087f7a3cfdf8f1b616a238a16e91735cdd9b801f9a39fb601cc4161c301b79b8` | `CONTRIBUTING.md` |
| `2d01d57684f8c6fc9bed1a2c1c8caf441dd48309f8527439a171e2a4992b8e27` | `GOVERNANCE.md` |
| `b12a99c13ee911790c17a3dd1f18108557b4acc0e1c1b9b8ceb5632ff4477bb1` | `LICENSE` |
| `9ce2d404cdbb6598afe37cb76009c1462f23e418e617f37134dc84db3883279e` | `LICENSE-DECISION.md` |
| `687664d9539a16ae0d384c0b5b8e582ca866de0a08ee45e13624e08fffb5ce36` | `README.md` |
| `d5ab02e27f21576e92bd7371213d060243bc76414e19606aea68e69feade64c1` | `ROADMAP.md` |
| `35efc615842032692ee8ec5448dbd5c9f2ae5299a1ce8156ed6395acf44cf23c` | `SECURITY.md` |
| `916ce8a3f1b08ef5dd44c0b94985ec1825c5f92ce676d782bd83496777a9e81a` | `architecture/custody-models.md` |
| `3b4ece5f87c266075eb8e2e7f182034e02dcf397d7a725b9e3b8bb572edfaf89` | `architecture/failure-and-reconciliation.md` |
| `8dfe0834c6cc9818997ca3a13c673dd6c3d841322208c318cbf84b87deeaa9e8` | `architecture/threat-model.md` |
| `159c886586aaf0c520ca379c0c59f95736a680ace6b288943a5aeeead0b81171` | `architecture/transparency-interface.md` |
| `d1e0cba2b6d09628e5b0e53d8a7585e5d704b3fe30de6d803fdaa3d859d55ffa` | `architecture/trust-domains.md` |
| `4ff293e3ad9f26fc76d7999156a51c77216cbbdbc73cada1d746a732932fcf98` | `conformance/README.md` |
| `e50c8d32d74c3cd07cf8b207f55961c89adbe716de28badf4fe251d9f0379539` | `conformance/T-01-through-T-12.md` |
| `10688955b17a2da5ad6afe4cb3a5e983331f72246225b1fa8a4b936f4270c6e8` | `decisions/ADR-0001-public-repository-purpose.md` |
| `19e2b93d3000113000455e51e3e05f62f4b132d52990a8ef1e5b7d2ec736a1b1` | `decisions/ADR-0002-normative-change-authority.md` |
| `e13f1ca90cc1c026ffb048907c966836e40062f3538e41e73dd2b5610e52b9f8` | `examples/non-normative/README.md` |
| `c5af1a1b3f9171d8074baa6c0249705057e095f8ef46b73584d6d9573fca1ebe` | `schemas/approval-receipt.schema.json` |
| `ff037cd20ecf4b7938b42764240b6eab145164bfa1ff43fd9fd50ba9417c7a37` | `schemas/authority-grant.schema.json` |
| `0057d212e9c138ff2281e971dbd9d9201d284496fdef6cc6c1a27e42e05e4dad` | `schemas/canonical-event.schema.json` |
| `bf6f2ca01e4c07394f4901eca5186c13892742b909e844697e901c884cba5e64` | `schemas/outcome-receipt.schema.json` |
| `a566d97bb67dc2d7e543278b2337a08ffb65a3e34837608cca35043988530457` | `spec/HAIO-GATS-v0.1.0.md` |
| `247cf6bd5d53442eb906b112ed22b6074d7d37e8a638e5293c1de30ce866fc9e` | `spec/HAIO-GATS-v0.1.0.pdf` |

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
- All four JSON files parse and compile successfully in strict Draft 2020-12
  mode with the locally available Ajv 8.6.3 validator; no dependency was
  installed.
- Focused positive and negative instance checks pass for gate binding, marker
  exclusion, timestamp validation, EV-02 action and scope semantics, identity-
  binding structure, and verified-event and verified-outcome evidence duties.
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
- The correction candidate is on local branch
  `fix/publication-readiness-v0.1.0`, derived from signed baseline commit
  `9b02a9dd286bccb08f29df3a79ed6b26fb761ba2`; it has no configured remote and
  its correction changes are uncommitted.

### Unknown or pending

- The Markdown transcription has not received independent line-by-line review
  against the deposited PDF.
- Final license, contributor-IP mechanism, maintainer assignments, code owners,
  private security-reporting channel, and normative voting rules are unresolved.
- Independent design, disclosure, security, and publication review are pending.
- No implementation, operational conformance, independent custody, or
  transparency-service integration is claimed.
