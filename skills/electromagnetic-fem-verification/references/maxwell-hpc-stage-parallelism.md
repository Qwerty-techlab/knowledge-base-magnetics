# Maxwell 3D HPC and stage parallelism

Use this note when a Maxwell 3D job receives multiple cores but a long `3dnms` stage still loads roughly one logical CPU. It distinguishes resource allocation from actual solver parallelism and defines a safe benchmark for manual Solution Matrix distribution.

## Authoritative sources

- Installed Maxwell 2024 R2 manual: `C:\Program Files\AnsysEM\v242\Win64\Help\Maxwell\Maxwell.pdf`.
- PyAEDT `Maxwell3d.analyze_setup` and `set_custom_hpc_options` API documentation.
- Solver profile (`*.profile`), generated ACF, process CPU delta, and FlexNet `lmutil lmstat` are the evidence for what the local run actually used.

## Durable findings

### Allocated cores are not used cores

`cores=N` and ACF `NumCores=N` grant a maximum resource allocation; they do not force every executable or internal phase to use N cores. Maxwell's profile encodes a matrix solver task as `Solver pdsn`, where `n` is the number of processors actually used. The manual explicitly allows this number to be lower than the available processors.

A useful audit therefore requires all four:

1. generated ACF (`NumEngines`, `NumCores`, `UseAutoSettings`, allowed distribution types);
2. exported Maxwell profile, including per-task `Cores` and solver designation;
3. process affinity and thread count;
4. CPU-time delta over a wall-time interval.

Affinity to all CPUs plus many process threads does not prove parallel computation.

### Stage behavior differs

A representative Maxwell 3D Magnetostatic profile showed:

- initial TAU mesh using all six allocated cores;
- mesh post-processing and manual refine using one core;
- an iterative solve on a roughly two-million-unknown matrix;
- a later long `3dnms` direct stage using about one CPU-second per wall-second despite six allocated cores.

Treat this as a case signature, not a universal performance table. Validation, conduction-path checks, seed/manual refinement, adaptation, matrix assembly, factorization, field recovery, and report generation have different parallel behavior.

### Manual Solution Matrix distribution

Maxwell 2024 R2 documents `Solution Matrix` distribution, based on matrix domain decomposition, for both Maxwell 3D Eddy Current and Maxwell 3D Magnetostatic designs. Distributed solver types require MPI.

For Magnetostatic, do not rely on `Use Automatic Settings`: the 2024 R2 manual describes automatic settings support for Transient and Eddy Current, not Magnetostatic. Create a manual configuration with:

- `use_auto_settings=False`;
- more than one task for an MPI/DDM candidate;
- total cores equal to the intended physical-core budget;
- `allowed_distribution_types=["Solution Matrix"]`;
- Intel MPI on the tested 2024 R2 Windows installation unless another supported MPI is deliberately validated.

PyAEDT exposes these directly:

```python
app.analyze_setup(
    setup_name,
    cores=16,
    tasks=2,
    use_auto_settings=False,
    allowed_distribution_types=["Solution Matrix"],
    blocking=True,
)
```

This requests two tasks sharing sixteen total cores; it does not promise an 8+8 split in every internal stage or linear acceleration.

### Memory-bounded custom ACF

`set_custom_hpc_options` exposes cores, tasks, distributions, and automatic settings, but not the machine `RAMPercent`. When preserving headroom for the agent, desktop, proxy, and other user applications is mandatory, use a custom ACF and pass it with `analyze_setup(..., acf_file=..., blocking=True)`.

The relevant ACF fields are:

```text
DesignType='Maxwell 3D'
MachineName='localhost'
NumEngines=<mpi_tasks>
NumCores=<total_core_budget>
RAMPercent=<derived_machine_limit>
UseAutoSettings=false
AllowedDistributionTypes[1: 'Solution Matrix']
BoolValues(AllowOffCore=true)
```

Derive `RAMPercent` from live physical memory, the resident AEDT GUI, the previous solver peak, and the required reserve; do not copy a fixed percentage between machines. Treat it as an AEDT/DSO limit, not an absolute Windows Job Object guarantee.

