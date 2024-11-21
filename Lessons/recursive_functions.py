from __future__ import annotations


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("Cannot calculate factorial of a negative number.")
    else:
        return n * factorial(n - 1)
