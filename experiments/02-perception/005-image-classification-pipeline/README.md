# Experiment 005: Image Classification Pipeline

**Status: scaffold — algorithm not implemented; no experimental results collected.**

## Goal
What makes an image training pipeline trustworthy?

## Prerequisites
[002](../../01-ml-fundamentals/002-mlp-from-scratch/README.md), [004](../../01-ml-fundamentals/004-generalization-and-data-splits/README.md). Read the upstream experiments and explain their exit criteria before starting this one. See the [full curriculum](../../../docs/curriculum.md).

## Hypothesis
A small model will beat a majority-class baseline on synthetic held-out shape images.

## Architecture
Seeded shape renderer -> split by source scene -> normalization from training data -> classifier -> confusion matrix.

Keep reusable mechanisms in `src/learning_lab/`; put experiment-specific orchestration here only when implemented. Sketch the interfaces, shapes, units, and assumptions in `learning.ipynb` first.

## Data and environment
Start with locally generated synthetic data. Record generation parameters, splits, seeds, and units. No dataset, model weights, third-party code, or new dependencies have been added for this scaffold. Review provenance and licenses before adding external materials; record any new dependency with uv and commit the updated lockfile.

## Reproduction
From the repository root:

```sh
uv sync --locked
uv run jupyter lab
```

Open `experiments/02-perception/005-image-classification-pipeline/learning.ipynb`. This currently opens a planning exercise, not a working implementation. `config.json` records the proposed protocol; it is not yet consumed by a runner. Do not report an experiment as reproduced until you add a runnable entry point, exact command, and meaningful tests.

## Baseline and metrics
**Baseline:** Majority-class predictor using training frequencies.

**Metrics:** Accuracy, per-class recall, and confusion matrix.

## Validation and completion criteria
Check tensor shapes, label mapping, and split disjointness; report all per-class metrics against the baseline.

Add independent checks for the core mechanism, then run the baseline and proposed method under identical conditions. The original Experiment 001 tests do not validate this experiment. Follow the [completion checklist](../../../docs/curriculum.md#completion-checklist).

## Controlled experiment
Add controlled image noise after freezing the split.

Predict the outcome before running. Record the actual configuration and each run in [results.md](results.md), including negative or inconclusive outcomes.

## Results
Not run. No measurements or claimed improvements exist yet. [Results worksheet](results.md).

## Lessons learned
To be completed by the learner after implementation and measurement. Separate observations from explanations and link supporting evidence in the [learning journal](../../../docs/learning-journal.md).

## Limitations
Synthetic shape recognition does not establish natural-image performance.

## Next steps
Complete this experiment's validation and reflection, then continue to [006](../../02-perception/006-detection-iou-and-nms/README.md).

## References and provenance
No third-party implementation is included. Add exact upstream URLs, revisions, licenses, and the role of each reference before adopting external material. Follow [provenance policy](../../../docs/provenance.md).
