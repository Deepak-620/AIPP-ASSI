"""
Prompt (you can paste this into an AI/code generator):

"Write a Python function named `fibonacci(n)` that calculates the nth Fibonacci
number using recursion. Include: 1) a clear docstring describing parameters,
return value, base cases, and constraints; 2) input validation with helpful
errors; 3) inline comments explaining the recursive relation; and 4) a brief
explanatory note summarizing how the recursion works."
"""

from typing import Final


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using a simple recursive approach.

    Definition:
    - Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...
    - Formally: F(0) = 0, F(1) = 1, and for n >= 2, F(n) = F(n-1) + F(n-2)

    Parameters:
    - n: Zero-based index (int). Must be a non-negative integer.

    Returns:
    - The nth Fibonacci number (int).

    Raises:
    - TypeError: If n is not an integer.
    - ValueError: If n is negative.

    Notes:
    - This implementation uses plain recursion for clarity/education.
      Its time complexity is exponential (approximately O(phi^n)). For
      large n, consider memoization or an iterative approach.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    # Base cases directly return known values without further recursion.
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case: decompose F(n) into subproblems F(n-1) and F(n-2)
    # and add their results. The recursion bottoms out at the base cases.
    return fibonacci(n - 1) + fibonacci(n - 2)


# Short explanatory note (displayed when run directly)
EXPLANATION: Final[str] = (
    "This program defines a recursive function `fibonacci(n)` that uses the base\n"
    "cases F(0)=0 and F(1)=1. For any n>=2, it calls itself to compute F(n-1)\n"
    "and F(n-2), then returns their sum. This mirrors the mathematical\n"
    "definition of the Fibonacci sequence."
)


if __name__ == "__main__":
    # Simple CLI interaction for quick testing
    try:
        value_str = input("Enter a non-negative integer n: ")
        value = int(value_str)
        print(f"F({value}) = {fibonacci(value)}")
        print()
        print(EXPLANATION)
    except Exception as exc:  # surface helpful error messages
        print(f"Error: {exc}")


