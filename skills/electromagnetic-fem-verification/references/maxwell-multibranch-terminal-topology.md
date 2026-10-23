# Maxwell multi-branch external-terminal topology

Use when a complicated united stranded conductor passes presolve but loses its conduction path after tetrahedralisation.

## Validated presolve pattern

1. Preserve an immutable accepted source design and edit only a disposable copy.
2. Keep each physical parallel cable as one continuous solid rather than one highly branched united current network.
3. Extend each cable's two *real end faces* to one field-region boundary. Build extensions with `create_object_from_face` + `sweep_along_vector`, then unite each extension pair back into its cable.
4. Delete the inherited parameterised Region before extensions. Create the final Region only after all extensions, with `Absolute Offset` and zero padding on the terminal side. Otherwise Region can expand when leads are added, leaving terminals inside the domain although they matched the old boundary.
5. Verify final Region bounding box and every terminal face centre numerically before assigning excitation.
6. Assign paired Coil Terminals, one solid Current winding with the physical parallel-branch count, and the inductance matrix. Treat this only as a provisional excitation topology until the saved-field current-distribution gate below passes.
7. Before mesh/Analyze require:
   - `ValidateDesign == 1`;
   - explicit conduction-path success;
   - exactly one path per cable with exact object mapping;
   - no illegal external terminal;
   - no current leak;
   - no current-design Message Manager error;
   - saved JSON/log evidence.

## Saved-field current-distribution gate

Formal conduction-path success does not prove that every physical parallel cable carries current or that individual P/N Coil Terminals inside one Winding Group behave as two ideal common PCB buses. A design can pass all presolve path checks while some isolated solids carry essentially zero current.

After the first saved field state:

1. integrate the signed normal component of `J` on an internal cross-section at both ends of every cable;
2. require opposite P/N signs and matching magnitudes for each body;
3. compare each active cable with `I_winding / parallel_branches`;
4. require the exact expected active-branch count and current sum;
5. reject the topology if any expected branch is unenergized, even when matrix and field energy agree.

For the robust numerical export/integration method, see `maxwell-saved-field-current-flux-audit.md`.

If this gate fails, use isolated diagnostic copies to discriminate the circuit interpretation:

- one explicit current winding per physical cable at `I_winding / branch_count`;
- a small number of multi-face terminals representing actual common bus nodes;
- the original grouped-terminal topology as control.

Keep geometry, mesh, current, materials, and solver settings fixed. Do not promote either alternative until its strict presolve gate and saved-field current audit pass.

## AEDT 2024 R2 / PyAEDT 1.3 robustness

- `duplicate_design()` performs Paste then `RenameDesignInstance`; the rename can fail while leaving an orphan copy. For diagnostics, use `CopyDesign`/`Paste`, detect the single new AEDT-assigned name, and do not rename it.
- Copied Coil Terminal props can omit `Faces`. Resolve audited real terminal faces from geometry with `get_faceid_from_position`, not copied `BoundaryProps`.
- Remove dependencies in order: Matrix via `MaxwellParameterSetup.DeleteParameters`, then Winding Group, then Coil Terminals via `BoundarySetup.DeleteBoundaries`.
- First prove one complete cable without mesh/Analyze; only then expand to all branches and require exact path mapping.
- A presolve pass proves excitation/topological admissibility only. Long external leads can change inductance/fields; bound or de-embed that contribution before accepting final FEM geometry.

## Status reporting

Distinguish planned redesign, active CAD/presolve driver, active meshing, and active field solve. A task-list `in_progress` label is not evidence that work or simulation is running.
