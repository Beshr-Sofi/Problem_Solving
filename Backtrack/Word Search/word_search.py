"""
Problem:
    Given an m x n grid of characters 'board' and a string 'word', return True 
    if 'word' exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring. 
    The same letter cell may not be used more than once in a word.

Backtracking (DFS) Strategy:
    1. Scan the board: Start DFS from every cell (r, c) that matches word[0].
    2. Base Case (Success): If k == len(word), all characters have been matched.
    3. Pruning (Failure): Return False if:
       - The coordinates (r, c) are out of grid bounds.
       - The current cell board[r][c] does not match word[k].
       - The cell was already visited in the current path (marked with '#').
    4. Mark & Explore:
       - Temporarily mark board[r][c] = '#' to avoid revisiting in the same path.
       - Recursively explore all 4 adjacent directions: Down, Up, Right, Left.
    5. Backtrack (Unmark):
       - Restore board[r][c] to its original character before returning.
       - This allows other paths to reuse this cell.

Decision Tree Example (Searching for word = "BAT" on board):
    Board:
        [A, B, C, D]
        [S, A, A, T]
        [A, C, A, E]

    Start at (0, 1) ['B', k=0]:
                           (0, 1)='B' [k=0]
                           /              \
                     Down /                \ Left
                         v                  v
                   (1, 1)='A' [k=1]     (0, 0)='A' [k=1]
                   /   |    \    \           |     \
             Down / Up | Rgt \  Left\  Down  |  Rgt \
                 v     v      v      v       v       v
               (2,1) (0,1)  (1,2)  (1,0)   (1,0)   (0,1)
               ='C'  ='#'   ='A'   ='S'    ='S'    ='#'
                !=T  seen   !=T    !=T     !=T     seen
                [X]   [X]    [X]    [X]     [X]     [X]
                 ^                          ^
           (Backtrack)                (Backtrack)
    Result: All paths pruned -> returns False.

Decision Tree Example (Searching for word = "CAT" on same board):
                           (0, 2)='C' [k=0]
                                  |
                             Down |
                                  v
                           (1, 2)='A' [k=1]
                                  |
                            Right |
                                  v
                           (1, 3)='T' [k=2] -> k == len(word) [MATCH! True]

Complexity:
    - Time Complexity:  O(M * N * 3^L), where M x N is the board dimension, 
                        and L is len(word). At each step after the first, 
                        we have at most 3 choices (cannot go back to parent).
    - Space Complexity: O(L) for the recursion call stack (depth equals word length).
                        In-place modification '#' requires O(1) extra space.
"""


def word_search(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, k):
        # Base case: successfully matched all characters in word
        if k == len(word):
            return True

        # Prune: out of bounds or character mismatch / already visited ('#')
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]:
            return False

        # Mark cell as visited in-place for the current path
        temp = board[r][c]
        board[r][c] = '#'

        # Explore all 4 adjacent directions: Down, Up, Right, Left
        # Python's 'or' operator short-circuits as soon as True is found
        found = (dfs(r + 1, c, k + 1) or
                 dfs(r - 1, c, k + 1) or
                 dfs(r, c + 1, k + 1) or
                 dfs(r, c - 1, k + 1))

        # Backtrack: restore the original character for other search paths
        board[r][c] = temp
        return found

    # Try starting the search from every cell on the board
    for r in range(rows):
        for c in range(cols):
            # Only start DFS if the first letter matches
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True

    return False


def main():
    board = [
        ["A", "B", "C", "D"],
        ["S", "A", "A", "T"],
        ["A", "C", "A", "E"]
    ]

    # Test cases
    test_words = ["BAT", "CAT", "ABCC", "SAAE"]
    for w in test_words:
        print(f"Word: '{w}' -> Found: {word_search(board, w)}")


if __name__ == '__main__':
    main()

