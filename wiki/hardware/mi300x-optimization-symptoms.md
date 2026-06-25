# MI300X Optimization Symptoms

This page is a fast triage guide for MI300X kernel optimization.

Use the flow:

1. Observe symptom in timeline or profiler.
2. Confirm with a focused counter set.
3. Apply one fix pattern at a time.
4. Re-measure and keep only changes that improve throughput.

## Symptom: Low Occupancy

Likely causes:

- Too many VGPRs per wave.
- Too much LDS per block/workgroup.
- Workgroup shape limits active waves.

Counters to check:

- Active waves per CU.
- Register allocation pressure.
- LDS allocation pressure.

Fix patterns:

- Reduce register live ranges by splitting long dependency chains.
- Reduce temporary arrays and wide unrolled sections.
- Adjust workgroup size to improve resident waves.
- Move some reused values to LDS only when it lowers register pressure.

## Symptom: Memory-Bound Kernel

Likely causes:

- Non-coalesced global memory access.
- Low cache reuse for hot data.
- High bytes moved per arithmetic operation.

Counters to check:

- Global memory throughput.
- Cache hit behavior.
- Memory pipeline stall share.

Fix patterns:

- Reorder indexing so adjacent lanes touch adjacent addresses.
- Tile data in registers/LDS to increase data reuse.
- Fuse adjacent kernels to cut intermediate memory traffic.
- Use vectorized loads/stores where alignment allows.

## Symptom: LDS Pressure Or LDS Stalls

Likely causes:

- Excessive LDS traffic or bank conflicts.
- Overuse of LDS for values with weak reuse.
- Barrier frequency too high.

Counters to check:

- LDS transactions and stall share.
- Barrier and synchronization overhead.
- Wave wait reasons tied to local memory.

Fix patterns:

- Change LDS layout to reduce conflict patterns.
- Reduce synchronization points across waves.
- Keep only high-reuse data in LDS.
- Rebalance tile dimensions to lower LDS contention.

## Symptom: VGPR Pressure

Likely causes:

- Aggressive unrolling.
- Large in-flight accumulator sets.
- Long value lifetimes from fused epilogues.

Counters to check:

- Registers used per wave.
- Occupancy drop from register usage.
- Stall reasons from long dependency chains.

Fix patterns:

- Tune unroll factors per loop independently.
- Reduce simultaneously live accumulators.
- Hoist invariant work out of inner loops.
- Stage epilogue work to shorten critical live ranges.

## Symptom: Wave Inefficiency

Likely causes:

- Branch divergence.
- Tail handling inside hot loops.
- Imbalanced work assignment per wave.

Counters to check:

- Branch and control-flow efficiency.
- Lane utilization.
- Time spent in short or underutilized waves.

Fix patterns:

- Separate hot path and tail path kernels.
- Convert branch-heavy inner paths to predicated arithmetic when practical.
- Use launch geometry that aligns work to full wave utilization.
- Repartition work so waves get similar amounts of useful computation.

## Quick Iteration Checklist

- Keep one baseline run for every kernel version.
- Change one tuning variable at a time.
- Capture the exact launch shape and input sizes with each run.
- Keep top 3 candidate variants and retest before finalizing.
