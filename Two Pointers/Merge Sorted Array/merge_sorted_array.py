def merge(nums1, m, nums2, n):
    """
    Merge two sorted arrays into the first array (in-place) - Forward approach.
    
    This implementation merges nums2 into nums1 by iterating from the beginning.
    It shifts elements in nums1 to the right when inserting elements from nums2.
    
    This is LeetCode problem 88: Merge Sorted Array.
    
    Example: nums1 = [10,20,20,40,0,0] (m=4), nums2 = [1,2] (n=2)
    Result: [1,2,10,20,20,40]
    
    Time Complexity: O(m * n) in worst case due to shifting
    Space Complexity: O(1) - in-place modification
    
    Args:
        nums1 (list): First sorted array with extra space at the end
        m (int): Number of valid elements in nums1
        nums2 (list): Second sorted array
        n (int): Number of elements in nums2
    """
    # Initialize pointers for both arrays
    l1, l2 = 0, 0
    
    # Process elements while we have elements left in nums1's valid portion
    while l1 < m:
        # If nums2 still has elements AND current nums2 element is smaller
        # than the current nums1 element (at position l1 + l2 accounting for insertions)
        if l2 < n and nums1[l1 + l2] > nums2[l2]:
            # Shift elements in nums1 to the right to make space
            # Start from the end of the current valid region (m + l2 - 1)
            # and move backwards to the insertion point (l1 + l2)
            for i in range(m + l2, l1 + l2, -1):
                nums1[i] = nums1[i - 1]
            
            # Insert the nums2 element at the correct position
            nums1[l2 + l1] = nums2[l2]
            
            # Move to next element in nums2
            l2 += 1
        else:
            # Current nums1 element is smaller or equal, move to next nums1 element
            l1 += 1
    
    # If there are remaining elements in nums2, append them to the end
    while l2 < n:
        nums1[l2 + l1] = nums2[l2]
        l2 += 1

def merge2(nums1, m, nums2, n):
    """
    Merge two sorted arrays into the first array (in-place) - Backward approach.
    
    This optimized implementation starts from the end of both arrays and fills
    nums1 from the back, avoiding the need for shifting elements. This is the
    standard solution for LeetCode 88.
    
    Example: nums1 = [10,20,20,40,0,0] (m=4), nums2 = [1,2] (n=2)
    Process:
    - Compare 40 vs 2: put 40 at end
    - Compare 20 vs 2: put 20 at next position
    - Compare 20 vs 2: put 20 at next position
    - Compare 10 vs 2: put 2 at next position
    - Compare 10 vs 1: put 1 at next position
    
    Time Complexity: O(m + n) - each element processed once
    Space Complexity: O(1) - in-place modification
    
    Args:
        nums1 (list): First sorted array with extra space at the end
        m (int): Number of valid elements in nums1
        nums2 (list): Second sorted array
        n (int): Number of elements in nums2
    """
    # Initialize pointers to the last valid elements in each array
    l1, l2 = m - 1, n - 1
    
    # Fill nums1 from the last position backwards
    for i in range(m + n - 1, -1, -1):
        # If we've exhausted nums2, we're done (remaining nums1 already in place)
        if l2 < 0:
            break
        
        # If nums1 still has elements AND its current last element is larger
        if l1 >= 0 and nums1[l1] > nums2[l2]:
            nums1[i] = nums1[l1]  # Place nums1 element at current position
            l1 -= 1                # Move nums1 pointer left
        else:
            nums1[i] = nums2[l2]   # Place nums2 element at current position
            l2 -= 1                # Move nums2 pointer left

def main():
    """
    Main function to demonstrate both merge approaches.
    
    Tests both merge functions with:
    nums1 = [10,20,20,40,0,0] (valid elements: 10,20,20,40)
    nums2 = [1,2]
    
    Both should produce [1,2,10,20,20,40]
    
    Note: The first approach (merge) is less efficient due to shifting,
    while the second (merge2) is optimized with O(m+n) time.
    """
    # Test first approach (forward with shifting)
    nums1 = [10, 20, 20, 40, 0, 0]
    nums2 = [1, 2]
    merge(nums1, 4, nums2, 2)
    print(nums1)  # Expected: [1, 2, 10, 20, 20, 40]

    # Test second approach (backward without shifting)
    nums1 = [10, 20, 20, 40, 0, 0]
    nums2 = [1, 2]
    merge2(nums1, 4, nums2, 2)
    print(nums1)  # Expected: [1, 2, 10, 20, 20, 40]

if __name__ == "__main__":
    main()
