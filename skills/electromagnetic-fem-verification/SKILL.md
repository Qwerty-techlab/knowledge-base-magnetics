---
name: electromagnetic-fem-verification
description: "Verify long EM FEM runs with staged evidence gates."
version: 0.2.0
author: Kirill Chefonov, Hermes Agent
license: MIT
platforms: [windows]
metadata:
  hermes:
    tags: [FEM, Maxwell, AEDT, Verification, Debugging]
    related_skills: [systematic-debugging]
---

# Electromagnetic FEM Verification

Use staged, persisted evidence to distinguish geometry, mesh, excitation, solver, memory, and automation failures in long electromagnetic FEM jobs. This skill verifies what actually completed; it does not treat analytical methodology, presolve validation, or a single mesh as final physical evidence.

## When to Use

- A Maxwell/AEDT or comparable EM FEM run lasts long enough that blind reruns are costly.
- Geometry and excitation validate, but meshing or `Analyze` later fails.
- A physical winding, bus, terminal, or conduction network may be mesh-sensitive.
- The result will be used to correct an analytical design methodology.
- Do not use this as proof that a model is physically correct merely because automation returned success.

## Prerequisites

- A solver project with a clearly named immutable presolve source design.
- A separate duplicated design for each changed physical diagnostic. Adaptive mesh levels within one unchanged design can qualify as comparable levels when their quantities, errors, and refinement history are persisted; separate projects per mesh level are not inherently required.
- A persistent run journal or JSON record outside transient console output.
- Access to solver profile, convergence, mesh statistics, validation log, and Message Manager output.
- For AEDT work, load the applicable `ansys-aedt` skill for connection and PyAEDT mechanics; this skill governs verification discipline.

Session-specific Maxwell evidence and exact failure signatures are in `references/maxwell-conduction-path-case.md`. For a validated class-level pattern that replaces a mesh-sensitive united winding with individually extended physical cable paths and strict external-terminal presolve gates, read `references/maxwell-multibranch-terminal-topology.md`. For auditing requested versus actually used cores, manual Solution Matrix MPI/DDM configurations, iterative-to-direct transitions, GPU limits, licensing checks, and a controlled core/task benchmark, read `references/maxwell-hpc-stage-parallelism.md`. For safe attachment to an already-open AEDT project, numerical cross-section current integration from exported `J`, gap-flux integration from exported `B`, and solid-level proof of swept-conductor overlap, read `references/maxwell-saved-field-current-flux-audit.md`. For post-close proof that a CAD-only project actually persisted its designs and geometry, plus the validated core-only fallback when winding inputs are unknown, read `references/aedt-cad-persistence-gates.md`.

## Procedure

### 1. Define the evidence contract before running

Record:

- source project and immutable source design;
- duplicated target design and setup;
- geometry, material, excitation, current, turns, branches, gap, domain, and mesh controls;
- required outputs and acceptance thresholds;
- whether the run is only a pilot, coarse control, convergence level, or final candidate.

Completion criterion: the run can be reconstructed without relying on the current chat or GUI state.

### 2. Enforce the presolve gate

Before meshing, persist all of the following:

1. `ValidateDesign` return code and validation log;
2. Message Manager messages captured immediately after validation;
3. expected conduction-path object membership, not only a success string;
4. terminal assignments and excitation properties;
5. available physical memory;
6. a geometry screenshot and object/topology audit.

Treat this gate as **necessary but not sufficient**. A conduction-path validation can succeed while the tetrahedral solve later rejects the winding.

Completion criterion: validation has no errors, no current-leak message, and the exact expected path-to-object mapping is recorded.

### 2A. Verify persisted CAD, not only the live session

Live face measurements and a successful PyAEDT return do not prove that geometry was persisted. After every CAD-only build:

1. save each design before running optional preview/export APIs;
2. close AEDT cleanly;
3. verify the saved `.aedt` contains nonzero 3D geometry, all expected design names, and a nontrivial file size;
4. reopen read-only and enumerate designs/objects when the text-level persistence check is ambiguous;
5. compare the project SHA-256 before and after any screenshot-only reopen.

A live CAD gate fails if the post-close project is an empty shell, even when face IDs, centers, and gaps were measured successfully in memory. Preserve failed projects as evidence and retry under a new filename after changing one classified variable.

