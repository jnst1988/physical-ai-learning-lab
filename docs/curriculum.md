# Learning curriculum

## Scope and status

Experiment 001 is implemented and verified. Experiment 017 (YOLO) has a runnable first-inference script but no actual model run or measured YOLO results yet. Experiments 002–016 have goals, hypotheses, evaluation protocols, notebooks, configuration worksheets, and result templates. Their algorithms have not been implemented or evaluated. Creating a scaffold is not evidence that the learner has completed it.

## Sequence

| Experiment | Prerequisites | Status |
| --- | --- | --- |
| [001: Backpropagation from Scratch](../experiments/01-ml-fundamentals/001-backpropagation-from-scratch/README.md) | None | Implemented |
| [002: MLP from Scratch](../experiments/01-ml-fundamentals/002-mlp-from-scratch/README.md) | 001 | Scaffold |
| [003: Optimization and Gradient Checking](../experiments/01-ml-fundamentals/003-optimization-and-gradient-checking/README.md) | 001, 002 | Scaffold |
| [004: Generalization and Data Splits](../experiments/01-ml-fundamentals/004-generalization-and-data-splits/README.md) | 002, 003 | Scaffold |
| [005: Image Classification Pipeline](../experiments/02-perception/005-image-classification-pipeline/README.md) | 002, 004 | Scaffold |
| [006: Detection, IoU, and NMS](../experiments/02-perception/006-detection-iou-and-nms/README.md) | 005 | Scaffold |
| [007: Segmentation and Mask Metrics](../experiments/02-perception/007-segmentation-and-mask-metrics/README.md) | 005, 006 | Scaffold |
| [008: Depth and Scale Ambiguity](../experiments/02-perception/008-depth-and-scale-ambiguity/README.md) | 004, 005 | Scaffold |
| [009: Camera Projection and Coordinate Frames](../experiments/03-spatial-ai/009-camera-projection-and-frames/README.md) | 008 | Scaffold |
| [010: Point Cloud Alignment](../experiments/03-spatial-ai/010-point-cloud-alignment/README.md) | 009 | Scaffold |
| [011: Pose Estimation and Reprojection](../experiments/03-spatial-ai/011-pose-estimation-and-reprojection/README.md) | 009, 010 | Scaffold |
| [012: Occupancy Mapping from Depth](../experiments/03-spatial-ai/012-occupancy-mapping-from-depth/README.md) | 008, 009, 011 | Scaffold |
| [013: Deterministic Simulation Loop](../experiments/04-physical-ai/013-deterministic-simulation-loop/README.md) | 003, 009 | Scaffold |
| [014: Feedback Control and Tracking](../experiments/04-physical-ai/014-feedback-control-and-tracking/README.md) | 012, 013 | Scaffold |
| [015: Behavior Cloning and Distribution Shift](../experiments/04-physical-ai/015-behavior-cloning-and-distribution-shift/README.md) | 004, 014 | Scaffold |
| [016: Closed-Loop Evaluation and Failure Analysis](../experiments/04-physical-ai/016-closed-loop-evaluation-and-failure-analysis/README.md) | 012, 014, 015 | Scaffold |

The four fundamentals stages build from differentiable mechanisms to representation, geometry, and closed-loop behavior. A prerequisite means you should explain and validate its key idea before progressing; it is not a claim that future code already imports it. Experiment 014 explicitly connects the mapping and dynamics tracks; 016 reconnects perception uncertainty with policy evaluation.

## How to use each framework

1. Read the question and prerequisite experiments. Predict a result before writing code.
2. Open the experiment notebook and derive one tiny example by hand.
3. Implement the minimum mechanism, starting with synthetic data and an independent baseline.
4. Turn the proposed config into a real runner input, or replace it with a documented configuration format. Never imply unused settings affect execution.
5. Add independent correctness checks, execute the baseline and controlled change, and save actual measurements in results.md.
6. Explain what you learned in the notebook and journal, then update the status with evidence.

There are no deadline estimates; progress is based on demonstrated understanding and reproducibility.

## Completion checklist

- [ ] A runnable entry point and exact root-level command are documented.
- [ ] Data generation or download, provenance, splits, seeds, coordinate conventions, and units are explicit.
- [ ] Necessary dependencies are declared and the uv lockfile is updated.
- [ ] Independent analytic, numerical, or trusted-reference checks cover the mechanism and important edge cases.
- [ ] Baseline and proposed method use the same declared evaluation conditions.
- [ ] Results include actual measurements, failures, uncertainty, configuration, environment, and commit.
- [ ] Notebook executes cleanly in the locked environment; outputs support the written conclusions.
- [ ] Limitations and one next controlled experiment are recorded.
- [ ] The journal and indexes reflect the actual state; CI includes meaningful validation for the new implementation.

## Environment policy

Use the existing root uv project. No extra packages are required to read the frameworks or run their protocol-display cells. Add numerical, vision, or simulation packages only when an implemented experiment needs them. Keep large datasets, checkpoints, and generated artifacts outside Git; record enough information to reproduce them. License review is required before copying external code or introducing datasets or model weights.

## Complementary model-study track

**017 — [YOLO model study](../experiments/05-open-source-model-studies/017-yolo/README.md)** has a first-inference runner and offline tests; real YOLO inference and evaluation are pending. Its conceptual foundations are [005](../experiments/02-perception/005-image-classification-pipeline/README.md), [006](../experiments/02-perception/006-detection-iou-and-nms/README.md) and the [CNN note](concepts/cnn.md). Finish prerequisites just in time rather than blocking all model studies until 016.

Later model studies are listed in [05 Open-source Model Studies](../experiments/05-open-source-model-studies/README.md). Before BEVFormer, complete minimal [attention](concepts/attention.md) and [temporal-fusion](concepts/temporal-fusion.md) exercises plus [009 camera projection](../experiments/03-spatial-ai/009-camera-projection-and-frames/README.md).

For external projects, use the [model-study template](../templates/model-study/README.md) to distinguish reproduction, architecture inspection, controlled ablation, modification and deployment. Do not equate a template with a successful run, and do not vendor upstream source or weights by default. MLflow, DVC, Hugging Face demos and GitHub Pages remain optional later enhancements; no service is required for this scaffolding.
