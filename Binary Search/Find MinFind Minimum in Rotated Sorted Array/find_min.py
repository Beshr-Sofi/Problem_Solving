def findMin(nums):
    """
    Find the minimum element in a rotated sorted array.
    
    This function uses a modified binary search approach to find the minimum 
    element in an array that was originally sorted in ascending order and then 
    rotated at some pivot point. The array has no duplicates.
    
    Key insight: In a rotated sorted array, the minimum element is at the 
    rotation point (pivot). The array consists of two sorted portions.
    
    Example: [3,4,5,1,2] -> original sorted [1,2,3,4,5] rotated at index 3
    
    Time Complexity: O(log n) - binary search approach
    Space Complexity: O(1) - uses constant extra space
    
    Args:
        nums (list): A rotated sorted array of unique integers
        
    Returns:
        int: The minimum element in the rotated sorted array
    """
    l, r = 0, len(nums) - 1  # Left and right pointers for binary search
    res = 1001  # Initialize result with a large value (assuming nums[i] ≤ 1000)
    
    # Binary search while search space is valid
    while l <= r:
        mid = (l + r) // 2  # Calculate middle index
        
        # Case 1: Current segment is rotated (nums[l] > nums[r])
        # This means the rotation pivot is within this segment
        if nums[l] > nums[r]:
            # If middle element is less than leftmost element,
            # the pivot (minimum) is in the left half (including mid)
            if nums[mid] < nums[l]:
                r = mid - 1  # Search left half
                res = nums[mid]  # Update result (nums[mid] could be minimum)
            else:
                # Otherwise, pivot is in the right half
                l = mid + 1  # Search right half
        
        # Case 2: Current segment is properly sorted (nums[l] <= nums[r])
        # This means we've narrowed down to a sorted segment where
        # the leftmost element is the minimum in this segment
        else:
            # Return the minimum between current best result and nums[l]
            # since nums[l] is the smallest in this sorted segment
            return min(nums[l], res)
    
    # Return the best result found (only reached if loop terminates without return)
    return res

def main():
    """
    Main function to demonstrate finding minimum in rotated sorted array.
    
    Tests the findMin function with a sample rotated array:
    Original: [1,2,3,4,5]
    Rotated at index 3: [3,4,5,1,2]
    
    The minimum should be 1, which is at the rotation pivot.
    """
    # Test case: rotated sorted array [3,4,5,1,2]
    nums = [3, 4, 5, 1, 2]
    
    print("Finding minimum in rotated sorted array")
    print("=" * 50)
    print(f"Input array: {nums}")
    print(f"Array is rotated: {nums[0]} > {nums[-1]} = {nums[0] > nums[-1]}")
    
    # Find and display the minimum
    minimum = findMin(nums)
    print(f"\nMinimum element: {minimum}")
    
if __name__ == "__main__":
    main()