Keep screenshots outside the build transaction. Export them in a separate read-only reopen, label them `DIAGNOSTIC geometry`, visually confirm that they are not field maps, and require the project hash to remain unchanged.

Completion criterion: live measurements, post-close storage evidence, and visual diagnostics all identify the same designs and geometry, while mesh and solver flags remain false.

### 2B. Use core-only screening when winding inputs are unknown

If cable OD, bend radius, insulation stack, terminal placement, or physical routing is unknown, do not invent a full winding CAD. A core-only screening project may still verify supplier-half import, E-E transforms, center-gap machining, side-leg mating, actual pole-face area, and a low/mid/high gap hypothesis range. It must remain explicitly unaccepted as the active winding model and must not advance to mesh or solve.

For supplier STEP files, distinguish all `CARTESIAN_POINT` records from topological `VERTEX_POINT` coordinates; use the latter for a reliable text-level bounding-box sanity check before AEDT import.

Call mesh generation independently when the API permits it. After it returns, capture before clearing messages:

- the direct return value;
- Message Manager output;
- mesh statistics and tetrahedron count;
- solver profile showing the mesh stop status;
- elapsed time and memory trace;
- project save state.

Do not infer mesh completion from one optimistic UI line. Require a normal-completion profile or equivalent persistent artifact.

Completion criterion: the initial mesh is saved, counted, and marked normal completion with no mesh error.

### 4. Gate `Analyze` independently

Clear only stale messages associated with older runs, then start `Analyze`. Immediately after it returns:

1. capture Message Manager before any logger cleanup;
2. persist the boolean/API result;
3. read the solver profile even when the API only returns `False`;
4. confirm whether Pass 1 began, a matrix solve occurred, and a field state exists;
5. verify the expected solution sweep contains a completed state, not merely a setup name.

Completion criterion: the profile reports normal completion and at least one valid field state exists.

### 5. Classify the failure before changing anything

Use these evidence classes:

- **CAD topology:** duplicate the design and use a destructive connectivity probe such as Separate Bodies only on the temporary copy. Record component count and volumes.
- **Mesh topology:** CAD is connected, initial mesh completes, but Pass 1 reports no conduction path or a current leak.
- **Memory:** memory trace reaches the configured limit, paging dominates, or the profile reports allocation failure.
- **Excitation:** validation rejects terminals, path membership is wrong, or solver reports current leak.
- **Automation:** GUI/profile shows completion but the wrapper misreports, or the wrapper logs contradictory lines.
- **Physics/convergence:** the solve completes, but independent mesh levels, energy/matrix/flux checks, or domain studies disagree.

Completion criterion: a falsifiable root-cause statement cites persistent artifacts, not intuition.

### 6. Apply the no-blind-rerun rule

Do not repeat a long run when geometry, excitation topology, mesh contract, and solver settings are unchanged. First make one evidence-based change that targets the classified cause, then validate it on an isolated presolve probe.

For winding topology changes, require the probe to demonstrate the exact intended number of connected components and conduction paths before meshing. Do not promote a pending probe to a working method.

Completion criterion: the rerun differs in one named, justified variable and its presolve probe passed.

### 7. Use lower-dimensional screening before an expensive 3D rerun

When a topology or excitation change can be separated from inherently 3D effects, build a fast 2D surrogate before committing to another long 3D solve. The 2D gate should preserve the magnetic circuit, gap, section turns, current, and signed ampere-turns, then check field scale, gap flux, energy-derived inductance, section symmetry, and aiding versus opposing polarity. Require its own mesh/domain sensitivity rather than treating a single fast solve as truth.

State its limitations explicitly: 2D does not verify real 3D cable routing, end turns, PCB nodes, terminal topology, lead leakage, or proximity/fringing around finite conductors. Passing 2D authorizes a short 3D field probe, not immediate production acceptance; failing 2D blocks an expensive 3D rerun until the magnetic-scale or polarity error is explained.

Completion criterion: the 2D artifact establishes a physically plausible magnetic scale and polarity with documented normalization, while all unresolved 3D-only questions remain listed as gates.

### 8. Accept physical results only after convergence evidence

A coarse result is a control, not a final result. Final acceptance normally requires:

- at least three comparable mesh levels with recorded quantities and errors (qualified adaptive passes may count; initial meshing followed by coarsening is not an extra solved level);
- a stated convergence threshold;
- external-domain sensitivity;
- nonlinear or operating-point checks when material behavior requires them;
- two or more independent observable estimates where meaningful, such as matrix inductance and magnetic energy;
- investigation of large disagreements instead of averaging them away.

