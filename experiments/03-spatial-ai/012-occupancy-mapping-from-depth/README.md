# Experiment 012: Occupancy Mapping from Depth

**Status: scaffold — algorithm not implemented; no experimental results collected.**

## Goal
How can depth observations become a spatial map?

## Prerequisites
[008](../../02-perception/008-depth-and-scale-ambiguity/README.md), [009](../../03-spatial-ai/009-camera-projection-and-frames/README.md), [011](../../03-spatial-ai/011-pose-estimation-and-reprojection/README.md). Read the upstream experiments and explain their exit criteria before starting this one. See the [full curriculum](../../../docs/curriculum.md).

## Hypothesis
Combining consistent observations recovers more occupied cells than a single view in a synthetic scene.

## Architecture
Known poses and depth rays -> world coordinates -> bounded occupancy grid -> map evaluation.

Keep reusable mechanisms in `src/learning_lab/`; put experiment-specific orchestration here only when implemented. Sketch the interfaces, shapes, units, and assumptions in `learning.ipynb` first.

## Data and environment
Start with locally generated synthetic data. Record generation parameters, splits, seeds, and units. No dataset, model weights, third-party code, or new dependencies have been added for this scaffold. Review provenance and licenses before adding external materials; record any new dependency with uv and commit the updated lockfile.

## Reproduction
From the repository root:

```sh
uv sync --locked
uv run jupyter lab
```

Open `experiments/03-spatial-ai/012-occupancy-mapping-from-depth/learning.ipynb`. This currently opens a planning exercise, not a working implementation. `config.json` records the proposed protocol; it is not yet consumed by a runner. Do not report an experiment as reproduced until you add a runnable entry point, exact command, and meaningful tests.

## Baseline and metrics
**Baseline:** Single-view grid with identical resolution.

**Metrics:** Occupied-cell IoU, observed coverage, and grid memory.

## Validation and completion criteria
Define free, occupied, and unknown separately; test a wall scene and keep evaluation bounds fixed across methods.

Add independent checks for the core mechanism, then run the baseline and proposed method under identical conditions. The original Experiment 001 tests do not validate this experiment. Follow the [completion checklist](../../../docs/curriculum.md#completion-checklist).

## Controlled experiment
Vary grid resolution and then pose noise in separate runs.

Predict the outcome before running. Record the actual configuration and each run in [results.md](results.md), including negative or inconclusive outcomes.

## Results
Not run. No measurements or claimed improvements exist yet. [Results worksheet](results.md).

## Lessons learned
To be completed by the learner after implementation and measurement. Separate observations from explanations and link supporting evidence in the [learning journal](../../../docs/learning-journal.md).

## Limitations
Known poses bypass SLAM; unknown cells must not silently count as free.

## Next steps
Complete this experiment's validation and reflection, then continue to [013](../../04-physical-ai/013-deterministic-simulation-loop/README.md).

## References and provenance
No third-party implementation is included. Add exact upstream URLs, revisions, licenses, and the role of each reference before adopting external material. Follow [provenance policy](../../../docs/provenance.md).