Before both meshing and Analyze, persist:

- physical total and available RAM;
- pagefile total, used, and free;
- summed RSS for the full Ansys process family;
- summed RSS for the agent/desktop process family;
- summed RSS for user-critical proxy/network applications;
- active solver processes.

Repeat the preflight immediately before Analyze because meshing and CAD duplication can consume several GiB after the first check. If the reserve is already too small, do not start the solve. During the solve, record the same process-family groups periodically and flag reserve breaches; avoid automatic termination of a long FEM run unless the user explicitly requests that policy.

When memory is tight, reduce MPI tasks before reducing the total core budget: multiple ranks can replicate solver data and increase aggregate memory. Start with two tasks; test four only after measured headroom and a controlled benchmark justify it.

### Iterative and direct solver relationship

For 3D Magnetostatic, PCG iterative solve is supported. The manual states that Maxwell automatically switches to direct solve if iterative convergence fails. A later direct stage may also be associated with requested matrix extraction. Do not infer the reason from the process name alone: require the final solver profile and Message Manager evidence.

Iterative solve can save roughly a factor of two or more memory according to the manual and may be faster, but it must pass the requested residual and produce the same accepted observables.

### GPU limit in 2024 R2

The exact HPC configuration note says AEDT GPU acceleration is supported only for Maxwell 3D Eddy Current Solution Matrix solves. Do not recommend a GPU as an accelerator for a Magnetostatic matrix solve unless a later version's official documentation and a pilot profile prove support.

### Licensing check

Electronics Desktop includes four HPC units per licensed simulation; additional cores or GPUs use Workgroup/Pack licensing. Check live availability and checkout rather than assuming that a requested core count was licensed:

```text
lmutil lmstat -f anshpc -c <server>
lmutil lmstat -f anshpc_pack -c <server>
```

A checked-out HPC Pack proves that HPC licensing is active, but it does not prove that the solver can use every allocated core in its current algorithmic phase.

## Safe benchmark protocol

Never alter an in-flight long run to test HPC settings. After it terminates:

1. Preserve the accepted presolve design and current result artifacts.
2. Duplicate the calculation design and reuse exactly the same saved mesh when supported.
3. Hold geometry, materials, excitations, setup residuals, matrix extraction, and mesh fixed.
4. Benchmark at least:
   - one task on all intended physical cores (local multiprocessing baseline);
   - two tasks sharing those cores (first DDM candidate);
   - four tasks sharing those cores when memory permits.
5. Prefer physical cores first; test SMT/logical processors only as a separate point.
6. Record startup/validation, mesh, assembly, iterative/direct solve, adaptation, and post-processing times separately.
7. Verify the generated ACF and exported profile rather than trusting the requested API arguments.
8. Measure process-tree CPU use, not only the parent process or total system CPU percentage.
9. Compare field-state existence and accepted observables (matrix inductance, energy, convergence) before accepting the fastest configuration.
10. Monitor peak memory and paging. Multiple tasks can increase aggregate memory; a faster CPU does not compensate for DDM paging.

Example physical-core test grid:

- 16-core CPU: `1×16`, `2×8`, `4×4`;
- 12-core CPU: `1×12`, `2×6`, `3×4`.

The notation is tasks × nominal cores per task; PyAEDT receives total `cores` and total `tasks`.

## Pitfalls

- Increasing `cores` while retaining one task and unsupported Auto mode is not a DDM test.
- `AllowedDistributionTypes` in a generated ACF is evidence of permission, not evidence that a distribution was selected.
- High thread count, broad affinity, or an HPC checkout is not evidence of multicore progress.
- Do not extrapolate direct-solver time from single-thread benchmarks after enabling DDM; establish a Maxwell-specific speedup curve.
- Do not benchmark by changing mesh or solver residuals at the same time as task/core layout.
- Multiple variations/frequencies distribute well but do not accelerate one operating point unless the relevant matrix/solver distribution is actually selected.
