# Tribonacci

**Problem:** Compute the n-th Tribonacci number. The Tribonacci sequence is defined as:

- T0 = 0
- T1 = 1
- T2 = 1
- For n >= 3: Tn = Tn-1 + Tn-2 + Tn-3

## Example

```
Input: n = 4
Output: 4
Explanation: Sequence: [0, 1, 1, 2, 4]
```

## Constraints

- 0 <= n <= 37 (values can grow quickly; typical upper bound used in common problems)
- Integer arithmetic only

## Approach ✅

- Use memoization (top-down dynamic programming) to cache computed terms.
- Recursively compute Tn as Tn-1 + Tn-2 + Tn-3 and memoize results to avoid recomputation.

## Complexity 🔧

- **Time:** O(n) — each value up to `n` is computed at most once.
- **Space:** O(n) — memoization dictionary stores intermediate results and recursion depth.
