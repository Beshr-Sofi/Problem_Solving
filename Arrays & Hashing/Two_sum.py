"""Two Sum problem: find indices of two numbers that add up to target.

This module implements a linear-time solution using a hash map (dictionary),
which stores previously seen numbers and their indices. For each number n,
we check if target - n has been seen before; if so, we return the pair
of indices.
"""

from typing import List, Optional

def twosum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Return indices of the two numbers such that they add up to target.

    Args:
        nums: List of integers.
        target: Integer target sum.

    Returns:
        A list with two indices [i, j] (i < j) if such a pair exists, otherwise None.

    Example:
        >>> twosum([2,7,11,15], 9)
        [0, 1]

    Complexity:
        Time: O(n) — we make a single pass over `nums`.
        Space: O(n) — dictionary storing seen numbers and indices.
    """
    # Dictionary to map number -> its index in `nums`
    seen = {}
    for i, n in enumerate(nums):
        # Complement value needed to reach target
        complement = target - n
        # If complement was seen before, return indices [index_of_complement, current_index]
        if complement in seen:
            return [seen[complement], i]
        # Otherwise, record the index of the current number
        seen[n] = i
    # No solution found
    return None

def main():
    # Example usage
    print(twosum([2, 7, 11, 15], 9))

if __name__ == "__main__":
    main()
