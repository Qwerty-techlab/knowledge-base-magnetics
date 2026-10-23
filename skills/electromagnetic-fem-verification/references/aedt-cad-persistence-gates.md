# AEDT CAD persistence and core-only screening gates

Use this reference when a CAD-only Maxwell/PyAEDT stage succeeds in the live session but must be proved after AEDT closes.

## Validated sequence

1. Run the live hardware gate and confirm no competing AEDT/Maxwell process.
2. Create a new project path; never reuse a failed or historical `.aedt`.
3. For a supplier STEP sanity check, parse only coordinates referenced by `VERTEX_POINT` for the topological bbox. All `CARTESIAN_POINT` records include curve centres and placement data and can produce a false bbox.
4. Build and measure the CAD. Persist face IDs, face centres, face areas, object names, bounding boxes, and side-contact probes. Keep `mesh_started=false`, `solver_started=false`, and `fields_exist=false` explicit.
5. Save every design immediately. Do not run screenshot, preview, or optional postprocessing APIs inside the build transaction.
6. Close AEDT and inspect the saved project. Require:
   - `ProjectContainsGeometry3D='1'` or equivalent geometry evidence;
   - nonzero `DesignIDServer` / a persisted design-model block;
   - every expected design name;
   - a nontrivial project size and stable SHA-256;
   - a successful read-only reopen when the text format is ambiguous.
7. Export geometry images in a separate read-only reopen. Compare project SHA-256 before and after. Visually label the files `DIAGNOSTIC geometry`; they are not field maps.

## AEDT 2024 R2 / PyAEDT 1.3 behaviours

- `Object3d.volume` can fail because `GetObjectVolume` returns `None` after Boolean subtraction. Treat volume as nullable diagnostic evidence unless volume is an explicit contract gate. Face-based gap and topology gates remain strict.
- Calling `export_design_preview_to_jpg()` before the first durable project save can leave an empty project shell even though live face measurements succeeded. A characteristic rejected shell has `ProjectContainsGeometry3D='0'`, `DesignIDServer=0`, no design block, and only the global project header.
- `app.plot()` depends on PyVista. Do not install or invoke it inside a critical build merely to obtain a picture. Use a separate graphical reopen with `post.export_model_picture()` or another native image export.
- A success message or `project_path.is_file()` is insufficient: the file may exist but contain no persisted design geometry.

## Core-only fallback

When physical winding inputs are unknown, a core-only project may screen:

- supplier-half bbox and transforms;
- E-E mating and symmetry;
- centre-gap low/mid/high hypotheses;
- unintended side gaps;
- actual pole-face area including supplier chamfers;
- monotonic core-half volume change.

It must remain unaccepted as the active winding model. Do not mesh or solve it as a substitute for missing cable OD, bend radius, insulation stack, routing, terminals, or excitations.

## Retry discipline

Preserve failed projects and their JSON as evidence. Retry under a new path only after changing one classified variable, such as removing an optional preview call from the save transaction or changing a nullable diagnostic query. Never overwrite a failed project to make the history appear successful.
