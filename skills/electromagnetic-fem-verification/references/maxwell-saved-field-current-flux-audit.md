# Maxwell saved-field current and flux audit

Use this note when a Maxwell 3D solve completed but branch currents, flux linkage, or winding topology remain physically suspect. The methods below are read-only postprocessing of an existing field solution; they do not replace mesh convergence.

## Safe attachment to a live AEDT project

When the `.aedt` project is already open in the target gRPC desktop, attach by **project name**, not by the full file path:

```python
app = Maxwell3d(
    project="my_open_project",
    design="MyDesign",
    new_desktop=False,
    aedt_process_id=PID,
    close_on_exit=False,
)
```

Passing the full `.aedt` path to an already-open project can open a second project with the same name. This makes `SetActiveProject(name)` ambiguous and may cause PyAEDT to create an empty `Project1`, so a postprocessing script can silently inspect the wrong design.

If duplicates exist, use `Desktop.odesktop.GetProjects()` to obtain project object references, then inspect each object's `GetPath()` and `GetTopDesignList()`. Identify temporary copies by an explicit expected design signature, not merely by list position. A safe cleanup pattern is:

1. retain the object containing the expected production design set;
2. rename only the proven temporary project object to a unique path under `%LOCALAPPDATA%/Temp` with `oProject.Rename(path, True)`;
3. close that unique project name with `CloseProject`;
4. delete the temporary file;
5. confirm only the intended project remains.

Never close one of two same-named projects by name before disambiguating the object references.

## Branch-current audit from exported J

Do **not** infer conductor current from `Mean(Mag_J)` over an entire winding volume. Long turns, elbows, singular endpoint cells, and locally dead regions make volume means unrelated to the current through a cross-section.

For each straight terminal lead:

1. choose an internal planar section away from the Region boundary and geometric elbows;
2. establish the known section normal (for example `+/-Y`);
3. sample the complete circular or rectangular section on a regular grid;
4. export vector `J` from the saved solution with `post.export_field_file(..., sample_points=..., export_with_sample_points=True)`;
5. integrate the signed normal component in SI units.

For a circular cable sampled uniformly inside radius `r`:

```python
I_normalized = mean(J_normal_samples) * math.pi * r_m**2
I_raster = sum(J_normal_samples) * cell_area_m2
```

Report both estimates. Repeat on a coarser nested grid and record the difference. Also require:

- P and N cross-sections of the same body to have opposite signs and matching magnitudes;
- active-branch current to match `I_winding / parallel_branches` within the stated numerical tolerance;
- exactly-zero branches to be separated from small numerical deviations.

A robust diagnosis can emerge even when the absolute integration is only percent-level: a branch at `1e-14 A` while peers carry amperes is not a grid artifact.

### PyAEDT pitfall

`get_scalar_field_value("J", "Integrate", ..., is_vector=True, object_type="surface")` is not a signed current integral. Its helper path converts a vector to magnitude and may add `AtPhase`, which can fail for real Magnetostatic `J`. Typed named-expression registration can also fail in older Maxwell designs. Prefer explicit vector export and numerical integration unless a tested native `J dot n` calculator expression is already available for that exact AEDT version/design.

## Gap-flux audit from exported B

Choose a plane normal to the main flux in the middle of the air gap. Use cell-center samples over the exact gap cross-section, export vector `B`, and compute

```python
phi_signed = sum(B_normal) * cell_area_m2
phi_absolute = sum(abs(B_normal)) * cell_area_m2
```

Repeat with a second grid spacing and report the relative change. A sub-percent or tighter grid delta makes this a strong independent observable.

Compare flux with:

- mean and extrema of `B` in core/gap volumes;
- gap and total field energy;
- matrix inductance;
- expected ampere-turns.

Use `N*Phi/I` only after proving that the exported flux is actually linked by all claimed turns and that winding reference directions are correct. A mismatch between matrix/energy and `N*Phi/I` is diagnostic evidence of cancellation, topology, or linkage error; do not average the values.

## CAD-overlap proof for swept conductors

A centerline-distance test alone can give false overlap claims near finite swept-wire endpoints. A circular sweep can have a flat cap, so `axis distance < r1+r2` for hypothetical infinite cylinders does not prove the actual finite solids intersect.

On an isolated CAD project or design copy:

1. create the candidate turn and lead as separate solids with the production sweep settings;
2. query bodies at several interior points or use a Boolean intersection/separate-bodies probe;
3. require both body names or nonzero intersection volume;
4. record the count across every repeated turn/branch;
5. close and delete the temporary project after the test.

Treat an analytical proximity result as a hypothesis until this solid-level probe confirms it.

## Acceptance record

Persist:

- project/design/solution names;
- sample plane and grid spacing;
- field export files;
- per-terminal signed current and P/N mismatch;
- expected branch current and zero-branch list;
- signed/absolute gap flux and grid delta;
- matrix, energy, and flux-linkage comparisons;
- any failed visualization separately from the successful numerical audit.

A field plot failure does not invalidate already exported numerical fields, but do not report plots as created unless the image file exists and is inspected.
