r"""
Problem:
    Given an m x n 2D binary grid 'grid' which represents a map of '1's (land)
    and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands
    horizontally or vertically. You may assume all four edges of the grid are
    surrounded by water.

Algorithm: Connected Components via Depth-First Search (DFS)
    1. Scan the grid cell by cell:
       - Iterate through every row i and column j.
       - When we encounter grid[i][j] == '1' that is NOT yet visited:
         - We have discovered a new island -> increment result += 1.
         - Trigger a DFS traversal from (i, j) to explore and mark all horizontally
           and vertically connected land cells of this island.
    2. DFS Traversal (Flood Fill):
       - Mark the current cell (row, column) as visited so it won't be counted again.
       - Look in all 4 cardinal directions:
         * Up:    (-1,  0)
         * Down:  (+1,  0)
         * Right: ( 0, +1)
         * Left:  ( 0, -1)
       - For each neighbor (r, c), if it is within grid bounds, contains '1',
         and is not yet visited, recursively call dfs(r, c).
    3. Return the total island count accumulated in result.

DFS Traversal Tree Example:
    Grid:
        ['1', '1', '0']
        ['1', '0', '0']
        ['0', '0', '1']

    1) Scanning starts at (0, 0): grid[0][0] == '1' (unvisited)
       -> Island #1 found! result = 1.
       -> DFS Traversal Tree for Island #1:

                      DFS((0, 0)) [visited]
                      /         \
                Down /           \ Right
                    v             v
               DFS((1, 0))    DFS((0, 1))
               [visited]      [visited]
                 /    \          /    \
             (neighbors      (neighbors
             water/visited)  water/visited)

       All cells in Island #1 {(0,0), (1,0), (0,1)} are now marked.

    2) Continue scanning:
       (0, 1): already visited -> skip
       (0, 2): '0' (water)     -> skip
       (1, 0): already visited -> skip
       (1, 1) to (2, 1): '0'   -> skip
       (2, 2): grid[2][2] == '1' (unvisited)
       -> Island #2 found! result = 2.
       -> DFS Traversal Tree for Island #2:

                      DFS((2, 2)) [visited]
                      (all 4 directions are water/out of bounds)

    Final Result: 2 islands.

Complexity:
    - Time Complexity:  O(M * N), where M = number of rows, N = number of columns.
                        Every cell is visited a constant number of times (at most
                        once by the outer loop and checked 4 times by DFS neighbors).
    - Space Complexity: O(M * N) in the worst case (e.g. an entire grid of '1's)
                        for the recursion call stack and visited tracking.
"""


def numIlands(grid):
    """
    Counts the number of connected islands in an m x n binary grid.
    """
    if not grid or not grid[0]:
        return 0

    visited = set()
    result = 0
    m, n = len(grid), len(grid[0])
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def dfs(row, column):
        # Mark current cell as visited
        visited.add((row, column))

        # Explore all 4 adjacent directions: Up, Down, Right, Left
        for dr, dc in directions:
            r, c = row + dr, column + dc
            # Valid next step: within bounds, is land ('1'), and not yet visited
            if 0 <= r < m and 0 <= c < n and grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)

    # Scan every cell in the grid
    for i in range(m):
        for j in range(n):
            # Found unvisited land -> new island
            if grid[i][j] == '1' and (i, j) not in visited:
                result += 1
                dfs(i, j)  # Traverse and mark all cells in this island

    return result


# Alias with standard LeetCode spelling
numIslands = numIlands


def main():
    test_cases = [
        # Test 1: Diagonal lands (not connected) -> 3 islands
        ([["1", "0", "0"],
          ["0", "1", "0"],
          ["0", "0", "1"]], "Diagonal cells"),

        # Test 2: Single large connected island -> 1 island
        ([["1", "1", "1", "1", "0"],
          ["1", "1", "0", "1", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "0", "0", "0"]], "Single large island"),

        # Test 3: Multiple distinct islands -> 3 islands
        ([["1", "1", "0", "0", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "1", "0", "0"],
          ["0", "0", "0", "1", "1"]], "Three separate islands"),

        # Test 4: All water -> 0 islands
        ([["0", "0"],
          ["0", "0"]], "All water"),
    ]

    for grid, description in test_cases:
        count = numIlands(grid)
        print(f"[{description}] -> Number of Islands: {count}")


if __name__ == "__main__":
    main()
