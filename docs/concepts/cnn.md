# CNN, receptive fields and feature hierarchies

**Status: concept syllabus / no code implemented.**

## Key questions
- What does a convolution kernel share across image locations, and what is the output shape after stride and padding?
- How do receptive fields and feature-map resolution evolve through a backbone?
- Why do detectors aggregate multi-scale features in a *neck* before prediction heads?
- Which architectural details are specific to the selected YOLO version?

## Minimal exercise (future)
1. Compute one convolution output element by hand and verify numerically.
2. Visualize tensor shapes and receptive field across a small CNN.
3. Trace *one pinned* YOLO implementation's backbone → neck → head, without assuming that all YOLO versions use the same structure.

**Use in:** [005 Classification](../../experiments/02-perception/005-image-classification-pipeline/README.md), [017 YOLO](../../experiments/05-open-source-model-studies/017-yolo/README.md).

**Evidence to add:** small input/output example, unit test, architecture sketch, failure cases, first controlled experiment.
