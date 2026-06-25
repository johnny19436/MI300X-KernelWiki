# MI300X Query Index By Problem

Use this page to jump from optimization symptom to the most relevant MI300X guidance.

## Low Occupancy

- [Optimization symptoms: low occupancy](../wiki/hardware/mi300x-optimization-symptoms.md#symptom-low-occupancy)
- [Counter cookbook: occupancy and wave activity](../wiki/techniques/mi300x-counter-cookbook.md#bundle-a-occupancy-and-wave-activity)
- [Kernel patterns: cross-pattern tuning order](../wiki/kernels/mi300x-kernel-patterns.md#cross-pattern-tuning-order)

## Memory-Bound Throughput

- [Optimization symptoms: memory-bound kernel](../wiki/hardware/mi300x-optimization-symptoms.md#symptom-memory-bound-kernel)
- [Counter cookbook: memory throughput and cache behavior](../wiki/techniques/mi300x-counter-cookbook.md#bundle-b-memory-throughput-and-cache-behavior)
- [Kernel patterns: GEMM](../wiki/kernels/mi300x-kernel-patterns.md#gemm)

## LDS Stalls Or Local Memory Pressure

- [Optimization symptoms: LDS pressure or LDS stalls](../wiki/hardware/mi300x-optimization-symptoms.md#symptom-lds-pressure-or-lds-stalls)
- [Counter cookbook: synchronization and local memory](../wiki/techniques/mi300x-counter-cookbook.md#bundle-d-synchronization-and-local-memory)
- [ISA bridge: effective local data share use](../wiki/languages/mi300x-isa-bridge.md#intent-effective-local-data-share-use)

## High VGPR Pressure

- [Optimization symptoms: VGPR pressure](../wiki/hardware/mi300x-optimization-symptoms.md#symptom-vgpr-pressure)
- [Counter cookbook: occupancy and wave activity](../wiki/techniques/mi300x-counter-cookbook.md#bundle-a-occupancy-and-wave-activity)
- [Kernel patterns: benchmark hygiene](../wiki/kernels/mi300x-kernel-patterns.md#benchmark-hygiene)

## Wave Inefficiency Or Divergence

- [Optimization symptoms: wave inefficiency](../wiki/hardware/mi300x-optimization-symptoms.md#symptom-wave-inefficiency)
- [Counter cookbook: instruction mix and pipeline balance](../wiki/techniques/mi300x-counter-cookbook.md#bundle-c-instruction-mix-and-pipeline-balance)
- [ISA bridge: lower control-flow overhead](../wiki/languages/mi300x-isa-bridge.md#intent-lower-control-flow-overhead)
