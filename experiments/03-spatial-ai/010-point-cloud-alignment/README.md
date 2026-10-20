# Experiment 010: Point Cloud Alignment

**Status: scaffold — algorithm not implemented; no experimental results collected.**

## Goal
Can known correspondences recover a rigid transformation?

## Prerequisites
[009](../../03-spatial-ai/009-camera-projection-and-frames/README.md). Read the upstream experiments and explain their exit criteria before starting this one. See the [full curriculum](../../../docs/curriculum.md).

## Hypothesis
Rigid least-squares alignment recovers a known rotation and translation on nondegenerate noiseless points.

## Architecture
Synthetic 3D points -> known SE(3) transform -> correspondences -> rigid alignment -> residuals.

Keep reusable mechanisms in `src/learning_lab/`; put experiment-specific orchestration here only when implemented. Sketch the interfaces, shapes, units, and assumptions in `learning.ipynb` first.

## Data and environment
Start with locally generated synthetic data. Record generation parameters, splits, seeds, and units. No dataset, model weights, third-party code, or new dependencies have been added for this scaffold. Review provenance and licenses before adding external materials; record any new dependency with uv and commit the updated lockfile.

## Reproduction
From the repository root:

```sh
uv sync --locked
uv run jupyter lab
```

Open `experiments/03-spatial-ai/010-point-cloud-alignment/learning.ipynb`. This currently opens a planning exercise, not a working implementation. `config.json` records the proposed protocol; it is not yet consumed by a runner. Do not report an experiment as reproduced until you add a runnable entry point, exact command, and meaningful tests.

## Baseline and metrics
**Baseline:** Identity transformation.

**Metrics:** Point RMSE, rotation error, and translation error.

## Validation and completion criteria
Recover a proper rotation with determinant +1; verify noiseless errors below 1e-6 and report noisy cases separately.

Add independent checks for the core mechanism, then run the baseline and proposed method under identical conditions. The original Experiment 001 tests do not validate this experiment. Follow the [completion checklist](../../../docs/curriculum.md#completion-checklist).

## Controlled experiment
Add Gaussian point noise and vary its standard deviation.

Predict the outcome before running. Record the actual configuration and each run in [results.md](results.md), including negative or inconclusive outcomes.

## Results
Not run. No measurements or claimed improvements exist yet. [Results worksheet](results.md).

## Lessons learned
To be completed by the learner after implementation and measurement. Separate observations from explanations and link supporting evidence in the [learning journal](../../../docs/learning-journal.md).

## Limitations
Known correspondences are easier than full registration; collinear points are degenerate.

## Next steps
Complete this experiment's validation and reflection, then continue to [011](../../03-spatial-ai/011-pose-estimation-and-reprojection/README.md).

## References and provenance
No third-party implementation is included. Add exact upstream URLs, revisions, licenses, and the role of each reference before adopting external material. Follow [provenance policy](../../../docs/provenance.md).
