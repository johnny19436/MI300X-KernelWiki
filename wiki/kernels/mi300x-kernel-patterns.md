# MI300X Kernel Patterns

This page captures common kernel classes and first tuning levers for MI300X.

Use it to quickly choose a starting optimization strategy before deep profiling.

## GEMM

Primary bottlenecks:

- Matrix pipeline under-utilization.
- Global memory bandwidth pressure from poor tiling.
- Register pressure from large accumulator tiles.

First tuning levers:

- Tune block/workgroup tile sizes for balanced compute and memory traffic.
- Tune K-loop unroll factor to manage issue efficiency and register pressure.
- Increase data reuse through register/LDS staging.
- Verify generated ISA aligns with expected matrix-centric compute flow.

## Attention (Score, Softmax, Value Paths)

Primary bottlenecks:

- Memory traffic from large intermediate tensors.
- Synchronization overhead in blockwise reductions.
- Control-flow inefficiency in masked or tail regions.

First tuning levers:

- Use blockwise fusion to reduce global-memory round trips.
- Keep logits, normalization factors, and partial accumulators in fast storage when possible.
- Separate tail handling from hot path where practical.
- Validate softmax numerical path without excessive synchronization.

## Reduction

Primary bottlenecks:

- Memory bandwidth limits for low arithmetic-intensity reductions.
- Barrier overhead in tree-style reduction stages.
- Underutilized waves in final reduction phases.

First tuning levers:

- Use hierarchical reduction (within wave, then across waves).
- Minimize global writes of partial sums.
- Tune block size to reduce tail inefficiency.
- Keep final-stage reduction compact and branch-light.

## Softmax

Primary bottlenecks:

- Multiple passes over data (max, exp/sum, normalize).
- Numerical-stability overhead.
- Memory traffic when intermediate states spill frequently.

First tuning levers:

- Fuse max/sum/normalize stages where numerically safe.
- Use stable accumulation strategy while minimizing extra passes.
- Reduce global-memory intermediates with local staging.
- Tune vector width and launch shape for contiguous access.

## LayerNorm

Primary bottlenecks:

- Bandwidth pressure from read-modify-write on full feature vectors.
- Two-pass statistics and normalization overhead.
- Register and LDS pressure for wide feature dimensions.

First tuning levers:

- Fuse mean/variance/normalize when possible.
- Use reduction shapes that maximize lane utilization.
- Keep reusable statistics in fast storage to reduce reloads.
- Tune feature tiling to balance occupancy and memory reuse.

## Cross-Pattern Tuning Order

1. Fix obvious memory access inefficiencies.
2. Improve occupancy and wave residency.
3. Reduce synchronization and control-flow overhead.
4. Re-check ISA-level instruction mix for expected kernel behavior.

## Benchmark Hygiene

- Compare variants on the same input distribution.
- Track median runtime and variance, not only best-case runs.
- Keep a changelog of launch shape, unroll factors, and tiling.
