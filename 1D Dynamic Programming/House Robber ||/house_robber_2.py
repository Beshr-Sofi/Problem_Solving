def rob_from_start(nums, start_index):
    """
    Helper function to solve the house robbery problem from a given start index.
    Uses memoization to avoid redundant calculations.
    """
    memo = {}
    
    def rob_helper(index):
        # If we've already computed this index, return the cached result
        if index in memo:
            return memo[index]
        
        # Base case: if index is out of bounds, return 0
        if index >= len(nums):
            return 0
        
        # Two options:
        # 1. Rob current house and skip the next one
        take = nums[index] + rob_helper(index + 2)
        # 2. Skip current house and consider the next one
        not_take = rob_helper(index + 1)
        
        # Store the maximum of the two options in memo
        memo[index] = max(take, not_take)
        return memo[index]
    
    return rob_helper(start_index)

def rob_circular_houses(nums):
    """
    Solves the house robbery problem with circular arrangement.
    Since the first and last houses are adjacent, we need to consider two cases:
    1. Rob houses from index 0 to n-2 (exclude last house)
    2. Rob houses from index 1 to n-1 (exclude first house)
    Take the maximum of these two cases.
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # Case 1: Rob houses excluding the last house
    rob_exclude_last = rob_from_start(nums, 0)
    
    # Case 2: Rob houses excluding the first house
    rob_exclude_first = rob_from_start(nums, 1)
    
    return max(rob_exclude_last, rob_exclude_first)

def main():
    nums = [5, 1, 2, 6, 12, 7, 9, 3, 4, 10]
    result = rob_circular_houses(nums)
    print(result)

if __name__ == "__main__":
    main()
