def threeSum(nums):
    """
    Find all unique triplets in the array that sum to zero.
    
    This is the classic LeetCode problem 15: 3Sum. The function finds all unique
    triplets [nums[i], nums[j], nums[k]] such that i != j != k and
    nums[i] + nums[j] + nums[k] == 0.
    
    Algorithm strategy:
    1. Sort the array to enable two-pointer technique and duplicate handling
    2. Fix one element (a) and use two pointers to find pairs that sum to -a
    3. Skip duplicates to ensure unique triplets
    4. Move pointers appropriately based on current sum
    
    Time Complexity: O(n²) where n is the length of the array
    Space Complexity: O(1) excluding the space for output
    
    Args:
        nums (list): Array of integers (may contain duplicates)
        
    Returns:
        list: List of lists, each containing a unique triplet that sums to zero
    """
    res = []  # Result list to store all unique triplets
    
    # Step 1: Sort the array
    # This enables the two-pointer technique and makes duplicate handling easier
    nums.sort()
    
    # Step 2: Iterate through the array, fixing one element at a time
    for i, a in enumerate(nums):
        # Skip duplicate elements to avoid duplicate triplets
        # If current element equals previous element, skip it
        if i > 0 and a == nums[i - 1]:
            continue
        
        # Step 3: Use two pointers to find pairs that sum to -a
        # Left pointer starts right after the fixed element
        # Right pointer starts at the end of the array
        l, r = i + 1, len(nums) - 1
        
        # Continue until pointers meet
        while l < r:
            # Calculate current sum
            sum = a + nums[l] + nums[r]
            
            # Case 1: Sum is too large - need smaller numbers
            if sum > 0:
                r -= 1  # Move right pointer left to decrease sum
            
            # Case 2: Sum is too small - need larger numbers
            elif sum < 0:
                l += 1  # Move left pointer right to increase sum
            
            # Case 3: Found a triplet that sums to zero
            else:
                # Add the triplet to result
                res.append([a, nums[l], nums[r]])
                
                # Move left pointer to find next potential pair
                l += 1
                
                # Skip duplicates on the left side
                # While the next element is same as previous, keep moving
                while l < r and nums[l - 1] == nums[l]:
                    l += 1
                
                # Note: We don't need to explicitly skip duplicates on right
                # because they'll be handled naturally when sum conditions change
    
    return res

def main():
    """
    Main function to demonstrate finding triplets that sum to zero.
    
    Tests the threeSum function with a diverse array containing:
    - Negative numbers: -1, -2, -4, -3
    - Zero: 0
    - Positive numbers: 1, 2, 3, 4
    - Duplicates: -1 appears twice, 0 appears twice
    
    Expected output should include all unique triplets that sum to zero,
    such as [-4,0,4], [-4,1,3], [-3,-1,4], etc.
    """
    # Input array with various numbers including duplicates
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    
    # Find all unique triplets that sum to zero
    result = threeSum(nums)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()
