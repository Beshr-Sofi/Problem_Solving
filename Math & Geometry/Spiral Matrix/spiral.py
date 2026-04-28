def spiralOrder(matrix):
    """
    Returns all elements of a 2D matrix in spiral order.
    
    Approach: Layer-by-Layer Boundary Traversal
    -------------------------------------------
    We define four boundaries (`top`, `bottom`, `left`, `right`) that represent 
    the unvisited portion of the matrix. We traverse the perimeter of this 
    unvisited portion in a clockwise direction, and then shrink the boundaries 
    inward to process the next "ring".
    
    Algorithm:
    1. Initialize boundaries: 
       - top = 0, bottom = m - 1
       - left = 0, right = n - 1
    2. While we have a valid block of at least 2x2 (`left < right` and `top < bottom`):
       - Traverse TOP row (left to right).
       - Traverse RIGHT col (top+1 to bottom).
       - Traverse BOTTOM row (right-1 down to left).
       - Traverse LEFT col (bottom-1 up to top+1).
       - Shrink all boundaries inward by 1.
    3. Handle the remaining center:
       - If the matrix has an odd number of rows/cols, the loop finishes leaving 
         either a single row or a single column unvisited.
       - If `bottom == top`, we traverse the remaining horizontal row.
       - Else if `left == right`, we traverse the remaining vertical column.
         
    Time Complexity: O(m * n) - Every element is visited exactly once.
    Space Complexity: O(1) - (Excluding the output array `res` which is O(m * n)).
    """
    res = []
    
    # Handle empty matrix edge case (though typical constraints guarantee non-empty)
    if not matrix:
        return res
        
    m, n = len(matrix), len(matrix[0])
    
    # Define the 4 boundaries
    left, right, bottom, top = 0, n - 1, m - 1, 0
    
    # Process full "rings" (requires at least 2 rows and 2 cols)
    while left < right and top < bottom:
        
        # 1. Traverse from left to right along the top boundary
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        
        # 2. Traverse from top+1 to bottom along the right boundary
        for i in range(top + 1, bottom + 1):
            res.append(matrix[i][right])

        # 3. Traverse from right-1 down to left along the bottom boundary
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom][i])

        # 4. Traverse from bottom-1 up to top+1 along the left boundary
        for i in range(bottom - 1, top, -1):
            res.append(matrix[i][left])
            
        # Shrink the boundaries inward for the next ring
        left, right, bottom, top = left + 1, right - 1, bottom - 1, top + 1

    # After the loop, there might be a single row or column left in the very center
    
    # If a single horizontal row remains
    if bottom == top:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
            
    # If a single vertical column remains
    elif left == right:
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])

    return res

def main():
    """
    Example demonstrating spiral order traversal.
    
    Matrix:
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
    
    Spiral path:
    1 -> 2 -> 3
              |
    4 -> 5    6
    ^         |
    7 <- 8 <- 9
    
    Expected output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
    matrix = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ]
    print(spiralOrder(matrix))

if __name__ == "__main__":
    main()
