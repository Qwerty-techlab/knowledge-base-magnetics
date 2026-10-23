# Maxwell saved materials, field evidence, and analytical reconciliation

## Persisted assignment gate
A material existing in the project library does not prove assignment. After editing a copy, save/reopen and verify each intended winding solid through both `object.material_name` and native:

```python
app.modeler.oeditor.GetPropertyValue(
    'Geometry3DAttributeTab', object_name, 'Material')
```
Record material properties separately from body assignments, plus excitation `IsSolid`, current, terminal faces and conductor counts. A library entry named Litz with strand parameters can coexist with copper assigned to both solids. Never call such a result a verified Litz solve. Do not silently change materials while extracting an existing solution: preserve that diagnostic and create a separate corrected iteration. Verify applied RAM settings in the solver profile against requested ACF, not merely that a preflight inspected the intended file.

## Validated image export (AEDT 2024.2 / PyAEDT 1.3.0)
Attach to the intended GUI project; avoid opening another same-named project. Identify core objects by material/name audit, not the first non-Region solid. Create surface maps on their face IDs:

```python
plot = app.post.create_fieldplot_surface(
    assignment=core_face_ids, quantity='Mag_B',
    setup='Setup1 : LastAdaptive', plot_name='Diagnostic_Mag_B')
app.post.export_model_picture(
    full_name=str(out_dir / 'Diagnostic_Mag_B.png'),
    field_selections=plot.name, orientation='isometric',
    width=1920, height=1080, show_grid=False, show_ruler=False)
```
Repeat for `Mag_H`. An absolute output path with an image extension worked. Inspect pixels: quantity, units, extrema, context and colour map must be present. Surface-core overview is not a gap-plane or volume-field map; label its scope accurately. A `Verified` filename must never imply physical acceptance. Export images separately from source-project saves; persist plots only in an evidence copy if required.

Extreme linear-core B values must be reported as unaccepted diagnostics. Cross-check with `get_scalar_field_value(quantity='Mag_B', scalar_function='Maximum', solution=..., object_name=core_name, object_type='volume')` and similarly for H. This confirms the displayed quantity, not the cause. Localize extrema before attributing them to sharp-edge singularities, geometric defects, smoothing or saturation. Constant permeability allows unphysical B without a nonlinear saturation response.

## Convergence extraction
Validated call:

```python
app.export_convergence('Setup1', output_file=str(out_dir/'convergence.txt'))
```
Read energy, element count, Energy Error and Delta Energy for each adaptive pass. Normal Completion and Adaptive Passes converged alone do not quantify every observable. Passing the energy threshold does not validate local maxima. Three qualified adaptive levels may count as comparable meshes; an initial dense mesh subsequently coarsened before solution is not an additional solved level.

## Reconciliation rules
- Recompute analytical formulas from stored parameters and cite TeX equation labels/lines. A gap designed to hit target L reproducing that target is arithmetic/implementation consistency, not independent physical validation.
- Compare at the same current and explicitly distinguish nominal L, tolerance-high L and differential L. A worst-case analytical B already based on Lmax must not be multiplied again by FEM-versus-Lnom discrepancy.
- Energy and flux-linkage agreeing in one linear field solution are internal consistency checks, not two independent physical validations or an accuracy estimate against hardware.
- `Psi_total/(N*Amin)` is only an equivalent analytical quantity when total linkage includes lead/leakage flux. It is not measured local core Bmax; use signed section flux integrals and spatial field statistics.
- A monolithic homogenized winding is not inherently invalid for magnetostatic L. Demonstrate equivalent ampere-turns and spatial current distribution. Explicit cable geometry requirements for AC losses must not become a blanket rejection of homogenized magnetostatics.
- Do not infer an opposing-polarity root cause from a small L or filenames. Compare excitation, units and definitions, then verify the self/mutual matrix; physically compatible linear self terms require |M| <= sqrt(L11*L22). Inconsistent terms signal a normalization/model-comparability problem.
- Do not attribute differences between two reruns to a material change without proving actual persisted assignment and controlling other changes.
- Update prior conclusions when native evidence contradicts them. Never fit a correction coefficient or change the contract solely from an unaccepted FEM result.