Analytical formulas remain hypotheses until converged FEM or measurement supports them for the exact model.

Completion criterion: every acceptance requirement is backed by a named artifact and numerical comparison.

### 9. Export field evidence after every successful solve

A numerically successful 2D or 3D solve is not a complete deliverable until field images are exported and delivered with the result. The minimum useful set is:

- geometry overview with core, gap, full winding, and surrounding region visible;
- `|B|` plus a directional or normal-flux view through the gap and winding window;
- `|H|` over the same physical context;
- `|J|` and current direction on all physical conductor branches when solved;
- magnetic-energy density around the gap, winding, and leakage-field region;
- volumetric loss density only when a valid loss model was solved;
- temperature and heat flux only when a valid thermal solution exists.

Do not crop every plot to the ferrite interior: include at least one overview and one section that show how the field interacts with the entire coil and surrounding space. Every image should identify design/setup/pass, units, legend, scale limits, camera orientation, and status (`ACCEPTED`, `DIAGNOSTIC`, or `REJECTED`). If the GUI field-plot path fails, export field data and render it offline rather than silently omitting visual evidence. Never label magnetic energy or current density as heat or temperature.

Completion criterion: the result message includes the required field images or explicitly states which fields were not physically solved and therefore cannot be shown.

## Background Monitoring

For long bounded jobs, launch them as tracked background processes with completion notification. Do not add a runtime kill unless the user explicitly requests one. Status questions should trigger a one-time process/profile check; continuous polling is unnecessary.

Distinguish:

- scheduler or wrapper notification;
- solver timeout;
- manual cancellation;
- solver-reported failure.

### 10. Report solver status with evidence of actual stage and progress

When a long FEM solve is running, the user expects concrete evidence of forward motion: **which pass is active, convergence metrics, mesh refinement progress** — not vague "calculating" or "in progress" labels. Report the **most recent solver artifact** visible in logs, profile, or stdout:

- Pass N/M started/completed
- Current adaptive refinement percentage
- Energy error or delta-energy from last pass
- Mesher stage (tetrahedralization, refinement, quality check)
- Field-solve phase (matrix assembly, iterative solver active, postprocessing)

If logs show no new output for >5 minutes during an expected-long phase, state that explicitly: "Pass 3 meshing completed 8 minutes ago; solver output quiet since; no errors in stderr; typical for matrix-assembly phase on this mesh size." For Kirill, do not poll a background process or its logs regularly. Use completion notification; perform a one-time status check only on an explicit status request or a concrete safety need. After completion, inspect persisted solver artifacts once to establish the outcome. This preference takes precedence over incremental progress reporting.

### Report operational state literally

Never describe a planned redesign, a task-list item, or an identified next step as “being worked on.” Before answering a status question, inspect the live process list and the latest persisted artifact, then use exactly one of these states:

- **planned** — no driver or solver is running and no new artifact is being produced;
- **active CAD/presolve probe** — name the driver/process and state explicitly that mesh and field solve have not started;
- **active meshing** — identify the mesher stage and evidence of CPU/memory progress;
- **active field solve** — identify setup/pass and whether a field state exists;
- **completed/failed** — cite the terminal artifact, not merely a wrapper notification.

If work was only planned, say so directly and start it immediately only when authorized. Do not let an `in_progress` task-list label substitute for evidence of an active operation.

Completion criterion: the user can tell whether anything is actually running, what exact stage it is in, and what evidence supports that status.

## Postprocessing and Field-Image Gate

Before calling a run a Litz/material-specific solve, verify persisted body assignments through native AEDT properties, not just the material library or setter return. Preserve the existing solution while auditing it. For validated GUI B/H export, convergence extraction, assignment checks and same-basis TeX/FEM comparisons, read `references/maxwell-material-field-reconciliation.md`.

Treat flux/energy agreement from one field solution as internal consistency, never as physical accuracy. Compare nominal, tolerance-high and differential inductance on explicitly matched current/material/geometry bases; do not mistake total-linkage-derived equivalent B for local Bmax. A homogenized monolithic winding can be valid for magnetostatics when its equivalent excitation is demonstrated.

