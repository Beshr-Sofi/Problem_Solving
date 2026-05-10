from collections import defaultdict

class CountSquares:
    """
    A data structure that tracks points on an X-Y plane and counts how many 
    axis-aligned squares can be formed using a given query point.
    
    Approach: Hash Map & Diagonal Search
    ------------------------------------
    An axis-aligned square has 4 points. If we are given a query point (qx, qy), 
    we need to find 3 other points to complete the square.
    
    The Mathematical Trick:
    Instead of searching for 3 points, we only need to search for ONE point: 
    the diagonal point (px, py).
    If we know the diagonal point, the other two corners of an axis-aligned 
    square MUST be at exactly (px, qy) and (qx, py)!
    
    Data Structure:
    Because duplicate points can exist and count as distinct points for forming 
    squares, we use a `defaultdict(int)` to map a coordinate tuple `(x, y)` to 
    the number of times it has been added.
    """
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point) -> None:
        """
        Adds a point to the data structure.
        Time Complexity: O(1)
        """
        # Convert the list to a tuple so it can be used as a dictionary key
        self.points[tuple(point)] += 1

    def count(self, point) -> int:
        """
        Counts the number of axis-aligned squares that can be formed.
        
        Algorithm:
        1. Iterate through every point we've ever added. Let's pretend this point 
           is our diagonal point (px, py).
        2. How do we verify it's a valid diagonal for a square?
           - The horizontal width `abs(qx - px)` must exactly equal the vertical 
             height `abs(qy - py)`.
           - The square must have an area > 0, meaning the diagonal point cannot 
             have the same x-coordinate as the query point (`qx != px`).
        3. If it is a valid diagonal, we check if the other two required corners 
           `(px, qy)` and `(qx, py)` exist in our dictionary.
        4. The total number of valid squares formed by this specific combination 
           is the mathematical product of the counts of the 3 points!
           
        Time Complexity: O(N) where N is the number of unique points added so far.
        Space Complexity: O(1) for this specific method execution.
        """
        total_squares = 0
        qx, qy = point

        # Loop through all unique points to find potential diagonals
        for px, py in list(self.points.keys()):
            # Check if it forms a square (Width == Height) and Area > 0
            if abs(qx - px) == abs(qy - py) and qx != px:
                
                # If the other two corners exist, their counts will be > 0.
                # Multiply the counts of the 3 required points together. 
                # (If any are missing, the dictionary returns 0, and the product becomes 0!)
                total_squares += (self.points[(px, py)] * 
                                  self.points[(px, qy)] * 
                                  self.points[(qx, py)])
                                  
        return total_squares

def main():
    """
    Example demonstrating Detect Squares.
    
    We add points at (1,1), (3,1), and (1,3).
    We query (3,3). 
    These four points form a perfect 2x2 square!
    Expected Output: 1
    """
    square = CountSquares()
    square.add([1, 1])
    square.add([3, 1])
    square.add([1, 3])
    
    print(f"Squares formed with query [3,3]: {square.count([3, 3])}")

if __name__ == "__main__":
    main()
