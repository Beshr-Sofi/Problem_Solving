"""House Robber (top-down DP with memoization).

Given a list of non-negative integers representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
You cannot rob two adjacent houses.

This module implements a recursive (top-down) dynamic programming solution with memoization.
"""


def rob_tmp(nums, memo, index):
    """Return the maximum amount that can be robbed starting from house `index`.

    Args:
        nums (List[int]): list of non-negative integers (money at each house).
        memo (dict): memoization dictionary mapping index -> max amount from that index.
        index (int): current house index to consider.

    Returns:
        int: maximum money that can be robbed starting from `index`.
    """
    # Base case: if index is beyond the last house, nothing to rob
    if index >= len(nums):
        return 0

    # Return cached result if available
    if index in memo:
        return memo[index]

    # Choice 1: rob current house, then move to index + 2
    rob_current = nums[index] + rob_tmp(nums, memo, index + 2)

    # Choice 2: skip current house, consider index + 1
    skip_current = rob_tmp(nums, memo, index + 1)

    # Store the best of both choices in memo and return
    memo[index] = max(rob_current, skip_current)
    return memo[index]


def main(nums):
    """Wrapper function: initializes memoization and starts recursion.

    Note: memo is initialized per call to avoid carrying state between calls.
    """
    memo = {}
    return rob_tmp(nums, memo, 0)


if __name__ == "__main__":
    # Example usage
    print(main([5, 1, 2, 10, 6, 2, 7, 9, 3, 1]))
