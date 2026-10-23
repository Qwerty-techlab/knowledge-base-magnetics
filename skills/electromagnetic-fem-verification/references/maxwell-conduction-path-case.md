# Maxwell conduction-path verification case

This reference records reusable evidence from a physical multi-branch winding case. It is a failure-analysis reference, not a recommended final excitation architecture.

## Observed evidence chain

1. A presolve model contained 12 continuous physical cable paths joined by common input/output buses.
2. `ValidateDesign=1` before mesh, after mesh, and before `Analyze`.
3. The validation log reported conduction-path success and the API returned one expected path containing the winding network.
4. Initial meshing completed normally with 1,475,260 tetrahedra.
5. `Analyze` stopped before a Pass 1 field state with:

   `The winding ... has no conduction path. It could potentially be a mesh issue.`

6. A destructive `Separate Bodies` probe on a temporary duplicate returned one CAD solid component, ruling out gross CAD disconnection.
7. Available RAM remained about 17 GiB at failure, ruling out memory exhaustion.

Conclusion: presolve conduction validation and CAD connected-component checks did not prove tetrahedral current-path viability.

## Diagnostic probes and what they establish

### Separate Bodies on a temporary duplicate

Use only on an isolated duplicate because it destructively modifies geometry.

Persist:

- source volume;
- connected-component count;
- per-component volume, face count, and bounding box;
- summed-volume delta.

A single component proves gross CAD connectivity only. It does not prove a mesh-level conduction path.

### Remove common buses, then separate

Subtract exact bus volumes on a temporary duplicate and separate the remaining winding. In the observed case this yielded exactly 12 continuous cable solids, each with the expected envelope. This is useful evidence for subsequent excitation redesign, but it is not itself a validated solver method.

### `Solve Inside=False`

With face Coil Terminals in this Maxwell 2024 R2 case, disabling `Solve Inside` caused validation errors stating that the terminals were not on valid conductor cross-sections. Do not assume surface-only winding excitation is a drop-in repair; presolve it independently.

### One Current section per open cable

A prior 12-source variant passed conduction validation but failed in Pass 1 with `Current leak to the air`. One source on an open conductor did not define a closed current path.

### Paired internal Current terminals

Paired Current terminals on cable ends were rejected when their faces did not border the outer problem region. Verify terminal classification and region contact explicitly.

### Paired Coil Terminals on separate cable bodies

Separating a united winding into its physical cable branches can expose the expected path count while still failing the excitation gate. In the observed 12-cable probe, Maxwell generated exactly 12 conduction paths—one per continuous 20-turn cable—and reported no current leak, but rejected all 24 paired Coil Terminals because their end faces were internal to the air region.

This is useful connectivity evidence, not a working topology. Before copying the pattern across every branch, use a **single-branch tracer probe**:

1. duplicate the rejected presolve design;
2. keep one cable only;
3. copy each real cable end face and sweep it to an exact outer Region boundary;
4. unite each extension with the cable;
5. resolve the new terminal faces by position and numerically assert their centers lie on the Region boundary;
6. assign the paired terminals and one winding;
7. run only `ValidateDesign`, Message Manager, and conduction-path inspection—no mesh or `Analyze`;
8. expand to all branches only if this probe passes.

Do not record the sweep-to-region method as solver-valid until the tracer probe and a subsequent solve both pass.

### Cleaning an inherited Maxwell design before a tracer probe

A duplicated Maxwell design can expose Matrix, Winding Group, and Coil Terminal objects together through PyAEDT's boundary collection even though AEDT owns them in different modules. Before destructive edits:

1. inventory each inherited object's `name`, `type`, and parent relationship;
2. delete the Matrix through `MaxwellParameterSetup`;
3. delete the parent Winding Group through `BoundarySetup`;
4. delete child Coil Terminals through `BoundarySetup`;
5. refresh PyAEDT's cached boundary view and verify the expected objects are absent;
6. only then modify conductor geometry.

Do not treat failure during this cleanup as evidence against the proposed conductor extension. Persist the exception stage and classify it as automation/API failure because the physical probe has not yet run. Add a contract test that locks the dependency order before retrying the CAD probe.

## Profile interpretation

A reliable profile distinguished stages:

- `Initial Meshing` ended with `Normal Completion`;
- `Adaptive Meshing / Pass 1` contained no solver state;
- the final profile item carried the conduction-path error;
- stop status was `Error`.

The wrapper also emitted a generic elapsed-time line saying the setup was solved correctly after logging an error. Therefore never use that generic line as success evidence.

## Durable rules

- Capture Message Manager immediately after `Analyze`; clearing it first can erase the root cause.
- Read the persisted solver profile on every failed solve.
- Do not rerun an unchanged long model after mesh-dependent conduction failure.
- Do not label a proposed topology as working until both presolve and solve gates pass.
- Keep analytical methodology provisional until comparable converged FEM or measurement exists.
