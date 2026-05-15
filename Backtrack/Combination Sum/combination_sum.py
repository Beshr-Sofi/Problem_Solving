"""
Problem Description:
The "Combination Sum" problem asks us to find all unique combinations of a given array of distinct integers (`nums`) that sum up to a given `target` integer.
You may use the same number from `nums` an unlimited number of times.
Two combinations are considered unique if the frequency of at least one of the chosen numbers is different.

Explanation of the Code:
The code uses a Depth-First Search (DFS) / Backtracking approach to explore all possible combinations.
- `res`: A list to store the final valid combinations.
- `curr`: A list to keep track of the current combination being built.
- `dfs(index, sumTotal)`: A recursive function where:
    - `index` is the current candidate number we are considering from `nums`.
    - `sumTotal` is the sum of the elements currently in `curr`.
    - Base Cases:
        - If `sumTotal == target`, we found a valid combination, so we append a copy of `curr` to `res`.
        - If `sumTotal > target` (we exceeded the target) or `index == len(nums)` (we ran out of candidates), we stop exploring this path and backtrack.
    - Recursive Steps:
        - Option 1 (Include the current number): We append `nums[index]` to `curr` and recursively call `dfs` with the same `index` (since we can reuse the same number) and an updated `sumTotal`.
        - Option 2 (Exclude the current number): We remove the last added number from `curr` (backtracking) and recursively call `dfs` with `index + 1` to move on to the next candidate without changing `sumTotal`.
- `sys.setrecursionlimit(2000)`: Increases the maximum recursion depth, which might be necessary if the target is large and the smallest number in `nums` is very small (leading to a deep recursion tree).

Time Complexity:
- O(2^(T/M)) where `T` is the target value and `M` is the minimum value in `nums`.
- In the worst case, the recursion tree has a maximum depth of `T/M` (if we keep adding the smallest element). At each step, we have 2 choices (include the current element or skip it). This leads to an exponential time complexity in the worst-case scenario.

Space Complexity:
- O(T/M) auxiliary space. This is the maximum depth of the recursion stack, and also the maximum size of the `curr` array. The space required to store the results is not included in the auxiliary space complexity.
"""

import sys

def combinationSum(nums, target) -> list[list[int]]:
    res = []
    curr = []
    def dfs(index, sumTotal):
        if sumTotal == target:
            res.append(curr.copy())
            return
        if index == len(nums) or sumTotal > target:
            return
        
        curr.append(nums[index])
        dfs(index, sumTotal + nums[index])

        curr.pop()
        dfs(index+1, sumTotal)
    
    sys.setrecursionlimit(2000)
    dfs(0,0)
    return res


def main():
    nums = [2, 3, 6, 7]
    target = 7
    print(combinationSum(nums, target))


if __name__ == "__main__":
    main()


    
