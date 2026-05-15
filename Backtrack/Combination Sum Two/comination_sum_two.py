import sys

def combinationSumTwo(candidates,target):
    """
    Finds all unique combinations in an array that sum to a target value, 
    using each element at most once.
    
    Approach: Depth-First Search (DFS) / Backtracking with Sorting
    --------------------------------------------------------------
    To find unique combinations, we sort the array first. Sorting helps us easily 
    skip duplicates to avoid building identical combinations. We then use a recursive 
    function to make a simple choice at each number: "Do I include this number 
    in my combination, or do I leave it out?"
    
    Algorithm:
    1. We sort the `candidates` array. This ensures that identical numbers are 
       adjacent, which is crucial for our "skip duplicates" logic.
    2. We define a recursive `dfs(index, sumTotal)` function:
       - `index`: The current index we are looking at in the `candidates` array.
       - `sumTotal`: The running sum of the combination we are currently building.
    3. Base Cases:
       - If `sumTotal == target`, we have found a valid combination! We append a 
         copy of our `curr` list to our `res` list.
       - If `sumTotal > target` or `index` equals the length of `candidates`, we've 
         exceeded the target or run out of numbers, so we stop exploring this path.
    4. The Recursion (The "Pick or Don't Pick" branches):
       - Branch 1 (Include): We add the current candidate to our `curr` combination 
         and recursively search forward: `dfs(index + 1, sumTotal + candidates[index])`.
       - Branch 2 (Exclude and Skip Duplicates): We remove the candidate we just added. 
         Then, to avoid creating duplicate combinations, we loop to skip over any 
         adjacent candidates that have the exact same value. Finally, we recursively 
         search without this candidate value: `dfs(index + 1, sumTotal)`.
         
    Because we skip duplicates in Branch 2, we guarantee that each unique combination 
    is only generated once, beautifully accumulating the results into the `res` array.
    
    Time Complexity: O(2^N) - In the worst case, every element could be part of the 
                     recursive branches, leading to 2^n possible subsets.
    Space Complexity: O(N) - For the recursive call stack depth and the `curr` 
                      array (at most N levels deep).
    """
    res = []
    curr = []
    candidates.sort()
    def dfs(index, sumTotal):
        if sumTotal == target:
            res.append(curr.copy())
            return
        if index == len(candidates) or sumTotal > target:
            return
        
        curr.append(candidates[index])
        dfs(index+1, sumTotal + candidates[index])

        curr.pop()
        while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
            index += 1
        dfs(index + 1, sumTotal)
        
    sys.setrecursionlimit(2000)
    dfs(0,0)
    return res

def main():
    candidates = [9,2,2,4,6,1,5]
    target = 8
    print(combinationSumTwo(candidates, target))


if __name__ == "__main__":
    main()
