# MI300X Query Index By Technique

Use this page to find MI300X guidance by optimization method.

## Occupancy Tuning

- [Optimization symptoms: low occupancy](../wiki/hardware/mi300x-optimization-symptoms.md#symptom-low-occupancy)
- [Counter cookbook: occupancy and wave activity](../wiki/techniques/mi300x-counter-cookbook.md#bundle-a-occupancy-and-wave-activity)

## Memory Coalescing And Reuse

- [Optimization symptoms: memory-bound kernel](../wiki/hardware/mi300x-optimization-symptoms.md#symptom-memory-bound-kernel)
- [Counter cookbook: memory throughput and cache behavior](../wiki/techniques/mi300x-counter-cookbook.md#bundle-b-memory-throughput-and-cache-behavior)
- [Kernel patterns: attention](../wiki/kernels/mi300x-kernel-patterns.md#attention-score-softmax-value-paths)

## LDS Layout And Synchronization

- [Optimization symptoms: LDS pressure or LDS stalls](../wiki/hardware/mi300x-optimization-symptoms.md#symptom-lds-pressure-or-lds-stalls)
- [Counter cookbook: synchronization and local memory](../wiki/techniques/mi300x-counter-cookbook.md#bundle-d-synchronization-and-local-memory)
- [ISA bridge: effective local data share use](../wiki/languages/mi300x-isa-bridge.md#intent-effective-local-data-share-use)

## Register Pressure Reduction

- [Optimization symptoms: VGPR pressure](../wiki/hardware/mi300x-optimization-symptoms.md#symptom-vgpr-pressure)
- [Kernel patterns: GEMM](../wiki/kernels/mi300x-kernel-patterns.md#gemm)

## Control-Flow Simplification

- [Optimization symptoms: wave inefficiency](../wiki/hardware/mi300x-optimization-symptoms.md#symptom-wave-inefficiency)
- [Counter cookbook: instruction mix and pipeline balance](../wiki/techniques/mi300x-counter-cookbook.md#bundle-c-instruction-mix-and-pipeline-balance)
- [ISA bridge: lower control-flow overhead](../wiki/languages/mi300x-isa-bridge.md#intent-lower-control-flow-overhead)

## ISA-Guided Verification

- [MI300X ISA bridge](../wiki/languages/mi300x-isa-bridge.md)
- [CDNA3 ISA XML](../sources/amdgpu_isa_cdna3.xml)
