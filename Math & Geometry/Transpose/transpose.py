def transpose(matrix):
    """
    Computes the transpose of a 2D matrix.
    
    The transpose of a matrix is an operator which flips a matrix over its main diagonal. 
    This operation switches the row and column indices of the matrix. That is, if a value 
    is at row `i` and column `j` in the original matrix, it will be at row `j` and column `i` 
    in the transposed matrix.
    
    Dimensions:
    If the original matrix has dimensions n x m (n rows, m columns), 
    the transposed matrix will have dimensions m x n (m rows, n columns).
    
    Algorithm:
    1. Determine the dimensions `n` and `m` of the original matrix.
    2. Initialize an empty result matrix `res` with dimensions m x n. 
       We use a list comprehension `[[0] * n for _ in range(m)]` to ensure that 
       we create `m` independent inner lists. (Using `[[0] * n] * m` would create 
       multiple references to the exact same list in memory, leading to bugs).
    3. Loop through every element in the original matrix using nested loops.
    4. Place the value from `matrix[i][j]` into `res[j][i]`.
    
    Time Complexity: O(n * m) - We visit every element in the matrix exactly once.
    Space Complexity: O(n * m) - We create a new matrix of the same total size to store 
                      the result.
    """
    n, m = len(matrix), len(matrix[0])
    
    # Initialize the result matrix with flipped dimensions (m rows, n columns)
    # List comprehension creates independent lists for each row
    res = [[0] * n for _ in range(m)]
    
    # Iterate through the original matrix
    for i in range(n):
        for j in range(m):
            # Swap the row and column indices for the new matrix
            res[j][i] = matrix[i][j]
            
    return res

def main():
    """
    Example demonstrating matrix transposition.
    
    Original Matrix (2x3):
    [
      [1, 2, 3],
      [4, 5, 6]
    ]
    
    Transposed Matrix (3x2):
    [
      [1, 4],
      [2, 5],
      [3, 6]
    ]
    """
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    print("Original matrix:")
    for row in matrix:
        print(row)
        
    print("\nTransposed matrix:")
    transposed = transpose(matrix)
    for row in transposed:
        print(row)

if __name__ == "__main__":
    main()
