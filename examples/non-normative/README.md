# Non-normative examples

This directory holds illustrative event sequences, schema instances, interoperability examples, and visual explanations. Examples do not create requirements, establish secure defaults, demonstrate conformance, or authorize operational use. The deposited [`v0.1.0 PDF`](../../spec/HAIO-GATS-v0.1.0.pdf) is authoritative.

Each example must identify:

- the specification version and requirements illustrated;
- whether actors, keys, resources, and evidence are synthetic;
- omitted controls and residual risks;
- the expected validation result; and
- the distinction between self-check and independent verification.

## X3D visual explorer

- [Open the live interactive explorer](https://paulhugel.github.io/haio-gats/examples/non-normative/haio-gats-x3d-explorer.html)
- [View the HTML source](haio-gats-x3d-explorer.html) and [standalone X3D scene](haio-gats-cycle.x3d)

**Specification scope:** v0.1.0 lifecycle material in PDF §§5–7, the 37 control identifiers, the 25 illustrated EV-02 event-field names, and 14 conformance test entries. Labels and descriptions are educational paraphrases; consult the PDF for exact wording and conditions.

**Data status:** No live operation, actor, key, resource, evidence artifact, or event value is represented. The geometry and examples are illustrative; no personal or restricted operational data is included.

**Omissions and residual risks:** This static viewer does not enforce human approval, authority scope, halt, identity, evidence capture, cryptographic registration, independent custody, recovery, or any conformance rule. The visual position of a parameter does not mean it applies only at that lifecycle stage. Simplified labels can omit conditions in the PDF. The 3D renderer loads pinned X_ITE from a public CDN; if unavailable, the text catalog remains usable.

**Expected validation result:** HTML loads as a read-only reference, the X3D scene contains 10 normal-state blocks, 5 exception blocks, and 76 parameter blocks, and a visitor can navigate from PROPOSED through CLOSED. Structural checks and browser interaction checks are self-checks of the illustration, not operational or conformance tests.

**Verification boundary:** No independent verifier has reviewed this example. A successful browser check, file hash, or Pages deployment must not be described as independent verification or HAIO-GATS conformance.
