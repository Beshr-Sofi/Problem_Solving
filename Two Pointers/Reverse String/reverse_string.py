def reverseString(s: list[str]):
    """
    Reverse a string in-place by modifying the input list of characters.
    
    This function reverses the given list of characters using a two-pointer approach.
    It modifies the original list directly without using extra space for another array.
    
    The algorithm:
    1. Initialize left pointer at start (index 0) and right pointer at end (index len-1)
    2. Swap characters at left and right positions
    3. Move left pointer rightward and right pointer leftward
    4. Continue until pointers meet in the middle (process half the array)
    
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1) - in-place reversal using constant extra space
    
    This is the standard solution for LeetCode problem 344: Reverse String
    
    Args:
        s (list[str]): A list of characters representing the string to reverse
                       The list is modified in-place, nothing is returned
    
    Returns:
        None: The function modifies the input list directly
    """
    # Initialize two pointers: left at start, right at end
    l, r = 0, len(s) - 1
    
    # Only need to iterate through half the array
    # When pointers meet or cross, the entire string is reversed
    for i in range(len(s) // 2):
        # Swap characters at left and right positions using tuple unpacking
        # This is a Pythonic way to swap values without a temporary variable
        s[l], s[r] = s[r], s[l]
        
        # Move pointers toward the center
        l += 1  # Left pointer moves right
        r -= 1  # Right pointer moves left
        
        # Visual representation of each swap:
        # Iteration 1: ["h","e","l","l","o"] -> ["o","e","l","l","h"] (swap h and o)
        # Iteration 2: ["o","e","l","l","h"] -> ["o","l","l","e","h"] (swap e and l)

def main():
    """
    Main function to demonstrate the in-place string reversal.
    
    Creates a list of characters representing the string "hello",
    reverses it in-place, and prints the result.
    
    Expected output: ['o', 'l', 'l', 'e', 'h']
    """
    # Input string "hello" represented as a list of characters
    s = ["h", "e", "l", "l", "o"]
    
    # Reverse the string in-place
    reverseString(s)
    
    # Print the modified list
    print(s)

if __name__ == "__main__":
    main()
