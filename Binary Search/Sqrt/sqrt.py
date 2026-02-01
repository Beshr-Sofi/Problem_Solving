"""
This module implements an integer square root function using binary search.
It finds the floor of the square root of a given number efficiently in O(log n) time.
"""

def sqrt(x):
    """
    Calculate the integer square root of x using binary search.
    
    This function finds the largest integer whose square is less than or equal to x.
    Uses binary search algorithm for efficient O(log n) time complexity.
    
    Args:
        x (int): Non-negative integer to find the square root of
        
    Returns:
        int: The floor of the square root of x
        
    Examples:
        >>> sqrt(15)
        3
        >>> sqrt(4)
        2
        >>> sqrt(0)
        0
    """
    # Edge cases: if x is 0 or 1, return x itself
    if not x or x == 1:
        return x
    
    # Initialize binary search boundaries
    # Left pointer starts at 1, right pointer at x//2
    # (square root of x cannot be greater than x//2 for x > 1)
    l, r = 1, x // 2
    
    # Binary search to find the square root
    while l <= r:
        # Calculate middle value to test
        mid = (l + r) // 2
        check = mid * mid
        
        # If mid squared equals x, we found the exact square root
        if check == x:
            return mid
        
        # If mid squared is greater than x, search in lower half
        if check > x:
            r = mid - 1
        # If mid squared is less than x, search in upper half
        else:
            l = mid + 1
    
    # Return l-1 as it will be the floor of the square root
    # (the largest integer whose square doesn't exceed x)
    return l - 1

def main():
    """
    Main function to test the sqrt function with sample values.
    """
    # Test values to find square roots for
    test_values = [15, 4, 0, 1, 16, 25, 26, 100, 2147395599]
    
    # Iterate through each test value and print its square root
    for val in test_values:
        print(f"The integer square root of {val} is {sqrt(val)}")
    
if __name__ == "__main__":
    # Execute main function when script is run directly
    main()
