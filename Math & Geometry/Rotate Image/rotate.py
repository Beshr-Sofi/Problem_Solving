def rotate(matrix):
    """
    Rotates an NxN 2D matrix 90 degrees clockwise in-place.
    
    Approach 1: Transpose and Reverse
    ---------------------------------
    This is an elegant mathematical approach to rotating a matrix.
    A 90-degree clockwise rotation can be broken down into two simpler operations:
    1. Transpose the matrix: Flip the matrix over its main diagonal. 
       This turns rows into columns (matrix[i][j] swaps with matrix[j][i]).
    2. Reverse each row: Flip the matrix horizontally.
       (matrix[i][j] swaps with matrix[i][n-j-1]).
       
    Time Complexity: O(N^2) - We visit every element twice (once for transpose, 
                     once for reverse).
    Space Complexity: O(1) - All operations are done in-place.
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap across the main diagonal)
    for i in range(n):
        # Start j from i to avoid double-swapping back to original
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
            
    # Step 2: Reverse every row horizontally
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

def rotate2(matrix):
    """
    Rotates an NxN 2D matrix 90 degrees clockwise in-place.
    
    Approach 2: Layer-by-Layer Rotation (Four-Way Swap)
    ---------------------------------------------------
    This approach rotates the matrix layer by layer, starting from the outer 
    edge and moving inwards. For each layer, it moves elements in groups of 
    four (Top, Right, Bottom, Left).
    
    Algorithm:
    1. Define boundaries: `l` (left) and `r` (right). `top` is `l`, `bottom` is `r`.
    2. Iterate through the elements in the current layer (from 0 to r-l).
    3. For each element `i` in the current layer:
       - Save the `top` element in a temporary variable.
       - Move the `left` element into the `top` spot.
       - Move the `bottom` element into the `left` spot.
       - Move the `right` element into the `bottom` spot.
       - Move the saved `top` element into the `right` spot.
    4. Move the boundaries inwards (`l += 1`, `r -= 1`) and repeat for inner layers.
    
    Time Complexity: O(N^2) - We visit each element exactly once.
    Space Complexity: O(1) - All operations are done in-place using a temp variable.
    """
    l, r = 0, len(matrix) - 1
    
    while l < r:
        # Number of elements to swap in the current layer
        for i in range(r - l):
            top, bottom = l, r
            
            # Save the top-left element
            temp = matrix[top][l + i]

            # Move bottom-left element into top-left position
            matrix[top][l + i] = matrix[bottom - i][l]
            
            # Move bottom-right element into bottom-left position
            matrix[bottom - i][l] = matrix[bottom][r - i]
            
            # Move top-right element into bottom-right position
            matrix[bottom][r - i] = matrix[top + i][r]
            
            # Move the saved top-left element into the top-right position
            matrix[top + i][r] = temp
            
        # Move to the next inner layer
        l += 1
        r -= 1

def main():
    """
    Example demonstrating both matrix rotation approaches.
    """
    # Original Matrix:
    # [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    print("Matrix 1 after rotate() (Transpose + Reverse):")
    rotate(matrix1)
    print(matrix1) # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    
    # We create a fresh matrix because matrix1 is already rotated!
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    print("\nMatrix 2 after rotate2() (Layer-by-Layer):")
    rotate2(matrix2)
    print(matrix2) # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

if __name__ == "__main__":
    main()
