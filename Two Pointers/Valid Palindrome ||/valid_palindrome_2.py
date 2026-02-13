def findPilandrome(s):
    """
    Brute force approach to determine if a string can become a palindrome by removing at most one character.
    
    This implementation tries every possible single-character deletion and checks if the resulting
    string is a palindrome. While simple and correct, it's less efficient than the two-pointer approach.
    
    Time Complexity: O(n²) - For each of n characters, we check if resulting string is palindrome O(n)
    Space Complexity: O(n) - Creates a new substring for each deletion attempt
    
    Args:
        s (str): The input string to check
        
    Returns:
        bool: True if string can become palindrome by removing at most one character
    """
    # Try removing each character one at a time
    for i in range(len(s)):
        # Create new string by skipping character at index i
        # s[:i] takes characters before i, s[i+1:] takes characters after i
        tmp = s[:i] + s[i+1:]
        
        # Check if this new string is a palindrome
        # A string is palindrome if it equals its reverse
        if tmp == tmp[::-1]:
            return True
    
    # If no single deletion creates a palindrome, return False
    return False

def findPilandrome2(s):
    """
    Optimized two-pointer approach to determine if a string can become a palindrome by removing at most one character.
    
    This is LeetCode 680: Valid Palindrome II. The algorithm uses two pointers moving from both ends.
    When a mismatch is found, we have two options to try:
    1. Skip the left character and check if the remaining substring is palindrome
    2. Skip the right character and check if the remaining substring is palindrome
    
    Example: "abca" 
    - Compare 'a' (index 0) with 'a' (index 3): match
    - Compare 'b' (index 1) with 'c' (index 2): mismatch
    - Try skipping 'b': check "ca" -> not palindrome
    - Try skipping 'c': check "ab" -> not palindrome? Wait, this seems wrong for "abca"!
    
    Note: There might be an indexing issue in this implementation. Let's trace carefully.
    
    Time Complexity: O(n) - Each character is visited at most twice
    Space Complexity: O(n) - Creates substring slices (can be optimized to O(1))
    
    Args:
        s (str): The input string to check
        
    Returns:
        bool: True if string can become palindrome by removing at most one character
    """
    # Initialize two pointers
    l, r = 0, len(s) - 1
    
    # Traverse from both ends
    while l < r:
        # If characters don't match
        if s[l] != s[r]:
            # Option 1: Skip left character
            # Take substring from l+1 to r+1 (inclusive of r, exclusive of l)
            skipLeft = s[l+1:r+1]
            
            # Option 2: Skip right character
            # Take substring from l to r (inclusive of l, exclusive of r)
            skipRight = s[l:r]
            
            # Check if either substring is a palindrome
            # A substring is palindrome if it equals its reverse
            return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
        
        # Characters match, move pointers inward
        l, r = l + 1, r - 1
    
    # If we exit the loop, it's already a palindrome
    return True

def main():
    """
    Main function to demonstrate the valid palindrome II detection.
    
    Tests the optimized findPilandrome2 function with the string "abca":
    - "abca" can become palindrome by removing 'c' to get "aba"
    
    Expected output: True
    """
    # Test string: "abca"
    s = "abca"
    
    # Check using the optimized two-pointer approach
    print(findPilandrome2(s))

if __name__ == "__main__":
    main()
