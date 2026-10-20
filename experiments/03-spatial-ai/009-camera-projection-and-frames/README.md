# Experiment 009: Camera Projection and Coordinate Frames

**Status: scaffold — algorithm not implemented; no experimental results collected.**

## Goal
How do camera intrinsics and rigid transforms map 3D points to pixels?

## Prerequisites
[008](../../02-perception/008-depth-and-scale-ambiguity/README.md). Read the upstream experiments and explain their exit criteria before starting this one. See the [full curriculum](../../../docs/curriculum.md).

## Hypothesis
Projection and backprojection recover a visible point when its depth and conventions are known.

## Architecture
World point -> rigid world-to-camera transform -> pinhole projection -> pixel plus depth -> backprojection.

Keep reusable mechanisms in `src/learning_lab/`; put experiment-specific orchestration here only when implemented. Sketch the interfaces, shapes, units, and assumptions in `learning.ipynb` first.

## Data and environment
Start with locally generated synthetic data. Record generation parameters, splits, seeds, and units. No dataset, model weights, third-party code, or new dependencies have been added for this scaffold. Review provenance and licenses before adding external materials; record any new dependency with uv and commit the updated lockfile.

## Reproduction
From the repository root:

```sh
uv sync --locked
uv run jupyter lab
```

Open `experiments/03-spatial-ai/009-camera-projection-and-frames/learning.ipynb`. This currently opens a planning exercise, not a working implementation. `config.json` records the proposed protocol; it is not yet consumed by a runner. Do not report an experiment as reproduced until you add a runnable entry point, exact command, and meaningful tests.

## Baseline and metrics
**Baseline:** Hand-calculated identity-camera example.

**Metrics:** Pixel reprojection error and 3D round-trip error.

## Validation and completion criteria
Require <1e-6 round-trip error for valid synthetic points; reject nonpositive camera depth; document units and transform direction.

Add independent checks for the core mechanism, then run the baseline and proposed method under identical conditions. The original Experiment 001 tests do not validate this experiment. Follow the [completion checklist](../../../docs/curriculum.md#completion-checklist).

## Controlled experiment
Vary focal length with the 3D scene fixed.

Predict the outcome before running. Record the actual configuration and each run in [results.md](results.md), including negative or inconclusive outcomes.

## Results
Not run. No measurements or claimed improvements exist yet. [Results worksheet](results.md).

## Lessons learned
To be completed by the learner after implementation and measurement. Separate observations from explanations and link supporting evidence in the [learning journal](../../../docs/learning-journal.md).

## Limitations
A pinhole model omits lens distortion and calibration noise.

## Next steps
Complete this experiment's validation and reflection, then continue to [010](../../03-spatial-ai/010-point-cloud-alignment/README.md).

## References and provenance
No third-party implementation is included. Add exact upstream URLs, revisions, licenses, and the role of each reference before adopting external material. Follow [provenance policy](../../../docs/provenance.md).
