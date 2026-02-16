def removeDuplicates(nums):
    """
    Remove duplicates in-place from a sorted array and return the number of unique elements.
    
    This function implements the algorithm for LeetCode problem 26: Remove Duplicates from Sorted Array.
    It uses a two-pointer technique to overwrite duplicate elements while preserving the relative order.
    
    Key insight: Since the array is sorted, duplicates are adjacent. We can use one pointer to track
    the position where the next unique element should be placed, and another pointer (the loop index)
    to scan through the array.
    
    Example: [1,1,2,3,3,4,5,5] -> [1,2,3,4,5, ...] with the first 5 elements being unique
    
    Time Complexity: O(n) where n is the length of the array
    Space Complexity: O(1) - modifies the array in-place
    
    Args:
        nums (list): A sorted list of integers (may contain duplicates)
        
    Returns:
        int: The number of unique elements in the array (k)
             The first k elements of nums will contain the unique elements in sorted order
    """
    # Initialize position pointer to track where to place the next unique element
    # This pointer always points to the last placed unique element
    position = 0
    
    # Iterate through the entire array
    for i in range(len(nums)):
        # If current element is different from the last placed unique element
        # This means we've found a new unique value
        if nums[i] != nums[position]:
            # Move position pointer to the next slot
            position += 1
            # Place the new unique element at this position
            nums[position] = nums[i]
    
    # Return the count of unique elements
    # Since position is zero-indexed, we add 1 to get the count
    return position + 1

def main():
    """
    Main function to demonstrate removing duplicates from a sorted array.
    
    Tests the removeDuplicates function with:
    nums = [1,1,2,3,3,4,5,5]
    
    Expected output:
    - Number of unique elements: 5
    - Modified array: [1,2,3,4,5]
    """
    # Input array (sorted with duplicates)
    nums = [1, 1, 2, 3, 3, 4, 5, 5]
    
    # Remove duplicates in-place and get count of unique elements
    k = removeDuplicates(nums)
    
    # Print results
    print(f"Number of unique elements: {k}")
    print(f"Modified array: {nums[:k]}")

if __name__ == "__main__":
    main()
