"""
Problem: Islands and Treasure (Walls and Gates - LeetCode #286)
==============================================================
You are given an m x n 2D grid initialized with three possible values:
  -  -1 : A water cell / wall that cannot be traversed.
  -   0 : A treasure chest / gate.
  - INF : (2147483647) An empty land cell.

Goal:
Fill each empty land cell with the shortest distance to its nearest treasure chest.
If an empty land cell cannot reach any treasure chest, it should remain INF.

Key Intuition: Multi-Source Breadth-First Search (BFS)
------------------------------------------------------
1. Why not BFS from every empty land cell?
   If there are many empty cells, running a separate BFS from each cell toward the
   nearest treasure would take O((m * n)^2) time, which is too slow (TLE).

2. The Reverse Approach (Multi-Source BFS):
   Instead of searching from each land cell to find a treasure, we search FROM all 
   treasure chests (0s) outward at the same time!
   - Step 1: Find all cells with value 0 and push them into a queue (distance = 0).
   - Step 2: Perform a level-by-level BFS expansion.
   - Step 3: Every cell reached at level `dist` gets updated to that distance.
   - Because BFS explores uniformly layer by layer, the FIRST time we reach an empty 
     cell, we are guaranteed to have found its shortest path to any treasure chest.

Step-by-Step Example Walkthrough:
---------------------------------
Initial Grid:
    [INF,  -1,   0, INF]
    [INF, INF, INF,  -1]
    [INF,  -1, INF,  -1]
    [  0,  -1, INF, INF]

1. Initialization:
   - Identify all chests (0s): positions (0, 2) and (3, 0).
   - Add them to Queue: [(0, 2), (3, 0)] with dist = 0.
   - Mark them as visited.

2. Level 0 (dist = 0):
   - Pop (0, 2) -> grid[0][2] = 0. Valid neighbors: (0, 3) and (1, 2).
   - Pop (3, 0) -> grid[3][0] = 0. Valid neighbor: (2, 0).
   - Queue for Level 1: [(0, 3), (1, 2), (2, 0)].

3. Level 1 (dist = 1):
   - Pop (0, 3) -> grid[0][3] = 1. Neighbor (1, 3) is a wall (-1), skip.
   - Pop (1, 2) -> grid[1][2] = 1. Valid neighbors: (1, 1) and (2, 2).
   - Pop (2, 0) -> grid[2][0] = 1. Valid neighbor: (1, 0).
   - Queue for Level 2: [(1, 1), (2, 2), (1, 0)].

4. Level 2 (dist = 2):
   - Pop (1, 1) -> grid[1][1] = 2. Valid neighbor: (0, 0).
   - Pop (2, 2) -> grid[2][2] = 2. Valid neighbor: (3, 2).
   - Pop (1, 0) -> grid[1][0] = 2. Neighbor (0, 0) is already visited.
   - Queue for Level 3: [(0, 0), (3, 2)].

5. Level 3 (dist = 3):
   - Pop (0, 0) -> grid[0][0] = 3.
   - Pop (3, 2) -> grid[3][2] = 3. Valid neighbor: (3, 3).
   - Queue for Level 4: [(3, 3)].

6. Level 4 (dist = 4):
   - Pop (3, 3) -> grid[3][3] = 4.

Final Updated Grid:
    [ 3, -1,  0,  1]
    [ 2,  2,  1, -1]
    [ 1, -1,  2, -1]
    [ 0, -1,  3,  4]

Complexity Analysis:
--------------------
- Time Complexity: O(m * n)
  Every cell in the m x n grid is visited and enqueued at most once.
- Space Complexity: O(m * n)
  Required for the `visited` set and the BFS queue storing at most m * n coordinates.
"""

from collections import deque

def isIslandAndTreasure(grid):
    """
    Fills each empty land cell with the distance to its nearest treasure chest
    using Multi-Source Breadth-First Search (BFS).
    
    :param grid: List[List[int]] - 2D grid containing -1 (walls), 0 (chests), and INF (land)
    :return: None (modifies grid in-place)
    """
    visited = set()
    m, n = len(grid), len(grid[0])
    q = deque()

    def helper(r, c):
        """Validates boundaries, obstacles, and visit status before enqueueing."""
        if (r < 0 or r == m or c < 0 or
                c == n or (r, c) in visited or grid[r][c] == -1):
            return
        q.append((r, c))
        visited.add((r, c))
    
    # Step 1: Multi-source initialization - add all treasure chests (0s) to the queue
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                q.append((i, j))
                visited.add((i, j))
    
    # Step 2: Level-by-level BFS traversal outward from all treasures simultaneously
    dist = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            grid[r][c] = dist

            # Explore 4-directionally: down, up, right, left
            helper(r+1, c)
            helper(r-1, c)
            helper(r, c+1)
            helper(r, c-1)
        dist += 1

def main():
    INF = 2147483647
    grid = [
        [INF,  -1,   0, INF],
        [INF, INF, INF,  -1],
        [INF,  -1, INF,  -1],
        [  0,  -1, INF, INF]
    ]
    isIslandAndTreasure(grid)
    for row in grid:
        print(row)

if __name__ == "__main__":
    main()
