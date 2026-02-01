"""
REMOVE ELEMENT FROM ARRAY

This module implements two algorithms to remove all occurrences of a value from 
a list in-place and return the count of remaining elements.

Two approaches:
1. RemoveElement: Bubble shift approach (less efficient)
2. RemoveElement2: Two-pointer approach (optimal)
"""

def RemoveElement(nums, val):
    """
    Remove all occurrences of val from nums using bubble shift approach.
    
    ALGORITHM EXPLANATION:
    - Iterates through the array backwards from the end to the beginning
    - When a matching element is found, shifts all elements after it one position left
    - This moves the target element to the end of the list
    - Finally returns the count of elements that are not equal to val
    
    WHY ITERATE BACKWARDS?
    - Prevents index shifting issues when modifying the array during iteration
    - Ensures we don't process already-shifted elements
    
    TIME COMPLEXITY: O(n²) - In worst case, we shift elements for each match
    SPACE COMPLEXITY: O(1) - Only modifies the list in-place
    
    Args:
        nums (list): The list to modify in-place
        val (int): The value to remove
        
    Returns:
        int: The count of remaining elements after removal
        
    Example:
        >>> nums = [3, 2, 2, 3]
        >>> RemoveElement(nums, 3)
        2
        >>> nums
        [2, 2, 3, 3]
    """
    # Iterate backwards through the list (from last index to 0)
    for i in range(len(nums) - 1, -1, -1):
        # Check if current element matches the value to remove
        if nums[i] == val:
            # Shift all elements after this index one position to the left
            for j in range(i + 1, len(nums)):
                # Swap adjacent elements to shift left
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    
    # Return count of non-val elements (total length minus occurrences of val)
    return len(nums) - nums.count(val)


def RemoveElement2(nums, val):
    """
    Remove all occurrences of val from nums using two-pointer approach (OPTIMAL).
    
    ALGORITHM EXPLANATION:
    - Uses a two-pointer technique: k (write pointer) and i (read pointer)
    - k tracks the position where the next non-val element should be placed
    - i scans through all elements
    - When a non-val element is found, copy it to position k and increment k
    - All non-val elements end up at the beginning of the list
    
    WHY TWO-POINTER?
    - Single pass through the array - very efficient
    - No unnecessary shifting or element movement
    - Optimal space usage with in-place modification
    
    TIME COMPLEXITY: O(n) - Single iteration through the array
    SPACE COMPLEXITY: O(1) - Only modifies the list in-place
    
    Args:
        nums (list): The list to modify in-place
        val (int): The value to remove
        
    Returns:
        int: The count of remaining elements after removal
        
    Example:
        >>> nums = [0, 1, 2, 2, 3, 0, 4, 2]
        >>> RemoveElement2(nums, 2)
        5
        >>> nums
        [0, 1, 3, 0, 4, 0, 4, 2]  # First 5 elements are non-2 values
    """
    # k is the write pointer - tracks where to place the next valid element
    k = 0
    
    # i is the read pointer - scans through all elements
    for i in range(len(nums)):
        # If current element is not the value to remove
        if nums[i] != val:
            # Place this element at position k
            nums[k] = nums[i]
            # Move write pointer forward
            k += 1
    
    # Return the count of elements that are not equal to val
    return k


# COMPARISON OF APPROACHES:
# 
# Approach 1 (RemoveElement):
# - Iterates backwards to avoid index issues
# - Uses nested loop for shifting elements
# - Less efficient for multiple matches
# 
# Approach 2 (RemoveElement2):
# - Single pass with two pointers
# - No shifting, just overwrites
# - Optimal for all cases


def main():
    """
    Main function to test both remove element algorithms.
    
    EXECUTION FLOW:
    1. Test RemoveElement with [3, 2, 2, 3], remove 3
       Expected: Returns 2 (count of non-3 elements)
       Array becomes: [2, 2, 3, 3]
    
    2. Test RemoveElement2 with [0, 1, 2, 2, 3, 0, 4, 2], remove 2
       Expected: Returns 5 (count of non-2 elements)
       First 5 elements are: [0, 1, 3, 0, 4]
    """
    # Test Case 1: RemoveElement with multiple occurrences
    nums = [3, 2, 2, 3]
    val = 3
    print(f"Test 1 - RemoveElement:")
    print(f"  Original: {[3, 2, 2, 3]}, Remove value: {val}")
    print(f"  Result count: {RemoveElement(nums, val)}")
    print(f"  Modified array: {nums}")
    
    # Test Case 2: RemoveElement2 with mixed values
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    print(f"\nTest 2 - RemoveElement2:")
    print(f"  Original: {[0, 1, 2, 2, 3, 0, 4, 2]}, Remove value: {val2}")
    print(f"  Result count: {RemoveElement2(nums2, val2)}")
    print(f"  Modified array (first {RemoveElement2([0, 1, 2, 2, 3, 0, 4, 2], 2)} elements are valid): {nums2}")


if __name__ == "__main__":
    main()
