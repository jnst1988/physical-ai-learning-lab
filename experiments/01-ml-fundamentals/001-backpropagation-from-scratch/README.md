# Experiment 001: Backpropagation from Scratch

## Goal
Understand how the chain rule propagates a scalar loss through a computation graph, including shared nodes, and how gradients enable learning.

## Hypotheses
1. Autodiff returns f(3)=16 and f'(3)=8 for f(x)=x²+2x+1.
2. Gradients of a smooth composite expression match central finite differences within relative tolerance 1e-5 and absolute tolerance 1e-6.
3. Gradient descent on y=2x+1 with four fixed samples reaches MSE below 1e-8 in 100 updates at learning rate 0.1.

## Architecture
`Scalar` stores a value, a gradient, and parent/local-derivative pairs. Arithmetic constructs a directed acyclic graph. An iterative postorder traversal visits dependencies once; reverse traversal accumulates contributions from every edge, including repeated use of the same parent. The output gradient is seeded with 1. Each backward call resets reachable gradients. Training constructs fresh parameter leaves after every update.

Supported operations: addition, subtraction, multiplication, constant powers, division, and tanh. Implementation: `src/learning_lab/autodiff.py`; training: `src/learning_lab/experiment001.py`.

## Reproduction
From the repository root on CPU:

```sh
uv sync --locked
uv run python -m learning_lab.experiment001
uv run pytest -q
uv run jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=python3 --output-dir=artifacts experiments/01-ml-fundamentals/001-backpropagation-from-scratch/learning.ipynb
```

No random seed is needed: data and initial parameters are fixed. See `docs/validation.md` for actual environment and output.

## Results
The analytic example, finite-difference comparison, shared-node cases, repeated backward calls, deep graphs, and training are checked by tests. Actual measured outputs are in `docs/validation.md`; the notebook includes executable assertions and learning prompts.

## Lessons learned
Local derivatives are sufficient when combined in reverse graph order. A shared value can receive multiple contributions, so overwriting its gradient loses information. A successful derivative check tests the mechanism; successful training tests its interaction with updates. Numerical checks are approximate and need suitable step sizes.

## Limitations
This is a teaching engine: no tensors, batching, GPU, higher-order differentiation, or performance claims. Treat node values and parent edges as immutable after construction. Division by zero and undefined real powers are outside the valid domain. The tiny noiseless regression task establishes correctness on this example, not generalization or physical intelligence.

## Next steps
Predict and measure how learning rates 0.01, 0.1, and 1.0 change convergence. Then build a small MLP and compare its gradients to an independently chosen framework baseline.

## References
Conceptual inspiration: [micrograd](https://github.com/karpathy/micrograd). See [license and provenance review](../../../docs/provenance.md). All implementation here is original.
