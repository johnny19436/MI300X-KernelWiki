# MI300X Counter Cookbook

This page provides practical profiling bundles for MI300X kernel tuning.

Goal: collect a small, stable counter set per pass instead of collecting every metric at once.

## Profiling Workflow

1. Start with runtime and kernel-level hotspot ranking.
2. Pick one hotspot kernel.
3. Run one counter bundle at a time.
4. Apply a targeted fix and repeat the same bundle.

## Bundle A: Occupancy And Wave Activity

Use when:

- Throughput is lower than expected for compute-heavy kernels.
- You suspect register or LDS limits.

Collect:

- Active waves per CU.
- Theoretical vs achieved occupancy.
- Register and LDS pressure indicators.

Interpretation:

- Low achieved occupancy with high register pressure usually means VGPR-limited residency.
- Low achieved occupancy with high LDS allocation usually means LDS-limited residency.

Common actions:

- Reduce register lifetimes and unroll depth.
- Adjust block/workgroup shape to improve resident waves.

## Bundle B: Memory Throughput And Cache Behavior

Use when:

- Kernel scales with memory frequency or data size more than compute.
- Roofline estimate suggests memory bound behavior.

Collect:

- Global memory bytes and throughput.
- Cache hit behavior for read/write paths.
- Memory-related stall share.

Interpretation:

- High memory stalls with low cache locality suggests poor data reuse or access ordering.
- High global bytes per output element suggests redundant traffic.

Common actions:

- Improve coalescing by changing index order.
- Add tiling and reuse in registers/LDS.
- Fuse neighboring kernels to avoid round trips to global memory.

## Bundle C: Instruction Mix And Pipeline Balance

Use when:

- Kernel is compute-heavy but underperforms expected arithmetic throughput.

Collect:

- Vector/scalar/matrix instruction distribution.
- Issue and stall balance across pipelines.
- Branch/control overhead.

Interpretation:

- A mismatch between expected and observed matrix instructions can indicate codegen mismatch.
- High control-flow overhead in hot loops indicates divergence or branch-heavy structure.

Common actions:

- Inspect generated ISA for intended instruction families.
- Simplify hot-loop control flow.
- Rework loop bodies for steadier instruction issue.

## Bundle D: Synchronization And Local Memory

Use when:

- Kernel uses shared tiling, reduction trees, or frequent barriers.

Collect:

- Barrier and wait event counts.
- LDS transaction activity.
- Stalls attributed to local memory and sync points.

Interpretation:

- High barrier cost suggests over-synchronization.
- High LDS activity with low arithmetic gain suggests weak local-memory reuse value.

Common actions:

- Reduce barriers where data hazards do not require full-wave sync.
- Re-layout LDS buffers to reduce conflicts.
- Shrink LDS footprint to improve wave residency.

## Suggested `rocprof` Pass Strategy

- Pass 1: kernel time and hotspot identification.
- Pass 2: Bundle A (occupancy).
- Pass 3: Bundle B (memory behavior).
- Pass 4: Bundle C or D depending on what remains unclear.

Keep each pass repeatable:

- Same input batch and sequence.
- Same launch parameters.
- Same warm-up count.

## Common Misreads

- High occupancy does not guarantee high throughput.
- High memory throughput can still be inefficient if useful work per byte is low.
- A single best run is not enough; compare median over repeated runs.
- Counter changes must be interpreted together with kernel runtime.
