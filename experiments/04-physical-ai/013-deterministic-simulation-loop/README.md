# Experiment 013: Deterministic Simulation Loop

**Status: scaffold — algorithm not implemented; no experimental results collected.**

## Goal
What must be recorded to reproduce a dynamical rollout?

## Prerequisites
[003](../../01-ml-fundamentals/003-optimization-and-gradient-checking/README.md), [009](../../03-spatial-ai/009-camera-projection-and-frames/README.md). Read the upstream experiments and explain their exit criteria before starting this one. See the [full curriculum](../../../docs/curriculum.md).

## Hypothesis
A fixed-step point-mass simulator reproduces trajectories for identical state and action sequences.

## Architecture
Initial state -> bounded action -> fixed-step integration -> observation -> trajectory log.

Keep reusable mechanisms in `src/learning_lab/`; put experiment-specific orchestration here only when implemented. Sketch the interfaces, shapes, units, and assumptions in `learning.ipynb` first.

## Data and environment
Start with locally generated synthetic data. Record generation parameters, splits, seeds, and units. No dataset, model weights, third-party code, or new dependencies have been added for this scaffold. Review provenance and licenses before adding external materials; record any new dependency with uv and commit the updated lockfile.

## Reproduction
From the repository root:

```sh
uv sync --locked
uv run jupyter lab
```

Open `experiments/04-physical-ai/013-deterministic-simulation-loop/learning.ipynb`. This currently opens a planning exercise, not a working implementation. `config.json` records the proposed protocol; it is not yet consumed by a runner. Do not report an experiment as reproduced until you add a runnable entry point, exact command, and meaningful tests.

## Baseline and metrics
**Baseline:** Analytic constant-velocity or constant-acceleration trajectory.

**Metrics:** Trajectory error, repeatability, and step count.

## Validation and completion criteria
Verify zero-force motion and a documented integration-error bound; identical reruns must match within the declared tolerance.

Add independent checks for the core mechanism, then run the baseline and proposed method under identical conditions. The original Experiment 001 tests do not validate this experiment. Follow the [completion checklist](../../../docs/curriculum.md#completion-checklist).

## Controlled experiment
Halve the time step while keeping simulated duration and forces fixed.

Predict the outcome before running. Record the actual configuration and each run in [results.md](results.md), including negative or inconclusive outcomes.

## Results
Not run. No measurements or claimed improvements exist yet. [Results worksheet](results.md).

## Lessons learned
To be completed by the learner after implementation and measurement. Separate observations from explanations and link supporting evidence in the [learning journal](../../../docs/learning-journal.md).

## Limitations
A toy simulator is not evidence of hardware fidelity.

## Next steps
Complete this experiment's validation and reflection, then continue to [014](../../04-physical-ai/014-feedback-control-and-tracking/README.md).

## References and provenance
No third-party implementation is included. Add exact upstream URLs, revisions, licenses, and the role of each reference before adopting external material. Follow [provenance policy](../../../docs/provenance.md).
