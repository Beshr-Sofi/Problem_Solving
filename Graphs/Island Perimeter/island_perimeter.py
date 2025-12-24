def islandPerimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    :param grid: List[List[int]] - 2D grid representing the map (1 = land, 0 = water)
    :return: int - perimeter of the island
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Check all four directions
                # Up
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Down
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter

def main():
    # Example usage
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    print(islandPerimeter(grid))  # Output: 16

if __name__ == "__main__":
    main()
