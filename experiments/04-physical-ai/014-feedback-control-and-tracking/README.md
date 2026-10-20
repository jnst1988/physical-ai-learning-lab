# Experiment 014: Feedback Control and Tracking

**Status: scaffold — algorithm not implemented; no experimental results collected.**

## Goal
How does feedback change response to disturbances?

## Prerequisites
[012](../../03-spatial-ai/012-occupancy-mapping-from-depth/README.md), [013](../../04-physical-ai/013-deterministic-simulation-loop/README.md). Read the upstream experiments and explain their exit criteria before starting this one. See the [full curriculum](../../../docs/curriculum.md).

## Hypothesis
A tuned feedback controller reduces tracking RMSE relative to a fixed open-loop action under a declared disturbance.

## Architecture
Target and observed state -> controller -> saturated action -> point-mass dynamics -> tracking error.

Keep reusable mechanisms in `src/learning_lab/`; put experiment-specific orchestration here only when implemented. Sketch the interfaces, shapes, units, and assumptions in `learning.ipynb` first.

## Data and environment
Start with locally generated synthetic data. Record generation parameters, splits, seeds, and units. No dataset, model weights, third-party code, or new dependencies have been added for this scaffold. Review provenance and licenses before adding external materials; record any new dependency with uv and commit the updated lockfile.

## Reproduction
From the repository root:

```sh
uv sync --locked
uv run jupyter lab
```

Open `experiments/04-physical-ai/014-feedback-control-and-tracking/learning.ipynb`. This currently opens a planning exercise, not a working implementation. `config.json` records the proposed protocol; it is not yet consumed by a runner. Do not report an experiment as reproduced until you add a runnable entry point, exact command, and meaningful tests.

## Baseline and metrics
**Baseline:** Fixed open-loop action evaluated on the same disturbance schedule.

**Metrics:** Tracking RMSE, overshoot, settling time, and saturation fraction.

## Validation and completion criteria
Report nominal and disturbed cases; enforce action limits; define settling band and deadline before tuning.

Add independent checks for the core mechanism, then run the baseline and proposed method under identical conditions. The original Experiment 001 tests do not validate this experiment. Follow the [completion checklist](../../../docs/curriculum.md#completion-checklist).

## Controlled experiment
Vary one controller gain at a time with the disturbance schedule fixed.

Predict the outcome before running. Record the actual configuration and each run in [results.md](results.md), including negative or inconclusive outcomes.

## Results
Not run. No measurements or claimed improvements exist yet. [Results worksheet](results.md).

## Lessons learned
To be completed by the learner after implementation and measurement. Separate observations from explanations and link supporting evidence in the [learning journal](../../../docs/learning-journal.md).

## Limitations
Simulator stability does not imply safe real-world control.

## Next steps
Complete this experiment's validation and reflection, then continue to [015](../../04-physical-ai/015-behavior-cloning-and-distribution-shift/README.md).

## References and provenance
No third-party implementation is included. Add exact upstream URLs, revisions, licenses, and the role of each reference before adopting external material. Follow [provenance policy](../../../docs/provenance.md).
