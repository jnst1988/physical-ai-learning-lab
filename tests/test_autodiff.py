import math
import pytest
from learning_lab.autodiff import Scalar
from learning_lab.experiment001 import fit


def test_shared_leaf_and_repeated_backward():
    x = Scalar(3)
    y = x*x + x*x + 2*x
    y.backward()
    assert x.grad == 14
    y.backward()
    assert x.grad == 14


def test_shared_intermediate():
    x = Scalar(2)
    a = x*x
    y = a*a + a
    y.backward()
    assert x.grad == 36


@pytest.mark.parametrize("v", [-1.3, -0.2, 0.4, 2.0])
def test_finite_difference(v):
    def f(x):
        return ((x*x + 0.3*x).tanh() / (x*x + 2) - 2/x)**2
    x = Scalar(v)
    y = f(x)
    y.backward()
    h = 1e-6
    numerical = (f(Scalar(v+h)).value - f(Scalar(v-h)).value)/(2*h)
    assert x.grad == pytest.approx(numerical, rel=1e-5, abs=1e-6)


def test_constants_and_reverse_operators():
    x = Scalar(2)
    y = 4/x + (3-x) + x**0
    y.backward()
    assert y.value == 4
    assert x.grad == -2
    z = Scalar(0)
    (z**0).backward()
    assert z.grad == 0


def test_domains():
    with pytest.raises(ZeroDivisionError):
        1/Scalar(0)
    with pytest.raises(TypeError):
        Scalar(2)**Scalar(2)


def test_deep_graph():
    x = Scalar(1)
    y = x
    for _ in range(2000):
        y = y + 1
    y.backward()
    assert x.grad == 1


def test_training_converges():
    w, b, losses = fit()
    assert all(math.isfinite(v) for v in losses)
    assert losses[-1] < 1e-8
    assert w == pytest.approx(2, abs=1e-4)
    assert b == pytest.approx(1, abs=1e-4)
