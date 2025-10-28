"""Factorial examples (recursive and iterative).

This module provides two implementations of factorial and a small demo when
run as a script.
"""


# Recursive factorial implementation
def factorial_recursive(n: int) -> int:
    """Compute n! recursively.

    - Raises ValueError for negative inputs.
    - Uses the mathematical definition:
        0! = 1
        n! = n * (n-1)!  for n > 0

    Note: recursion mirrors the definition but may hit Python's recursion
    limit for large n.
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


# Iterative factorial implementation
def factorial_iterative(n: int) -> int:
    """Compute n! using an iterative loop.

    - Raises ValueError for negative inputs.
    - Preferred for large n to avoid recursion limits and overhead.
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # Quick demo of both implementations
    samples = [0, 1, 5, 10]
    print("Factorial demo (recursive vs iterative):")
    for s in samples:
        print(f"{s}! = {factorial_recursive(s)}  (recursive)")
        print(f"{s}! = {factorial_iterative(s)}  (iterative)")
