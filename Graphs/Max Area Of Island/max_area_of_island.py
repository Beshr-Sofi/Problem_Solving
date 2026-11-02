r"""
LeetCode 695: Max Area of Island

Problem:
    You are given an m x n binary matrix 'grid'. An island is a group of 1's 
    (representing land) connected 4-directionally (horizontal or vertical).
    The area of an island is the number of cells with a value 1 in the island.
    
    Return the maximum area of an island in 'grid'. If there is no island, return 0.

Algorithm / How the Solution Works:
    1. Outer Loop (Scan):
       - Scan through every cell (i, j) in the grid.
       - If grid[i][j] == 1 and it hasn't been visited yet, a new island is found.
       - Launch dfs(i, j, size=1) to explore the entire island and calculate its area.
       - Update result = max(result, island_area).

    2. DFS Traversal (Accumulative Area via 'size'):
       - Mark current cell (row, column) in 'visited'.
       - For each of the 4 directions (Up, Down, Right, Left):
         * Calculate neighbor (r, c) = (row + dr, column + dc).
         * If (r, c) is within bounds, is land (grid[r][c] == 1), and unvisited:
           - Recurse: size = dfs(r, c, size + 1).
           - Passing (size + 1) increments the count for each newly discovered cell,
             and reassigning 'size' chains the accumulated area forward through
             all subsequent branches.
       - Return the final accumulated 'size'.

DFS Traversal Tree Example (from main's grid):
    Island on the right column has 4 cells: (0,4) -> (1,4) -> (2,4) -> (3,4)
    Island in the middle has 6 cells:
        (0, 1) = 1  --- (0, 2) = 1
                           |
                        (1, 2) = 1
                           |
        (2, 1) = 1  --- (2, 2) = 1
           |
        (3, 1) = 1

    Starting DFS at (0, 1) with size = 1:

                          dfs((0, 1), size=1)
                         /                   \
                   Down /                     \ Right
                       v                       v
               (0,0)=0 (water)            dfs((0, 2), size=2)
                                                  |
                                                  | Down
                                                  v
                                          dfs((1, 2), size=3)
                                                  |
                                                  | Down
                                                  v
                                          dfs((2, 2), size=4)
                                                  |
                                                  | Left
                                                  v
                                          dfs((2, 1), size=5)
                                                  |
                                                  | Down
                                                  v
                                          dfs((3, 1), size=6)
                                                  |
                                         (all neighbors visited
                                          or water) -> returns 6

    The max area found across all islands is 6.

Complexity:
    - Time Complexity:  O(M * N), where M = rows and N = columns.
                        Each cell is visited at most once; 4 directions are checked
                        per cell in O(1) time.
    - Space Complexity: O(M * N) in the worst case for recursion stack depth
                        and the 'visited' set.
"""


def maxAreaOfIsland(grid):
  visited = set()
  result = 0
  m, n = len(grid), len(grid[0])
  directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

  def dfs(row, column, size):
    visited.add((row, column))

    for dr, dc in directions:
      r, c = row + dr, column + dc
      if 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and (r, c) not in visited:
        size = dfs(r, c, size+1)
    return size

  for i in range(m):
    for j in range(n):
      if grid[i][j] == 1 and (i, j) not in visited:
        result = max(result, dfs(i, j, 1))
            
  return result

def main():
  grid = [
    [0,1,1,0,1],
    [1,0,1,0,1],
    [0,1,1,0,1],
    [0,1,0,0,1]
  ]

  print(maxAreaOfIsland(grid))

if __name__ == "__main__":
  main()
