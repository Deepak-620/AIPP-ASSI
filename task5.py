"""Utilities for simple list operations.

This file demonstrates two ways to find the largest number in a list:
- an explicit iterative implementation (O(n) time, O(1) extra space)
- a thin wrapper around Python's built-in max() (also O(n) time)

Both implementations validate input and handle common edge cases.
"""

from typing import Iterable, Optional


def find_max_iterative(nums: Iterable[float]) -> float:
    """Return the largest value in nums using an explicit iteration.

    Raises ValueError if `nums` is empty.

    Complexity: O(n) time, O(1) extra space.
    """
    iterator = iter(nums)
    try:
        largest = next(iterator)
    except StopIteration:
        raise ValueError("find_max_iterative() arg is an empty iterable")

    for x in iterator:
        # no special casing needed: numeric comparisons work for int/float
        if x > largest:
            largest = x
    return largest


def find_max_builtin(nums: Iterable[float]) -> float:
    """Return the largest value in nums using Python's built-in max().

    This is the concise, idiomatic approach. It raises ValueError on empty
    iterables as well.

    Complexity: O(n) time, O(1) extra space (implementation dependent).
    """
    return max(nums)


def _demo() -> None:
    samples = [
        [3, 1, 4, 1, 5, 9, 2],
        [-10, -3, -20, -1],
        [42],
    ]

    print("Demo: find largest in lists")
    for s in samples:
        print("list:", s)
        print("  iterative ->", find_max_iterative(s))
        print("  builtin   ->", find_max_builtin(s))


if __name__ == "__main__":
    _demo()
