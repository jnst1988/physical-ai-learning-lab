# Experiment 006: Detection, IoU, and NMS

**Status: scaffold — algorithm not implemented; no experimental results collected.**

## Goal
How are object boxes matched and duplicate detections removed?

## Prerequisites
[005](../../02-perception/005-image-classification-pipeline/README.md). Read the upstream experiments and explain their exit criteria before starting this one. See the [full curriculum](../../../docs/curriculum.md).

## Hypothesis
NMS removes overlapping duplicate boxes while preserving separated objects.

## Architecture
Synthetic boxes and scores -> IoU -> score filtering -> NMS -> one-to-one ground-truth matching.

Keep reusable mechanisms in `src/learning_lab/`; put experiment-specific orchestration here only when implemented. Sketch the interfaces, shapes, units, and assumptions in `learning.ipynb` first.

## Data and environment
Start with locally generated synthetic data. Record generation parameters, splits, seeds, and units. No dataset, model weights, third-party code, or new dependencies have been added for this scaffold. Review provenance and licenses before adding external materials; record any new dependency with uv and commit the updated lockfile.

## Reproduction
From the repository root:

```sh
uv sync --locked
uv run jupyter lab
```

Open `experiments/02-perception/006-detection-iou-and-nms/learning.ipynb`. This currently opens a planning exercise, not a working implementation. `config.json` records the proposed protocol; it is not yet consumed by a runner. Do not report an experiment as reproduced until you add a runnable entry point, exact command, and meaningful tests.

## Baseline and metrics
**Baseline:** Keep every predicted box above the same score threshold.

**Metrics:** IoU, precision, recall at a declared IoU threshold, and retained-box count.

## Validation and completion criteria
Hand-check identical, disjoint, touching, and nested boxes; ensure one truth cannot match multiple predictions.

Add independent checks for the core mechanism, then run the baseline and proposed method under identical conditions. The original Experiment 001 tests do not validate this experiment. Follow the [completion checklist](../../../docs/curriculum.md#completion-checklist).

## Controlled experiment
Vary the NMS IoU threshold and report the precision/recall tradeoff.

Predict the outcome before running. Record the actual configuration and each run in [results.md](results.md), including negative or inconclusive outcomes.

## Results
Not run. No measurements or claimed improvements exist yet. [Results worksheet](results.md).

## Lessons learned
To be completed by the learner after implementation and measurement. Separate observations from explanations and link supporting evidence in the [learning journal](../../../docs/learning-journal.md).

## Limitations
This isolates postprocessing; no object detector is trained.

## Next steps
Complete this experiment's validation and reflection, then continue to [007](../../02-perception/007-segmentation-and-mask-metrics/README.md).

## References and provenance
No third-party implementation is included. Add exact upstream URLs, revisions, licenses, and the role of each reference before adopting external material. Follow [provenance policy](../../../docs/provenance.md).
