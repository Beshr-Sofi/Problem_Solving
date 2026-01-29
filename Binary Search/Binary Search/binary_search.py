def search(nums, target):
    """Performs binary search to find a target value in a sorted list.
    
    Uses the divide-and-conquer approach to efficiently find the target by repeatedly
    dividing the search space in half. Time complexity: O(log n)
    
    Args:
        nums (list): A sorted list of integers to search in
        target (int): The value to search for
        
    Returns:
        int: The index of the target if found, -1 otherwise
        
    Example:
        >>> search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
        4
    """
    l , r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def main():
    """Main function that demonstrates the binary search algorithm.
    
    Creates a sample sorted list and searches for a target value using the
    binary search function, then prints the result.
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = search(nums, target)
    print(f"Target {target} found at index: {result}")

if __name__ == "__main__":
    main()
