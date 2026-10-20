# Temporal fusion, alignment and memory

**Status: concept syllabus / no code implemented.**

## Key questions
- When does a frame-by-frame perception model fail to preserve identity or recover occluded information?
- How should temporal features be aligned under ego-motion and coordinate changes?
- What are simple averaging, recurrent state, temporal attention and feature memory good for?
- What are the risks of stale features, latency and distribution shift?

## Minimal exercise (future)
1. Create a 2-frame synthetic moving-object example.
2. Compare independent-frame estimates with a simple aligned temporal fusion baseline.
3. Inject noise, occlusion or time offset while controlling other inputs.
4. Trace historical features in one pinned BEVFormer variant and formulate an ablation.

**Use in:** [009 Camera frames](../../experiments/03-spatial-ai/009-camera-projection-and-frames/README.md), BEVFormer, SAM 2 and world-model studies.

**Evidence to add:** coordinate convention, alignment algorithm, false-positive/latency tradeoff, failure analysis.
