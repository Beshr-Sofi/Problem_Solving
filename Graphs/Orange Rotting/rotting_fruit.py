"""
You are given an m x n grid where each cell can have one of three values:
  - 0 : Empty cell
  - 1 : Fresh orange
  - 2 : Rotten orange

Every minute, any fresh orange that is 4-directionally adjacent (up, down, left, right)
to a rotten orange becomes rotten.

Goal:
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible (i.e. some fresh orange cannot be reached), return -1.

Key Intuition: Multi-Source Breadth-First Search (BFS)
------------------------------------------------------
1. Simultaneous Rotting:
   All rotten oranges simultaneously infect their adjacent fresh neighbors each minute.
   This parallel, level-by-level spreading is the textbook definition of Breadth-First
   Search (BFS).

2. Multi-Source Initialization:
   Instead of starting BFS from a single source, we insert ALL initially rotten oranges
   into the queue at minute 0. We also count the total number of fresh oranges.

3. Minute-by-Minute (Level-by-Level) Traversal:
   - For each minute, process all rotten oranges currently in the queue (the current layer).
   - For each rotten orange, inspect its 4 neighbors.
   - If a neighbor is a fresh orange (value 1) and not yet visited:
     * Mark it as visited (it is now rotting).
     * Decrement the `freshOranges` count.
     * Enqueue it so it can rot its own neighbors in the next minute.
   - Increment the elapsed minutes (`result`).

4. Termination & Result:
   - If `freshOranges == 0` at the start, return 0 (no time needed).
   - The while loop runs one extra level where the queue processes the last batch of
     oranges but finds no new fresh neighbors to infect, so the final elapsed time is
     `result - 1`.
   - If `freshOranges` is still greater than 0 after BFS finishes, some oranges were
     unreachable; return -1.

Step-by-Step Example Walkthrough:
---------------------------------
Grid:
    [1, 1, 0]
    [0, 1, 1]
    [0, 1, 2]

Initial State:
  - Rotten oranges at: (2, 2) -> Queue: [(2, 2)]
  - Fresh oranges count = 5: at (0, 0), (0, 1), (1, 1), (1, 2), (2, 1)

Minute 1:
  - Pop (2, 2). Fresh neighbors: (2, 1) and (1, 2) rot.
  - Queue: [(2, 1), (1, 2)]
  - Fresh remaining: 3

Minute 2:
  - Pop (2, 1): neighbor (1, 1) rots.
  - Pop (1, 2): neighbor (1, 1) already visited.
  - Queue: [(1, 1)]
  - Fresh remaining: 2

Minute 3:
  - Pop (1, 1): neighbor (0, 1) rots.
  - Queue: [(0, 1)]
  - Fresh remaining: 1

Minute 4:
  - Pop (0, 1): neighbor (0, 0) rots.
  - Queue: [(0, 0)]
  - Fresh remaining: 0 (all fresh oranges are now rotten!)

Minute 5 (Final check layer):
  - Pop (0, 0): no unvisited fresh neighbors.
  - Queue becomes empty.
  - Result increments to 5.

Final return: `result - 1` = 5 - 1 = 4 minutes.

Complexity Analysis:
--------------------
- Time Complexity: O(m * n)
  Each cell is visited and processed at most once during the BFS traversal.
- Space Complexity: O(m * n)
  The queue and visited set store at most m * n coordinates in the worst case.
"""

from collections import deque

def orangeRotting(grid):
    """
    Calculates the minimum minutes to rot all fresh oranges using Multi-Source BFS.
    
    :param grid: List[List[int]] - m x n matrix of 0 (empty), 1 (fresh), 2 (rotten)
    :return: int - Minimum minutes needed, or -1 if impossible
    """
    visited = set()
    freshOranges = 0
    q = deque()
    m, n = len(grid), len(grid[0])
    result = 0

    # Step 1: Initialize multi-source queue with all rotten oranges and count fresh ones
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                visited.add((i, j))
                q.append((i, j))
            elif grid[i][j] == 1:
                freshOranges += 1

    def helper(r, c):
        """Helper to validate cell bounds, visited state, and rot fresh oranges."""
        nonlocal freshOranges
        if r < 0 or r == m or c < 0 or c == n or (r, c) in visited or grid[r][c] != 1:
            return
        visited.add((r, c))
        freshOranges -= 1
        q.append((r, c))
    
    # Step 2: Multi-source BFS layer-by-layer (each layer represents 1 minute)
    while q:
        for i in range(len(q)):
            r, c = q.popleft()

            # Explore 4-directional neighbors: down, up, right, left
            helper(r + 1, c)
            helper(r - 1, c)
            helper(r, c + 1)
            helper(r, c - 1)

        result += 1
    
    # Step 3: result - 1 compensates for the final round where no new oranges were rotted
    return result - 1 if not freshOranges else -1

def main():
    grid = [
        [1, 1, 0],
        [0, 1, 1],
        [0, 1, 2]
    ]
    print("Minutes to rot all oranges:", orangeRotting(grid))

if __name__ == "__main__":
    main()