For Maxwell/PyAEDT result extraction, persist the raw `SolutionData` arrays before any unit conversion and record the project display units. Do not divide `FluxLinkage(...)` by 1000 unless AEDT explicitly reports mWb; in the verified Magnetostatic export, `FluxLinkage` was already returned as Wb while `InputCurrent` was returned in mA-equivalent numeric form (`52599.8` for `52.5998 A`). Convert each quantity independently, then compute `L = Psi/I` and show the raw values beside the interpreted values. A unit mistake in postprocessing must never trigger a new solve.

When the user requests field evidence, export true 2D planar maps, not a 3D camera view of a colored cut plane. Each delivered image must state the plane and coordinate (for example, `Mag_B, YZ, X=0 mm`), show axes with units, a readable color bar with `T`, setup/pass, and the quantity name. Visually inspect the exported image; if it is wireframe, blank, edge-on, or lacks the legend, classify the export as failed even when `Analyze` succeeded. Use a separate geometry overview only as supplementary evidence.

For an inductance target, do not compare a two-section result by simply adding `L1 + L2` until the physical circuit is proven. Extract section self terms and mutual coupling/sign, then evaluate the actual series connection (`L_total = L1 + L2 +/- 2M`) with signed terminal polarity. Before changing CAD, compare the target against a gap-only estimate using the actual `Ae`, gap, and effective complete-turn count; this distinguishes wrong turns/gap/polarity from a postprocessing error.

## Controlled domain and mesh diagnostics

Before expanding a Maxwell region, inventory external coil terminal face locations. External terminals must coincide with conductor surfaces on the problem-region boundary. Expanding through their plane without rerouting conductors invalidates excitation; touching that boundary is not by itself proof of a defective model. A transverse-only expansion that preserves terminal planes is a valid **partial** domain study, not full 3D domain acceptance. Extending leads also changes physical leakage and cannot be called a pure boundary-size comparison.

Read the saved validation log even if Message Manager is empty: `validate_simple` returns **1 for success, 0 for failure**. Never weaken the gate to reinterpret zero as success. Preserve setup settings when testing domain size; when testing mesh sensitivity, change only documented adaptation criteria. Require native profile completion, convergence history and actual field data; never assign `field_solution_exists = analyze_return` as evidence.

For Kirill, answering “why does FEM disagree?” requires a falsifiable comparison and continued authorized investigation, not repeatedly calling the newest suspicion the root cause. Maintain a hypothesis ledger with measured deltas and unresolved gates. A material rename with unchanged magnetostatic properties is not a physical correction; a spatial energy partition is not an independently separable leakage inductance to subtract from the result. Small changes under mesh refinement narrow the explanation but do not prove physical accuracy or validate the analytical formula.

For tested transverse-domain and stricter-mesh comparisons, validation signatures and interpretation limits, see `references/maxwell-domain-mesh-diagnostics.md`.

## Pitfalls

