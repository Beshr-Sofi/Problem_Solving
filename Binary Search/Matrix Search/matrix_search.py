def SearchMatrix(matrix, target):
    """
    Search for a target value in a 2D matrix using binary search.
    
    This function assumes the matrix is:
    - Each row is sorted in ascending order
    - The first element of each row is greater than the last element of the previous row
    - This allows treating the 2D matrix as a sorted 1D array
    
    Algorithm:
    1. Binary search on the first column to find the correct row
    2. Binary search on the found row to locate the target
    
    Time Complexity: O(log m + log n) where m is number of rows, n is number of columns
    Space Complexity: O(1)
    
    Args:
        matrix: 2D list of integers (m x n matrix)
        target: The value to search for
    
    Returns:
        True if target is found, False otherwise
    """
    
    # Binary search on first column to find the potential row containing target
    l, r = 0, len(matrix) - 1
    while l <= r:
        mid = (l + r) // 2
        # If the first element of mid row <= target, search lower rows
        if matrix[mid][0] <= target:
            l = mid + 1
        else:
            # Otherwise search upper rows
            r = mid - 1
    
    # row is set to the last row where first element <= target
    row = l - 1
    
    # Check if row is valid
    if row < 0:
        return False
    
    # Binary search within the found row
    l, r = 0, len(matrix[0]) - 1
    while l <= r:
        mid = (l + r) // 2
        # If we find the target, return True
        if matrix[row][mid] == target:
            return True
        # If current element is less than target, search right half
        elif matrix[row][mid] < target:
            l = mid + 1
        # Otherwise search left half
        else:
            r = mid - 1
    
    # Target not found
    return False

def main():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 34
    result = SearchMatrix(matrix, target)
    print(f"Target {target} found in matrix: {result}")

if __name__ == "__main__":
    main()
