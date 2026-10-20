# Experiment 015: Behavior Cloning and Distribution Shift

**Status: scaffold — algorithm not implemented; no experimental results collected.**

## Goal
Why can low imitation loss fail in closed-loop rollouts?

## Prerequisites
[004](../../01-ml-fundamentals/004-generalization-and-data-splits/README.md), [014](../../04-physical-ai/014-feedback-control-and-tracking/README.md). Read the upstream experiments and explain their exit criteria before starting this one. See the [full curriculum](../../../docs/curriculum.md).

## Hypothesis
Behavior cloning has lower performance from shifted starting states than from demonstration-like states.

## Architecture
Toy controller demonstrations -> trajectory-level split -> supervised policy -> closed-loop evaluation.

Keep reusable mechanisms in `src/learning_lab/`; put experiment-specific orchestration here only when implemented. Sketch the interfaces, shapes, units, and assumptions in `learning.ipynb` first.

## Data and environment
Start with locally generated synthetic data. Record generation parameters, splits, seeds, and units. No dataset, model weights, third-party code, or new dependencies have been added for this scaffold. Review provenance and licenses before adding external materials; record any new dependency with uv and commit the updated lockfile.

## Reproduction
From the repository root:

```sh
uv sync --locked
uv run jupyter lab
```

Open `experiments/04-physical-ai/015-behavior-cloning-and-distribution-shift/learning.ipynb`. This currently opens a planning exercise, not a working implementation. `config.json` records the proposed protocol; it is not yet consumed by a runner. Do not report an experiment as reproduced until you add a runnable entry point, exact command, and meaningful tests.

## Baseline and metrics
**Baseline:** Expert controller and a constant-action policy.

**Metrics:** Held-out action MSE, rollout success rate, and horizon-normalized tracking error.

## Validation and completion criteria
Split whole trajectories; freeze the policy before evaluation; compare in-distribution and shifted starts over 20 declared seeds.

Add independent checks for the core mechanism, then run the baseline and proposed method under identical conditions. The original Experiment 001 tests do not validate this experiment. Follow the [completion checklist](../../../docs/curriculum.md#completion-checklist).

## Controlled experiment
Vary the amount of demonstration data with evaluation seeds held fixed.

Predict the outcome before running. Record the actual configuration and each run in [results.md](results.md), including negative or inconclusive outcomes.

## Results
Not run. No measurements or claimed improvements exist yet. [Results worksheet](results.md).

## Lessons learned
To be completed by the learner after implementation and measurement. Separate observations from explanations and link supporting evidence in the [learning journal](../../../docs/learning-journal.md).

## Limitations
Toy behavior cloning omits real sensing, contact, and deployment constraints.

## Next steps
Complete this experiment's validation and reflection, then continue to [016](../../04-physical-ai/016-closed-loop-evaluation-and-failure-analysis/README.md).

## References and provenance
No third-party implementation is included. Add exact upstream URLs, revisions, licenses, and the role of each reference before adopting external material. Follow [provenance policy](../../../docs/provenance.md).
