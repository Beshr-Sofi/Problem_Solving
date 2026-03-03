def isValidSudoku(board):
    """
    Checks if a 9x9 Sudoku board is valid based on the rules:
    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each 3x3 sub-box must contain the digits 1-9 without repetition.
    
    Empty cells are denoted by ".".
    
    Time Complexity: O(1) - The board size is fixed at 9x9. We do a constant number of operations (3 passes of 81 iterations).
    Space Complexity: O(1) - The dictionary stores at most 9 elements at a time.
    """
    
    # 1. Check all rows for duplicates
    checker = {}
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            if board[i][j] in checker:
                return False
            checker[board[i][j]] = 1
        checker = {} # Clear dictionary for the next row
        
    # 2. Check all columns for duplicates
    for i in range(9):
        for j in range(9):
            if board[j][i] == ".": # Keep row index varying 'j' and column index static 'i'
                continue
            if board[j][i] in checker:
                return False
            checker[board[j][i]] = 1
        checker = {} # Clear dictionary for the next column
        
    # 3. Check all 3x3 sub-boxes for duplicates
    for i in range(3):
        for j in range(3):
            # Iterate over the 9 sub-boxes (3 rows of boxes, 3 columns of boxes)
            checker = {}
            row_start = i * 3
            column_start = j * 3
            
            # Iterate through the 9 elements in this specific 3x3 box
            for a in range(row_start, row_start+3):
                for b in range(column_start, column_start+3):
                    if board[a][b] == ".":
                        continue
                    if board[a][b] in checker:
                        return False
                    checker[board[a][b]] = 1
                    
    return True

def main():
    board = [["1","2",".",".","3",".",".",".","."],
             ["4",".",".","5",".",".",".",".","."],
             [".","9","8",".",".",".",".",".","3"],
             ["5",".",".",".","6",".",".",".","4"],
             [".",".",".","8",".","3",".",".","5"],
             ["7",".",".",".","2",".",".",".","6"],
             [".",".",".",".",".",".","2",".","."],
             [".",".",".","4","1","9",".",".","8"],
             [".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))

if __name__ == '__main__':
    main()