- **Context or memory is not engineering source authority:** before CAD, compare frequency key, electrical topology, turns per complete conductor path, parallel-path count, continuity, target inductance, and gap across the prompt, canonical result, contract, and FEM manifest. A chat handoff, task label, remembered topology, or internally consistent draft cannot supersede those files unless the amendment is explicit and persisted. If semantics conflict, reject the derived branch even when every hash matches. Distinguish electrical turns from physical banks and parallel cables: parallel cables do not change turns, while two series-aiding sections add turns and require an L/M matrix. Frequency variants are alternatives unless the contract explicitly combines them. A core-only CAD may validate import/transforms/face probes, but any gap hypothesis derived from a rejected turn count is non-active evidence. See `references/semantic-source-authority-gate.md`.
- **Hash-consistent but semantically stale chain:** matching hashes prove identity, not that the contract/manifest still represents the latest required turns, sections, paths, nodes, or polarity. Verify those semantics before CAD.
- **Live CAD success without persistence:** face centres and object queries can pass in memory while the saved `.aedt` is an empty shell. Require the post-close storage gate in `references/aedt-cad-persistence-gates.md`.
- **Sharp-edge maxima:** a zero-radius CAD edge is acceptable only as an explicitly diagnostic geometry assumption. Local B/H maxima at that edge are non-acceptance until radius sensitivity or measured machining geometry exists.
- **Requested cores ≠ used cores:** `cores=N`, a broad CPU affinity mask, many process threads, or an HPC checkout only prove resource availability. Verify actual per-stage core use from the generated ACF, Maxwell profile solver designation, and CPU-time delta; use manual Solution Matrix MPI/DDM benchmarks for Magnetostatic when local multiprocessing remains serial.
- **`ValidateDesign` overconfidence:** it can validate CAD conduction before the tetrahedral solver discovers a missing path.
- **Message loss:** clearing the logger immediately after a failed solve destroys the most precise error. Capture first, clear later.
- **Wrapper contradiction:** PyAEDT may print an error and then a generic “solved correctly” duration line. Trust the return value, Message Manager, profile stop status, and field-state existence together.
- **Stale GUI messages:** filter by current project, design, setup, and timestamp; old red messages are not current evidence.
- **Connected CAD ≠ connected mesh:** a one-component Separate Bodies result rules out gross CAD disconnection but does not prove tetrahedral current connectivity.
- **RAM assumptions:** long runtime or solver failure is not automatically out-of-memory. Use measured availability and profile evidence.
- **Volume-mean current inference:** `Mean(Mag_J)` over a complete winding solid is not branch current. Integrate the signed normal component across an internal lead cross-section and verify both P/N faces.
- **Duplicate live AEDT projects:** when a project is already open in the target gRPC desktop, attaching by full `.aedt` path can open a second same-named project and make the active design ambiguous. Attach by project name; disambiguate duplicate project objects before closing anything.
- **Infinite-cylinder overlap assumptions:** centerline spacing and summed radii do not prove that finite swept solids with flat caps intersect. Require a separate-solid point/Boolean probe on a copy.
- **Unverified redesigns:** a topology that merely sounds better is still a hypothesis until its presolve and solve gates pass.
- **Mixed Maxwell cleanup:** do not iterate over `app.boundaries` and delete Matrix, Winding Group, and Coil Terminals as interchangeable objects. Inventory names/types first; on an isolated duplicate, remove dependent Maxwell parameters and excitations explicitly through their owning AEDT modules and in dependency order, then verify the copied design is clean before editing geometry. A cleanup/API failure means the physical probe never started and must be reported as automation failure, not topology evidence. See `references/maxwell-conduction-path-case.md`.
- **Single-mesh conclusions:** close energy/matrix agreement on one mesh does not establish mesh convergence or physical completeness.
- **Maxwell 2D field-plot camera:** in AEDT 2024 R2 a planar XY design exported through `export_field_jpg(..., orientation="top")` can be rendered edge-on as a line. Probe orientations on a geometry-only image; for the verified E160 Maxwell 2D case `orientation="front"` showed the sheet face-on. Visually inspect every exported image before delivery.
- **Maxwell 2D field-plot export returns geometry preview instead of field:** `create_fieldplot_surface()` can return a plot object and `export_field_jpg()` can return `True`, yet the exported JPG contains only wireframe geometry without field colormap or legend. This is not a camera-orientation issue (the geometry is visible face-on) but a rendering-state failure where AEDT exports a geometry preview instead of the solved field visualization. Visually inspect **every** exported field image before delivery; when an image lacks the expected color gradient and legend, it is geometry-only and must be re-exported or the user explicitly informed that field visualization export failed but the solve itself succeeded. Do not label a geometry-only wireframe as field evidence.
- **Maxwell 2D named-expression instability:** with AEDT 2024 R2/PyAEDT 1.3.0, `FieldsCalculator.add_expression()` may fail in `LoadNamedExpressions` and leave the current PyAEDT wrapper unable to access `SetActiveEditor`. Classify this as postprocessing automation failure, not solver failure; stop repeated calls, fresh-reattach to the saved design, and fall back to raw field-grid export plus offline rendering/integration. Never rerun a valid FEM solve merely to recover screenshots.
- **Maxwell 2D energy normalization:** a raw field-calculator `Integrate(Energy)` can be returned per metre of out-of-plane depth even when Matrix L already includes `ModelDepth`. Verify against the convergence-table convention and apply the physical depth exactly once to raw energy; do not rescale Matrix L. An exact ratio equal to `1/depth_m` is strong evidence of this normalization mismatch.
- **GOST R 2.105 technical report formatting (Russian projects):** Russian FEM verification reports must follow GOST R 2.105 (technical documentation standard). Reuse existing project report-generation helpers (typically `make_report.py` with functions `h1`, `h2`, `para`, `add_figure`, `add_table`, `table_caption`, `setup_document`) rather than reimplementing formatting. Standard: Times New Roman 14pt, numbered headings (e.g., "1 Введение", "2.1 Подраздел"), figure captions "Рисунок N — Description", table captions "Таблица N — Description" with em-dash separator. When extending an existing calculation report with a new FEM chapter, load the existing document via `python-docx`, count existing "Рисунок" and "Таблица" occurrences to continue numbering, insert page break, and append the new chapter maintaining the established style.
- **GitHub Cyrillic filename visibility issue:** Files with Cyrillic names (e.g., `Отчёт_МКЭ.docx`) committed to git and successfully pushed may not appear in GitHub PR file listings (web UI/API exhibits caching or encoding issues). The file exists in the remote branch (`git ls-tree HEAD` confirms it), but the PR diff viewer and `gh pr view --json files` omit it. Workaround: use ASCII-transliterated filenames for reports in git repositories even when local filesystem supports UTF-8. Pattern: `Otchet_MKE_verification.docx` or `Raschet_drosselya_boost_FEM.docx` instead of Cyrillic. This is a GitHub platform limitation, not a git or encoding error.
- **Maxwell 2D `CalculatorWrite` gRPC instability:** In AEDT 2024 R2/PyAEDT 1.3.0, `ofieldsreporter.CalculatorWrite()` can fail with gRPC errors (`Failed to execute gRPC AEDT command: CalculatorWrite`) even after a successful field solve. When this blocks energy extraction or field probes, fall back to: (1) `app.post.get_scalar_field_value(quantity='Energy', scalar_function='Integrate', solution=..., object_name='AllObjects', object_type='surface')` for magnetic energy, and (2) `app.post.get_solution_data(expressions=f'{MATRIX}.L({row},{col})', setup_sweep_name=..., report_category='Magnetostatic', context=MATRIX)` for matrix parameters. Never rerun a converged solve just to recover postprocessing — the solution data is intact; only the automation layer failed.
- **Field plot export must be visually verified before delivery:** After `export_field_jpg()`, use `vision_analyze` to confirm the exported image contains a **color-mapped field with legend and min/max scale**, not geometry wireframe. The user expects actual field visualization screenshots after every solve result. If the export shows only CAD outlines, document it as "field visualization export failed; solve succeeded, geometry verified, but colormap rendering did not materialize" and either retry with alternative export settings or proceed without the image while explicitly noting the automation limitation. Do not deliver geometry-only wireframes labeled as field evidence.
- **Maxwell 2D postprocessing automation failure recovery:** when AEDT 2024 R2/PyAEDT 1.3.0 `CalculatorWrite` or `LoadNamedExpressions` fails mid-postprocessing with gRPC errors, the FEM solution itself remains valid and accessible. Extract Matrix L via `app.post.get_solution_data()` and field quantities via `app.post.get_scalar_field_value()` instead of retrying the broken automation path. Never rerun a valid converged solve merely to recover screenshots or derived quantities; write a separate postprocessing script that reads the saved design.

