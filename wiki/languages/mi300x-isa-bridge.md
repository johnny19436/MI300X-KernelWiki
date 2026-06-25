# MI300X ISA Bridge

This page links optimization intent to instruction families you can inspect in disassembly.

Primary reference:

- `sources/amdgpu_isa_cdna3.xml`

## How To Use This Bridge

1. Start from a kernel-level symptom.
2. Choose the expected instruction behavior.
3. Inspect disassembly for matching instruction families and balance.
4. If mismatch exists, adjust source-level structure and rebuild.

## Intent: High Arithmetic Throughput

Look for:

- Vector ALU and matrix-oriented instruction flow in hot loops.
- Steady compute issue without long memory-only regions.

If missing:

- Check whether indexing/control flow prevents vectorization.
- Reduce branching and simplify hot-loop dependency chains.

## Intent: Efficient Global Memory Access

Look for:

- Consistent global memory instructions with regular address progression.
- Fewer scattered access patterns in hot sections.

If problematic:

- Rework data layout or indexing to improve contiguous lane access.
- Increase tiling/reuse to reduce repeated global reads.

## Intent: Effective Local Data Share Use

Look for:

- Local memory instructions concentrated around high-reuse stages.
- Limited synchronization around LDS transactions.

If problematic:

- Reduce unnecessary local-memory staging.
- Adjust LDS layout to reduce conflict-prone access patterns.

## Intent: Better Scalar vs Vector Balance

Look for:

- Control/scalar instructions supporting setup, not dominating hot loops.
- Main arithmetic path executed in vector/matrix pipelines.

If problematic:

- Move invariant scalar setup outside inner loops.
- Avoid scalar-heavy address computation in wave-hot regions.

## Intent: Lower Control-Flow Overhead

Look for:

- Compact branch structure in critical loops.
- Minimal divergent control paths.

If problematic:

- Split tail/rare paths from the core hot path.
- Prefer branch-light loop bodies for throughput-critical regions.

## Instruction Families To Track In `sources/amdgpu_isa_cdna3.xml`

- Scalar ALU families (for control/setup paths).
- Vector ALU families (for lane-parallel arithmetic paths).
- Memory families (global and local data movement behavior).
- Flow-control families (branch/wait/sync behavior).

Use the XML file to confirm:

- Encoding family (`EncodingName`).
- Opcode values and operand forms.
- Field layouts for relevant instruction formats.

## Practical Disassembly Checklist

- Is the hot loop dominated by expected compute instructions?
- Is memory traffic pattern aligned with your tile/index strategy?
- Are synchronization instructions concentrated or excessive?
- Do branches appear in the hottest instruction window?

If two variants have similar runtime, prefer the one with:

- Cleaner instruction mix.
- Lower synchronization burden.
- Better occupancy headroom.
