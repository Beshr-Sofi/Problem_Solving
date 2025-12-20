# Two Sum

**Problem:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input has exactly one solution, and you may not use the same element twice.

## Example

```
Input: nums = [2,7,11,15], target = 9
Output: [0, 1]
```

## Constraints

- 2 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9
- Exactly one valid answer.

## Approach ✅

- Use a hash map (dictionary) to store values we've seen and their indices.
- For each number `n`, check if `target - n` exists in the map; if so, we found the pair.
- This yields time O(n) and space O(n).

## Complexity 🔧

- **Time:** O(n)
- **Space:** O(n)
