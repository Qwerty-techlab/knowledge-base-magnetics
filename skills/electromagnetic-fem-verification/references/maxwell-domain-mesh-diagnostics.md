# Controlled Maxwell domain and mesh diagnostics

## Verified partial-domain method

In AEDT 2024.2, a sectional winding used four external terminals at Z = +/-80 mm. Expanding the vacuum region to Z = +/-160 mm without extending the conductors produced `Illegal external terminal`: each external terminal must border the problem region and coincide with a 3D object surface. ValidateDesign returned 0 while Message Manager was empty; the saved validation log contained all four errors. The gate correctly prevented meshing.

A separate copy retained Z = +/-80 mm and changed only transverse bounds from X +/-130, Y +/-110 to X +/-210, Y +/-190 mm. Replacing the region with a vacuum box passed validation with exactly two expected conduction paths. A normal solve and accessible fields verified the method. This is **partial transverse sensitivity only**; it does not resolve core contact with the Z boundary or lead leakage. Do not present the unsuccessful full expansion as a recommended method.

## Comparison evidence, not a universal correction

- Transverse expansion: L 114.952528 -> 114.949486 microhenry, delta -0.002646 percent. Both runs used the 1 percent energy criterion. The delta is below the current mesh error indicator and is not a precisely resolved boundary contribution.
- Same geometry with adaptation tightened to 0.2 percent: six passes, 147646 -> 548216 tetrahedra. Final Energy Error 0.15774 percent, Delta Energy 0.066566 percent, L 114.532375 microhenry. Change from transverse baseline: -0.362865 percent.
- Analytical reference was 100.004025 microhenry; the remaining +14.5278 percent discrepancy was **unresolved**. No corrected gap or validated analytical correction followed from these tests.
- Native profile confirmed RAM Limit 35 percent, one task and eight cores. ACF contents alone were not used as proof of effective limits.

## Interpretation safeguards

Keep geometry, excitation, material, solver and domain fixed for a mesh study; preserve all setup settings for a domain study. If recreating setup, compare complete properties rather than assuming defaults match. Record each run's source hash, actual target path, validation log, convergence, profile, SI result arrays and visual exports. Exit 0 is insufficient; wrappers must fail nonzero on postprocessing failures too.

In a saved field audit, changing mesh/domain dramatically altered a local B maximum while integral L was stable. This supports treating local extrema as unresolved, not declaring saturation or proving a specific singularity. Integrating Energy over conductor volumes and converting 2W/I^2 is only a spatial energy contribution; it is not standalone leakage L that may be subtracted to force agreement.

## Resource and launch recovery

Create output directories before shell redirection; a Python script cannot create the directory for a log the shell must open before launching it. Persist preflight failure separately from solver failure. If available RAM blocks the gate, do not lower thresholds. With explicit authorization, close nonessential applications gracefully, protect solver/agent/communications and system services, then run one fresh preflight. A successful browser close and fresh passing preflight enabled the stricter-mesh run; avoid repeated polling or blanket process killing.

## Field delivery limitations

Native cut-plane export with front XZ and right YZ orientations yielded real colored B/H sections. Dense conductor wireframe and truncated plot titles still impaired readability. Presence of color is only an existence check, not full legibility acceptance. For Kirill, show front and side 2D sections with clear quantity, plane coordinate, setup/pass and units; suppress unnecessary overlays or add a readable detail view while retaining a contextual overview. Never rerun the solver just to repair visualization.
