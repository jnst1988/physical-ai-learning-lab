"""Original scalar reverse-mode autodiff implementation; no ML dependencies."""
import math


class Scalar:
    """A real scalar and its local vector-Jacobian products.

    backward() clears the reachable graph before computing a fresh derivative.
    Gradients accumulate across graph branches, not across backward() calls.
    """

    def __init__(self, value, parents=()):
        self.value = float(value)
        self.grad = 0.0
        self.parents = tuple(parents)  # (parent, local derivative)

    @staticmethod
    def wrap(value):
        return value if isinstance(value, Scalar) else Scalar(value)

    def __add__(self, other):
        other = self.wrap(other)
        return Scalar(self.value + other.value, ((self, 1.0), (other, 1.0)))

    __radd__ = __add__

    def __mul__(self, other):
        other = self.wrap(other)
        return Scalar(self.value * other.value,
                      ((self, other.value), (other, self.value)))

    __rmul__ = __mul__

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + -self.wrap(other)

    def __rsub__(self, other):
        return self.wrap(other) - self

    def __pow__(self, exponent):
        if not isinstance(exponent, (int, float)):
            raise TypeError("Only constant real exponents are supported")
        value = self.value ** exponent
        # x**0 is constant, including at x=0.
        slope = 0.0 if exponent == 0 else exponent * self.value ** (exponent - 1)
        return Scalar(value, ((self, slope),))

    def __truediv__(self, other):
        return self * self.wrap(other) ** -1

    def __rtruediv__(self, other):
        return self.wrap(other) / self

    def tanh(self):
        value = math.tanh(self.value)
        return Scalar(value, ((self, 1 - value * value),))

    def backward(self):
        # Iterative postorder traversal avoids Python recursion limits.
        ordered, visited = [], set()
        stack = [(self, False)]
        while stack:
            node, expanded = stack.pop()
            if expanded:
                ordered.append(node)
            elif node not in visited:
                visited.add(node)
                stack.append((node, True))
                stack.extend((parent, False) for parent, _ in node.parents)
        for node in ordered:
            node.grad = 0.0
        self.grad = 1.0
        for node in reversed(ordered):
            for parent, slope in node.parents:
                parent.grad += node.grad * slope
