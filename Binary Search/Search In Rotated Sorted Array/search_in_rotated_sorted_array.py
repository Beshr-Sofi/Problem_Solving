def rotatedBinarySearch2(nums, target):
    """
    Search for a target value in a rotated sorted array that may contain duplicates.
    
    This is an extension of the standard rotated binary search problem (LeetCode 81)
    that handles arrays with duplicate elements. The presence of duplicates makes
    the search more complex because we can't always determine which half is sorted
    when nums[l] == nums[mid] == nums[r].
    
    Key challenges with duplicates:
    1. When nums[l] == nums[mid] == nums[r], we can't tell which half is sorted
    2. Standard binary search may fail because the pivot point is ambiguous
    
    Strategy: When we encounter duplicate values at boundaries that equal nums[mid],
    we shrink the search space by moving the boundaries inward until we can
    determine which half is sorted.
    
    Example: [6,6,6,7,0,1,2,6,6] - search for 4 (should return False)
    
    Time Complexity: O(n) in worst case when many duplicates (degenerates to linear)
    Space Complexity: O(1) - uses constant extra space
    
    Args:
        nums (list): A rotated sorted array that may contain duplicates
        target (int): The value to search for in the array
        
    Returns:
        bool: True if target exists in the array, False otherwise
    """
    # Initialize binary search pointers
    l, r = 0, len(nums) - 1
    
    # Standard binary search loop
    while l <= r:
        # Calculate middle index
        mid = (l + r) // 2
        
        # Handle duplicates: shrink boundaries when they equal nums[mid]
        # This is necessary because when nums[l] == nums[mid] == nums[r],
        # we cannot determine which half is sorted
        while l < len(nums) and nums[l] == nums[mid]:
            l += 1  # Move left pointer right to skip duplicates
        while r >= 0 and nums[r] == nums[mid]:
            r -= 1  # Move right pointer left to skip duplicates
        
        # Recalculate mid after adjusting boundaries
        # This is crucial because l and r have changed
        mid = (l + r) // 2
        
        # Check if we found the target at the recalculated mid
        if nums[mid] == target:
            return True
        
        # Determine which half is sorted and where target might be
        
        # Case: Middle element is greater than target
        # We need to decide which half to search
        if nums[mid] > target:
            # If target is less than leftmost element AND left half is sorted
            # This means target could be in the right half (which might be rotated)
            if target < nums[l]:
                l = mid + 1  # Search in right half
            else:
                r = mid - 1  # Search in left half
        
        # Case: Middle element is less than target  
        else:
            # If target is greater than rightmost element AND right half is sorted
            # This means target could be in the left half (which might be rotated)
            if target > nums[r]:
                r = mid - 1  # Search in left half
            else:
                l = mid + 1  # Search in right half
    
    # Target not found
    return False

def main():
    # Test case: rotated sorted array with duplicates
    nums = [6, 6, 6, 7, 0, 1, 2, 6, 6]
    target = 4
    
    # Search for target and print result
    print(rotatedBinarySearch2(nums, target))
