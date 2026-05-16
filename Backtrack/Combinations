def combinations(n , k):
    """
    Generates all possible combinations of k numbers chosen from the range [1, n].
    
    Approach: Depth-First Search (DFS) / Backtracking
    -------------------------------------------------
    To find every unique combination of size k, we use a recursive function that 
    iterates through the available numbers. At each step, we pick a number, add it 
    to our current combination, and recursively find the remaining numbers needed. 
    Once we finish exploring that path, we remove the number (backtrack) and try 
    the next available number.
    
    Algorithm:
    1. We define a recursive `helper(index, curr)` function:
       - `index`: The next number we can potentially add to our combination.
       - `curr`: The current combination of numbers we are building.
    2. Base Case: 
       - If the length of `curr` is equal to `k`, we have successfully built a 
         complete combination of the required size. We append a copy of `curr` 
         to our `res` list and return.
    3. The Recursion (The "Loop and Backtrack" branches):
       - We loop through all numbers `i` from `index` up to `n`.
       - Branch 1 (Include): We add the number `i` to `curr`, and then recursively 
         call `helper(i + 1, curr)` to continue building the combination with the 
         remaining available numbers (greater than `i`).
       - Branch 2 (Exclude / Backtrack): After exploring all combinations that 
         include `i`, we pop `i` from `curr`. This perfectly restores `curr` to 
         its previous state, allowing the next iteration of the loop to try a 
         different number in that position.
         
    Because we only iterate forward (`i + 1`) and strictly build combinations up 
    to size `k`, we avoid generating permutations (different orders of the same 
    numbers) and guarantee that each unique combination is generated exactly once.
    
    Time Complexity: O(k * C(n, k)) - Where C(n, k) is the number of combinations 
                     (n choose k). We generate C(n, k) valid combinations, and 
                     copying each one takes O(k) time.
    Space Complexity: O(k) - For the recursive call stack depth and the `curr` 
                      array, which both grow up to a maximum size of k.
    """
    res = []
    def helper(index, curr):
        if len(curr) == k:
            res.append(curr.copy())
            return
        for i in range(index, n+1):
            curr.append(i)
            helper(i + 1, curr)
            curr.pop()

    helper(1, [])
    return res

def main():
    print(combinations(4, 2))

if __name__ == "__main__":
    main()
