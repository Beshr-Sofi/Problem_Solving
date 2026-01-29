def searchInsert(nums, target):
    """
    Finds the index where a target value should be inserted in a sorted array.
    
    Uses binary search to efficiently find the insertion position. If the target
    exists in the array, returns its index. Otherwise, returns the index where
    it should be inserted to maintain sorted order.
    
    Args:
        nums (list): A sorted list of integers
        target (int): The value to search for or insert
        
    Returns:
        int: The index where target is found or where it should be inserted
        
    Time Complexity: O(log n) - binary search
    Space Complexity: O(1) - constant space
    
    Examples:
        >>> searchInsert([1,3,5,6], 5)
        2
        >>> searchInsert([1,3,5,6], 2)
        1
        >>> searchInsert([1,3,5,6], 7)
        4
        >>> searchInsert([1,3,5,6], 0)
        0
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return mid + 1 if nums[mid] < target else mid

def main():
    """
    Main function that demonstrates the searchInsert function.
    
    Tests the searchInsert function with various test cases to show:
    - Finding an existing element in the array
    - Finding the correct insertion position for non-existing elements
    - Edge cases (target smaller than smallest element, larger than largest)
    """
    nums = [1, 3, 5, 6]
    
    # Test case 1: Target exists in array
    target = 5
    print(searchInsert(nums, target))  # Output: 2
    
    # Test case 2: Target should be inserted between elements
    target = 2
    print(searchInsert(nums, target))  # Output: 1
    
    # Test case 3: Target larger than all elements
    target = 7
    print(searchInsert(nums, target))  # Output: 4
    
    # Test case 4: Target smaller than all elements
    target = 0
    print(searchInsert(nums, target))  # Output: 0

if __name__ == "__main__":
    main()
