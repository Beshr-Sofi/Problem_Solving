"""
GUESSING GAME - BINARY SEARCH ALGORITHM

This program implements a guessing game using binary search to find a secret 
number between 1 and n. The algorithm efficiently narrows down the search space
by half with each guess.

TIME COMPLEXITY: O(log n) - Binary search divides the search space by 2 each time
SPACE COMPLEXITY: O(1) - Only uses a constant amount of extra space
"""

class Solution:
    """
    Solution class for the guessing number problem.
    Uses binary search to find the secret number efficiently.
    """
    
    def guessNumber(self, n: int) -> int:
        """
        Find the secret number between 1 and n using binary search.
        
        Args:
            n (int): Upper bound of the range to search
            
        Returns:
            int: The secret number that was guessed
        """
        # Initialize binary search pointers
        # l = left pointer (start of range), r = right pointer (end of range)
        l, r = 1, n
        
        # Continue searching while search space exists
        while l <= r:
            # Calculate middle point to eliminate half the search space
            mid = (l + r) // 2
            
            # Call guess function to check if mid is the secret number
            # Returns: 0 if found, 1 if secret is higher, -1 if secret is lower
            check = guess(mid)
            
            # If guess returns 0, we found the secret number
            if not check:
                return mid
            
            # If secret is higher than mid, search in upper half
            # Move left pointer up to narrow the range
            elif check == 1:
                l = mid + 1
            
            # If secret is lower than mid, search in lower half
            # Move right pointer down to narrow the range
            else:
                r = mid - 1


def guess(num: int) -> int:
    """
    Simulates the guessing oracle - represents the external guessing API.
    
    Args:
        num (int): The number to guess
        
    Returns:
        int: -1 if num > secret, 1 if num < secret, 0 if num == secret
    """
    # The secret number we're trying to find
    pick = 6
    
    # Compare the guess with the secret number
    if num < pick:
        # If guess is too low, return 1
        return 1
    elif num > pick:
        # If guess is too high, return -1
        return -1
    else:
        # If guess is correct, return 0
        return 0


def main():
    """
    Main function to test the guessing game.
    
    EXAMPLE EXECUTION (with n=10, secret number=6):
        Step 1: l=1, r=10, mid=5 → guess(5)=-1 → secret is higher
        Step 2: l=6, r=10, mid=8 → guess(8)=-1 → secret is lower
        Step 3: l=6, r=7, mid=6 → guess(6)=0 → FOUND! Return 6
    """
    # Set the upper bound for the search range
    n = 10
    
    # Create a Solution instance
    sol = Solution()
    
    # Find the secret number and print the result
    print(sol.guessNumber(n))


if __name__ == "__main__":
    # Execute main function when script is run directly
    main()