## Verification Checklist

- [ ] Semantic source-authority table reconciles frequency, topology, complete turns/path, parallel paths, continuity, target L, gap, and current across prompt/result/contract/manifest
- [ ] Context-only or rejected branches are disabled at plan/CAD CLI level and cannot produce new execution artifacts
- [ ] Immutable source design preserved
- [ ] CAD-only project passed post-close persistence verification (expected designs, nonzero geometry, stable SHA-256)
- [ ] Any core-only fallback remains explicitly unaccepted as the active winding model
- [ ] Geometry-only images are labelled `DIAGNOSTIC` and visually distinguished from field maps
- [ ] Target design is an isolated duplicate
- [ ] Validation log and direct Message Manager output persisted
- [ ] Exact conduction-path mapping recorded
- [ ] Initial mesh and Analyze treated as separate gates
- [ ] Mesh statistics and solver profile saved
- [ ] Memory claim backed by measurements
- [ ] Failure classified before any fix or rerun
- [ ] No long rerun with unchanged topology and settings
- [ ] Applicable 2D screening passed before an expensive corrected 3D rerun, with 3D-only limitations recorded
- [ ] Pending probes explicitly marked unverified
- [ ] Final result backed by comparable meshes and independent observables
- [ ] Successful solve delivered with contextual B/H/J/energy field images
- [ ] Loss/temperature plots shown only from valid loss/thermal solutions
