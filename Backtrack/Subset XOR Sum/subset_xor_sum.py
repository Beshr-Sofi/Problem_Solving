def subsetXORSum(nums):
    """
    Calculates the sum of all XOR totals for every possible subset of an array.
    
    Approach: Depth-First Search (DFS) / Backtracking
    -------------------------------------------------
    To find every possible subset, we can use a recursive function that makes a 
    simple choice at every single number in the array: "Do I include this number 
    in my subset, or do I leave it out?"
    
    Algorithm:
    1. We define a recursive `helper(i, current)` function:
       - `i`: The current index we are looking at in the `nums` array.
       - `current`: The running XOR total of the subset we are currently building.
    2. Base Case: If `i` equals the length of `nums`, we have finished making 
       choices for every number. The `current` variable now holds the final XOR 
       total for one complete subset! We add it to `totalSum`.
    3. The Recursion (The "Pick or Don't Pick" branches):
       - Branch 1 (Include): We mathematically include the current number in our 
         subset by XORing it: `helper(i + 1, current ^ nums[i])`.
       - Branch 2 (Exclude): We skip the current number, leaving `current` exactly 
         as it is: `helper(i + 1, current)`.
         
    Because every number splits the timeline into 2 branches, this explores 
    all 2^n possible subsets and beautifully accumulates their XOR totals into 
    the `nonlocal` variable `totalSum`.
    
    Time Complexity: O(2^N) - There are exactly 2^n possible subsets for an array 
                     of length N.
    Space Complexity: O(N) - For the recursive call stack depth (at most N levels deep).
    """
    totalSum = 0
    
    def helper(i, current):
        nonlocal totalSum
        
        # Base Case: We've reached the end of the array, add the subset's total
        if i == len(nums):
            totalSum += current
            return
            
        # Branch 1: Include the current element in the subset (apply XOR)
        helper(i + 1, current ^ nums[i])
        
        # Branch 2: Exclude the current element from the subset (do nothing)
        helper(i + 1, current)
        
    # Start the recursion at index 0, with a starting XOR total of 0
    helper(0, 0)
    
    return totalSum

def main():
    """
    Example demonstrating Sum of All Subset XOR Totals.
    
    Array: [1, 3]
    Subsets:
    1. [] -> XOR Total = 0
    2. [1] -> XOR Total = 1
    3. [3] -> XOR Total = 3
    4. [1, 3] -> XOR Total = 1 ^ 3 = 2
    Total Sum = 0 + 1 + 3 + 2 = 6
    """
    nums = [1, 3, 5, 6, 8, 10]
    print("Sum of all subset XOR totals:", subsetXORSum(nums))

if __name__ == "__main__":
    main()
