def mergeSort(nums):
    """
    Sort an array using the Merge Sort algorithm (in-place modification).
    
    Merge Sort is a divide-and-conquer algorithm that:
    1. Divides the array into two halves
    2. Recursively sorts each half
    3. Merges the sorted halves back together
    
    This implementation modifies the original array in-place by using
    the merge function to combine sorted subarrays back into the original.
    
    Time Complexity: O(n log n) in all cases (best, average, worst)
    Space Complexity: O(n) for the temporary arrays created during division
    
    Args:
        nums (list): The array to be sorted (modified in-place)
    """
    # Base case: array with 0 or 1 element is already sorted
    if len(nums) < 2:
        return
    
    # Step 1: DIVIDE - Split the array into two halves
    mid = len(nums) // 2
    left = nums[:mid]    # Left half (creates a copy)
    right = nums[mid:]   # Right half (creates a copy)
    
    # Step 2: CONQUER - Recursively sort both halves
    mergeSort(left)
    mergeSort(right)
    
    # Step 3: COMBINE - Merge the sorted halves back into original array
    merge(left, right, nums)

def merge(left, right, nums):
    """
    Merge two sorted arrays (left and right) into the original array (nums).
    
    This function takes two sorted lists and combines them into a single
    sorted list by repeatedly comparing the smallest elements from each.
    
    Args:
        left (list): Sorted left half
        right (list): Sorted right half
        nums (list): Original array to store the merged result (modified in-place)
    """
    # Initialize pointers for left array (i), right array (j), and result array (k)
    i = j = k = 0
    
    # Step 1: Compare elements from both arrays and place the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # Left element is smaller or equal, place it in result
            nums[k] = left[i]
            i += 1
            k += 1
        else:
            # Right element is smaller, place it in result
            nums[k] = right[j]
            j += 1
            k += 1
    
    # Step 2: Copy any remaining elements from left array
    # This happens if right array was exhausted first
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    
    # Step 3: Copy any remaining elements from right array
    # This happens if left array was exhausted first
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

def main():
    """
    Main function to demonstrate merge sort.
    
    Tests the mergeSort function with an array containing duplicates:
    [10, 9, 1, 1, 1, 2, 3, 1]
    
    After sorting, the array should become: [1, 1, 1, 1, 2, 3, 9, 10]
    """
    # Input array with duplicates and unsorted elements
    nums = [10, 9, 1, 1, 1, 2, 3, 1]
    
    # Sort the array using merge sort
    mergeSort(nums)
    
    # Print the sorted array
    print(nums)

if __name__ == '__main__':
    main()
