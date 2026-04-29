def setZeroes(matrix):
    """
    Given an m x n integer matrix, if an element is 0, sets its entire row 
    and column to 0 in-place.
    
    Approach: O(1) Space with First Row/Col as Flags
    ------------------------------------------------
    To achieve O(1) space complexity, we use the matrix's own first row and 
    first column to keep track of which rows and columns need to be zeroed.
    
    The Catch: 
    The very first element `matrix[0][0]` represents BOTH the first row and 
    the first column. If we set it to 0, we won't know if it was meant to zero 
    out the row, the column, or both. 
    To fix this, we use `matrix[0][0]` exclusively to track the first COLUMN, 
    and we create a single extra variable `corner` to track the first ROW.
    
    Algorithm:
    1. Mark Flags: Iterate through the matrix. If `matrix[i][j] == 0`:
       - Mark the column: `matrix[0][j] = 0`
       - Mark the row: If it's the first row (`i == 0`), set `corner = 0`.
         Otherwise, mark `matrix[i][0] = 0`.
    2. Apply Flags (Inner Matrix): Iterate through the matrix AGAIN, but skip 
       the first row and first column (start from index 1). If either the row 
       flag `matrix[i][0]` or the col flag `matrix[0][j]` is 0, set `matrix[i][j] = 0`.
    3. Apply Flags (First Column): If `matrix[0][0] == 0`, the entire first 
       column must be zeroed.
    4. Apply Flags (First Row): If `corner == 0`, the entire first row must 
       be zeroed.
       
    Time Complexity: O(m * n) - We iterate over the matrix roughly twice.
    Space Complexity: O(1) - Done entirely in-place with one extra variable.
    """
    n, m = len(matrix), len(matrix[0])
    
    # This variable tracks whether the FIRST ROW needs to be zeroed.
    corner = 1 
    
    # Step 1: Iterate through the matrix to mark the flags
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # If the zero is in the first row, update our special variable
                if i == 0:
                    corner = 0
                # Otherwise, use the first column to mark that this row has a zero
                else:
                    matrix[i][0] = 0
                    
                # Always use the first row to mark that this column has a zero
                matrix[0][j] = 0
    
    # Step 2: Use the marked flags to zero out the inner matrix
    # We MUST skip the first row and col so we don't overwrite our flags prematurely!
    for i in range(1, n):
        for j in range(1, m):
            # If either the row flag or the column flag is 0, set this cell to 0
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    
    # Step 3: Check if the first column itself needs to be zeroed
    if matrix[0][0] == 0:
        for i in range(n):
            matrix[i][0] = 0
    
    # Step 4: Check if the first row itself needs to be zeroed
    if corner == 0:
        for i in range(m):
            matrix[0][i] = 0

def main():
    """
    Example demonstrating Set Matrix Zeroes.
    
    Original Matrix:
    [1, 1, 1]
    [1, 0, 1]
    [1, 1, 1]
    
    The 0 at center (row 1, col 1) will cause row 1 and col 1 to become zeroes.
    
    Expected output:
    [[1, 0, 1], 
     [0, 0, 0], 
     [1, 0, 1]]
    """
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    setZeroes(matrix)
    print(matrix)

if __name__ == "__main__":
    main()
