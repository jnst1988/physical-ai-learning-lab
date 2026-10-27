# Open-source model studies

**Priority update:** This is a supporting study track. Use it as a just-in-time foundation for the primary [Physical AI video/world-model and VLA track](../07-video-world-models-and-vlam/README.md).

**Status: learning framework only.** This stage complements, rather than replaces, Experiments 001–016.

## Two complementary learning loops

| Fundamentals: build a mechanism | Model studies: investigate a real system |
| --- | --- |
| Derive, implement and test a minimal component | Reproduce a documented upstream inference or training baseline |
| Understand gradients, detection metrics, camera geometry and attention | Trace architecture and tensors, form a falsifiable hypothesis, run controlled changes |
| Small deterministic examples; lightweight dependencies | Versioned upstream weights, data, environment, evaluation and deployment |
| No prerequisite to finish *all* fundamentals first | Learn foundations just in time, then return to the upstream model |

**Start:** [017 — YOLO](017-yolo/README.md). It is a *scaffold*: no official model has been installed, trained, evaluated, or benchmarked in this repository.

## Curated bridge: perception to Physical AI

YOLO is a useful first full-model study, but it covers only object detection. To understand the transition from autonomous-driving perception to general Physical AI, the next studies should add temporal identity, object masks, geometry and action-relevant scene representations. The robotics track then uses those representations in a shared task, tests VLA/world-model policies, and closes the loop with measured actions.

| Priority / placeholder | Capability and learning question | Candidate reference | Connects to | State |
| --- | --- | --- | --- | --- |
| Done first / 017 | **Object detection:** what do boxes, confidence thresholds and NMS expose or hide? | [YOLO11](017-yolo/references.md) | 005–006; CNN features | Scaffold and runner exist; real inference pending |
| P1 / next | **Video tracking:** how do detections become stable object identities over time, and how do ID switches affect downstream decisions? | ByteTrack or BoT-SORT | 006; temporal fusion; video observation contracts in 018 | Placeholder only |
| P1 / next | **Promptable segmentation:** can an object be followed as a pixel mask through a video, and where does tracking drift? | SAM 2 | 007; temporal fusion; robot visual observations | Placeholder only |
| P2 / later | **Depth and 3D geometry:** which scale and calibration assumptions are needed to turn image evidence into useful spatial measurements? | Depth Anything V2, paired with calibrated geometry | 008–011; camera/robot frames | Placeholder only |
| P2 / later | **Driving-scene BEV / occupancy:** how are multi-camera observations fused into a spatial state useful for prediction and planning, and what transfers to robotics? | BEVFormer or a smaller occupancy baseline | 009, 012; temporal fusion; world models | Placeholder only |

These are capability placeholders, not a commitment to reproduce every named model. Prefer one model per missing capability, select an upstream revision and verify its license/compute needs when starting the work. Do not add empty directories, notebooks or implied results. In particular, Grounding DINO, SparseDrive and FoundationPose remain optional references: add them only if a concrete question remains after the core bridge above.

The intended connection is **image detection → temporal object state → masks and geometry → spatial/occupancy representation → VLA or video-world-model policy → closed-loop task evaluation**. The autonomous-driving domain supplies mature perception problems and evaluation habits; the Physical AI path tests which ideas transfer to robots and which depend on vehicle-specific sensors or labels.

## How to contribute a model study

1. Copy the [model-study template](../../templates/model-study/README.md), then define the versioned upstream model and license.
2. Write questions, a baseline protocol and measurable hypotheses **before** running.
3. Record source revision, dataset rights/splits, weights terms, Python/dependency versions, hardware, seed, command, metrics and failures.
4. Keep third-party repositories as external references or independent checkouts; do **not** copy upstream source into this MIT-licensed repository by default.
5. Publish only small permitted example artifacts and summaries, clearly marking *planned* versus *measured*.
