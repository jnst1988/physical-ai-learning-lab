# Experiment 016: Closed-Loop Evaluation and Failure Analysis

**Status: scaffold — algorithm not implemented; no experimental results collected.**

## Goal
Does a policy remain effective when perception and dynamics change?

## Prerequisites
[012](../../03-spatial-ai/012-occupancy-mapping-from-depth/README.md), [014](../../04-physical-ai/014-feedback-control-and-tracking/README.md), [015](../../04-physical-ai/015-behavior-cloning-and-distribution-shift/README.md). Read the upstream experiments and explain their exit criteria before starting this one. See the [full curriculum](../../../docs/curriculum.md).

## Hypothesis
Controlled observation noise or delay exposes failures hidden by nominal evaluation.

## Architecture
Frozen policy -> observation perturbation -> dynamics -> outcome metrics -> categorized failures.

Keep reusable mechanisms in `src/learning_lab/`; put experiment-specific orchestration here only when implemented. Sketch the interfaces, shapes, units, and assumptions in `learning.ipynb` first.

## Data and environment
Start with locally generated synthetic data. Record generation parameters, splits, seeds, and units. No dataset, model weights, third-party code, or new dependencies have been added for this scaffold. Review provenance and licenses before adding external materials; record any new dependency with uv and commit the updated lockfile.

## Reproduction
From the repository root:

```sh
uv sync --locked
uv run jupyter lab
```

Open `experiments/04-physical-ai/016-closed-loop-evaluation-and-failure-analysis/learning.ipynb`. This currently opens a planning exercise, not a working implementation. `config.json` records the proposed protocol; it is not yet consumed by a runner. Do not report an experiment as reproduced until you add a runnable entry point, exact command, and meaningful tests.

## Baseline and metrics
**Baseline:** Nominal observations with the exact same initial states and seeds.

**Metrics:** Success rate with confidence interval, tracking error, and failure-category counts.

## Validation and completion criteria
Evaluate 20 fixed seeds per condition; predeclare success, failure, timeout, and episode horizon; include every failed rollout.

Add independent checks for the core mechanism, then run the baseline and proposed method under identical conditions. The original Experiment 001 tests do not validate this experiment. Follow the [completion checklist](../../../docs/curriculum.md#completion-checklist).

## Controlled experiment
Vary noise, delay, or mass mismatch one factor at a time.

Predict the outcome before running. Record the actual configuration and each run in [results.md](results.md), including negative or inconclusive outcomes.

## Results
Not run. No measurements or claimed improvements exist yet. [Results worksheet](results.md).

## Lessons learned
To be completed by the learner after implementation and measurement. Separate observations from explanations and link supporting evidence in the [learning journal](../../../docs/learning-journal.md).

## Limitations
Synthetic robustness results are not a certification of physical-system safety.

## Next steps
Complete this experiment's validation and reflection, then continue to Propose a new experiment after reviewing the full evaluation evidence..

## References and provenance
No third-party implementation is included. Add exact upstream URLs, revisions, licenses, and the role of each reference before adopting external material. Follow [provenance policy](../../../docs/provenance.md).
