def searchSortedRotatedArray(nums, target):
    """
    Search for a target value in a rotated sorted array using binary search.
    
    This function implements a modified binary search algorithm to find a target
    value in an array that was originally sorted in ascending order and then 
    rotated at some pivot point. The array contains distinct integers.
    
    Key insight: At any point in the binary search, at least one half of the 
    array (left or right of mid) will be properly sorted. We can determine
    which half is sorted and then check if the target lies within that sorted half.
    
    Example: [4,5,6,7,0,1,2] is [0,1,2,4,5,6,7] rotated at index 4
    
    Time Complexity: O(log n) - binary search approach
    Space Complexity: O(1) - uses constant extra space
    
    Args:
        nums (list): A rotated sorted array of distinct integers
        target (int): The value to search for in the array
        
    Returns:
        int: The index of target if found, -1 otherwise
    """
    # Initialize binary search pointers
    l, r = 0, len(nums) - 1
    
    # Binary search while the search space is valid
    while l <= r:
        # Calculate middle index
        mid = (l + r) // 2
        
        # If we found the target, return the index immediately
        if target == nums[mid]:
            return mid
        
        # Case 1: Left half [l, mid] is sorted (including when l == mid)
        if nums[l] <= nums[mid]:
            # The left half is properly sorted from nums[l] to nums[mid]
            
            # Target is NOT in the sorted left half if:
            # 1. target > nums[mid] (greater than largest in left half), OR
            # 2. target < nums[l] (smaller than smallest in left half)
            if target > nums[mid] or target < nums[l]:
                # Target must be in the right half (which may be rotated)
                l = mid + 1
            else:
                # Target is within the bounds of the sorted left half
                # Search in the left half
                r = mid - 1
        
        # Case 2: Right half [mid, r] is sorted (left half is rotated)
        else:
            # The right half is properly sorted from nums[mid] to nums[r]
            
            # Target is NOT in the sorted right half if:
            # 1. target < nums[mid] (smaller than smallest in right half), OR
            # 2. target > nums[r] (greater than largest in right half)
            if target < nums[mid] or target > nums[r]:
                # Target must be in the left half (which is rotated)
                r = mid - 1
            else:
                # Target is within the bounds of the sorted right half
                # Search in the right half
                l = mid + 1
    
    # Target not found in the array
    return -1

def main():
    """
    Main function to demonstrate searching in a rotated sorted array.
    
    Tests the searchSortedRotatedArray function with a sample rotated array:
    [4,5,6,7,0,1,2] is the rotated version of [0,1,2,4,5,6,7]
    
    The target 0 should be found at index 4.
    """
    # Test case: rotated sorted array
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    
    # Search for target and print result
    result = searchSortedRotatedArray(nums, target)
    print(result)
