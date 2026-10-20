# Experiment 007: Segmentation and Mask Metrics

**Status: scaffold — algorithm not implemented; no experimental results collected.**

## Goal
Why can pixel accuracy hide poor segmentation?

## Prerequisites
[005](../../02-perception/005-image-classification-pipeline/README.md), [006](../../02-perception/006-detection-iou-and-nms/README.md). Read the upstream experiments and explain their exit criteria before starting this one. See the [full curriculum](../../../docs/curriculum.md).

## Hypothesis
An all-background prediction achieves high accuracy on sparse masks but low foreground IoU.

## Architecture
Synthetic foreground masks -> controlled prediction errors -> confusion counts -> IoU and Dice.

Keep reusable mechanisms in `src/learning_lab/`; put experiment-specific orchestration here only when implemented. Sketch the interfaces, shapes, units, and assumptions in `learning.ipynb` first.

## Data and environment
Start with locally generated synthetic data. Record generation parameters, splits, seeds, and units. No dataset, model weights, third-party code, or new dependencies have been added for this scaffold. Review provenance and licenses before adding external materials; record any new dependency with uv and commit the updated lockfile.

## Reproduction
From the repository root:

```sh
uv sync --locked
uv run jupyter lab
```

Open `experiments/02-perception/007-segmentation-and-mask-metrics/learning.ipynb`. This currently opens a planning exercise, not a working implementation. `config.json` records the proposed protocol; it is not yet consumed by a runner. Do not report an experiment as reproduced until you add a runnable entry point, exact command, and meaningful tests.

## Baseline and metrics
**Baseline:** All-background mask.

**Metrics:** Pixel accuracy, foreground IoU, and Dice.

## Validation and completion criteria
Verify perfect, empty, and disjoint mask cases; define the empty-union convention before comparing metrics.

Add independent checks for the core mechanism, then run the baseline and proposed method under identical conditions. The original Experiment 001 tests do not validate this experiment. Follow the [completion checklist](../../../docs/curriculum.md#completion-checklist).

## Controlled experiment
Vary foreground area while keeping the predictor fixed.

Predict the outcome before running. Record the actual configuration and each run in [results.md](results.md), including negative or inconclusive outcomes.

## Results
Not run. No measurements or claimed improvements exist yet. [Results worksheet](results.md).

## Lessons learned
To be completed by the learner after implementation and measurement. Separate observations from explanations and link supporting evidence in the [learning journal](../../../docs/learning-journal.md).

## Limitations
Metric behavior alone does not evaluate a segmentation model.

## Next steps
Complete this experiment's validation and reflection, then continue to [008](../../02-perception/008-depth-and-scale-ambiguity/README.md).

## References and provenance
No third-party implementation is included. Add exact upstream URLs, revisions, licenses, and the role of each reference before adopting external material. Follow [provenance policy](../../../docs/provenance.md).
