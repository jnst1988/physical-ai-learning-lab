"""Run with: uv run python -m learning_lab.experiment001."""
from learning_lab.autodiff import Scalar


def fit(steps=100, rate=0.1):
    """Fit y=2x+1 on four fixed points using mean squared error."""
    weight, bias = Scalar(0), Scalar(0)
    samples = [(-1, -1), (0, 1), (1, 3), (2, 5)]
    losses = []
    for _ in range(steps):
        loss = sum((weight * x + bias - y) ** 2 for x, y in samples) / len(samples)
        losses.append(loss.value)
        loss.backward()
        # New leaves keep old graph values and local derivatives consistent.
        weight = Scalar(weight.value - rate * weight.grad)
        bias = Scalar(bias.value - rate * bias.grad)
    return weight.value, bias.value, losses


def main():
    x = Scalar(3)
    result = x * x + 2 * x + 1
    result.backward()
    print(f"f(3)={result.value:.1f}; df/dx={x.grad:.1f} (expected 16 and 8)")
    weight, bias, losses = fit()
    print(f"MSE: {losses[0]:.8f} -> {losses[-1]:.8g}")
    print(f"weight={weight:.6f}, bias={bias:.6f} (targets 2 and 1)")


if __name__ == "__main__":
    main()
