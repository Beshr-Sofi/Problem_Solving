"""Tribonacci sequence (T0=0, T1=1, T2=1) implementation.

This module provides a memoized (top-down DP) implementation of the
Tribonacci sequence. It returns the n-th Tribonacci number using recursion
with caching to avoid repeated work.
"""

from typing import Dict, Optional


def tribonacci(n: int, memo: Optional[Dict[int, int]] = None) -> int:
    """
    Compute the n-th Tribonacci number.

    The Tribonacci sequence is defined as:
        T0 = 0, T1 = 1, T2 = 1
        Tn = Tn-1 + Tn-2 + Tn-3  for n >= 3

    Args:
        n: Non-negative integer index of the Tribonacci sequence.
        memo: Optional dictionary to use for memoization. If None, a new
              dictionary initialized with base cases will be used.

    Returns:
        The n-th Tribonacci number as an integer.

    Example:
        >>> tribonacci(4)
        4

    Complexity:
        Time: O(n) — each value up to n is computed once.
        Space: O(n) — memo stores up to n intermediate results.
    """
    # Initialize memoization dictionary with the base cases if not provided
    if memo is None:
        memo = {0: 0, 1: 1, 2: 1}

    # If value already computed, return it immediately
    if n in memo:
        return memo[n]

    # Otherwise compute recursively and cache the result
    memo[n] = (
        tribonacci(n - 1, memo)
        + tribonacci(n - 2, memo)
        + tribonacci(n - 3, memo)
    )
    return memo[n]


def main():
    # Example usage: print the 21st Tribonacci number
    print(tribonacci(21))


if __name__ == "__main__":
    main()
