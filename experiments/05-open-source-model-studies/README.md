# Open-source model studies

**Status: learning framework only.** This stage complements, rather than replaces, Experiments 001–016.

## Two complementary learning loops

| Fundamentals: build a mechanism | Model studies: investigate a real system |
| --- | --- |
| Derive, implement and test a minimal component | Reproduce a documented upstream inference or training baseline |
| Understand gradients, detection metrics, camera geometry and attention | Trace architecture and tensors, form a falsifiable hypothesis, run controlled changes |
| Small deterministic examples; lightweight dependencies | Versioned upstream weights, data, environment, evaluation and deployment |
| No prerequisite to finish *all* fundamentals first | Learn foundations just in time, then return to the upstream model |

**Start:** [017 — YOLO](017-yolo/README.md). It is a *scaffold*: no official model has been installed, trained, evaluated, or benchmarked in this repository.

## Planned studies (not yet created)

| Candidate | Foundation connections | Status |
| --- | --- | --- |
| 017 YOLO | 005 image classification, 006 IoU/NMS, [CNN](../../docs/concepts/cnn.md) | Scaffold exists |
| Grounding DINO | 006 detection, [attention](../../docs/concepts/attention.md) | Planned |
| SAM 2 | 007 segmentation, [temporal fusion](../../docs/concepts/temporal-fusion.md) | Planned |
| Depth Anything V2 | 008 monocular depth and scale | Planned |
| BEVFormer | 009 camera projection, [attention](../../docs/concepts/attention.md), [temporal fusion](../../docs/concepts/temporal-fusion.md) | Planned |
| SparseDrive | 3D scene representations, sparse queries, prediction | Planned |
| FoundationPose | 009–011 coordinate frames and pose | Planned |
| World models | 012 occupancy, 013 simulation, 015 behavior cloning | Planned |

Future studies receive directories only when active work begins. Avoid empty notebooks and fabricated results.

## How to contribute a model study

1. Copy the [model-study template](../../templates/model-study/README.md), then define the versioned upstream model and license.
2. Write questions, a baseline protocol and measurable hypotheses **before** running.
3. Record source revision, dataset rights/splits, weights terms, Python/dependency versions, hardware, seed, command, metrics and failures.
4. Keep third-party repositories as external references or independent checkouts; do **not** copy upstream source into this MIT-licensed repository by default.
5. Publish only small permitted example artifacts and summaries, clearly marking *planned* versus *measured*.
