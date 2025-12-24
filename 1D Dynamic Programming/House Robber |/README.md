# House Robber — Problem Description and Solution

## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed, represented by a non-negative integer in a list. You cannot rob two
adjacent houses (they have security systems connected). Find the maximum amount of money you
can rob without triggering the alarms.

**Example**

- Input: `[5, 1, 2, 10, 6, 2, 7, 9, 3, 1]`
- Output: `34` (one optimal strategy is to rob houses with amounts 5 + 2 + 6 + 7 + 9 + 5 etc.)

## Approach

This repository contains a top-down dynamic programming (recursive) solution with memoization:

- We define a recursive function that computes the best result starting at a given index.
- For each house at index `i`, there are two choices: rob it (and skip `i+1`) or skip it (and consider `i+1`).
- We use a dictionary `memo` to store results for already computed indices to avoid repeated work.

This approach yields linear time complexity because each index is computed at most once.

## Complexity

- Time: O(n) — each index is solved once and stored in the memo dictionary.
- Space: O(n) — recursion depth and memo dictionary both use up to O(n) space.

## Notes

- The implementation in `problem solving.py` uses a `main` wrapper that initializes the memo dictionary
  and a `rob_tmp` helper that carries out the recursion with memoization.
- The code includes an example invocation in the `__main__` block.

---

If you'd like, I can also add unit tests or convert the solution to an iterative (bottom-up) DP version. Just tell me which you prefer.
