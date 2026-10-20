# Experiment 003: Optimization and Gradient Checking

**Status: scaffold — algorithm not implemented; no experimental results collected.**

## Goal
How do step size and scaling affect optimization?

## Prerequisites
[001](../../01-ml-fundamentals/001-backpropagation-from-scratch/README.md), [002](../../01-ml-fundamentals/002-mlp-from-scratch/README.md). Read the upstream experiments and explain their exit criteria before starting this one. See the [full curriculum](../../../docs/curriculum.md).

## Hypothesis
A moderate step size converges on a quadratic while an overly large step size diverges.

## Architecture
Analytic quadratic -> autodiff gradient -> optimizer update -> loss trajectory.

Keep reusable mechanisms in `src/learning_lab/`; put experiment-specific orchestration here only when implemented. Sketch the interfaces, shapes, units, and assumptions in `learning.ipynb` first.

## Data and environment
Start with locally generated synthetic data. Record generation parameters, splits, seeds, and units. No dataset, model weights, third-party code, or new dependencies have been added for this scaffold. Review provenance and licenses before adding external materials; record any new dependency with uv and commit the updated lockfile.

## Reproduction
From the repository root:

```sh
uv sync --locked
uv run jupyter lab
```

Open `experiments/01-ml-fundamentals/003-optimization-and-gradient-checking/learning.ipynb`. This currently opens a planning exercise, not a working implementation. `config.json` records the proposed protocol; it is not yet consumed by a runner. Do not report an experiment as reproduced until you add a runnable entry point, exact command, and meaningful tests.

## Baseline and metrics
**Baseline:** Closed-form derivative and minimizer.

**Metrics:** Distance to minimizer, gradient error, and loss per update.

## Validation and completion criteria
Match the analytic gradient within 1e-6 absolute error; show one convergent and one divergent trajectory with the same starting point.

Add independent checks for the core mechanism, then run the baseline and proposed method under identical conditions. The original Experiment 001 tests do not validate this experiment. Follow the [completion checklist](../../../docs/curriculum.md#completion-checklist).

## Controlled experiment
Compare rates 0.01, 0.1, and 1.0 on f(x)=x*x, starting at x=3.

Predict the outcome before running. Record the actual configuration and each run in [results.md](results.md), including negative or inconclusive outcomes.

## Results
Not run. No measurements or claimed improvements exist yet. [Results worksheet](results.md).

## Lessons learned
To be completed by the learner after implementation and measurement. Separate observations from explanations and link supporting evidence in the [learning journal](../../../docs/learning-journal.md).

## Limitations
Conclusions on a convex quadratic need not transfer to neural networks.

## Next steps
Complete this experiment's validation and reflection, then continue to [004](../../01-ml-fundamentals/004-generalization-and-data-splits/README.md).

## References and provenance
No third-party implementation is included. Add exact upstream URLs, revisions, licenses, and the role of each reference before adopting external material. Follow [provenance policy](../../../docs/provenance.md).
