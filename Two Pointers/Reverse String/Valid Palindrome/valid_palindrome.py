import re  # Import regex module for pattern matching and text processing

def findPalindrome(s):
    """
    Determine if a string is a valid palindrome considering only alphanumeric characters.
    
    A palindrome is a word, phrase, or sequence that reads the same forwards and backwards,
    ignoring case, spaces, punctuation, and special characters.
    
    This implementation uses a two-step approach:
    1. Clean the string: Remove all non-alphanumeric characters and convert to lowercase
    2. Compare the cleaned string with its reverse
    
    Example: "Was it a car or a cat I saw?" -> "wasitacaroracatIwas"? No, actually it becomes:
    Step 1: Remove non-alphanumeric: "WasitacaroracatIsaw" -> lowercase: "wasitacaroracatisaw"
    Step 2: Compare with reverse: "wasitacaroracatisaw" == "wasitacaroracatisaw" -> True
    
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(n) for storing the cleaned string and its reverse
    
    This is the standard solution for LeetCode problem 125: Valid Palindrome
    
    Args:
        s (str): The input string to check for palindrome property
        
    Returns:
        bool: True if the string is a palindrome considering only alphanumeric characters,
              False otherwise
    """
    # Step 1: Clean the string
    # re.sub(pattern, replacement, string) - replaces all matches of pattern with replacement
    # r'[^a-zA-Z0-9]' - regex pattern meaning: any character that is NOT (^) a-z, A-Z, or 0-9
    # This removes spaces, punctuation, and special characters
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    
    # Convert all characters to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Step 2: Compare with its reverse
    # s[::-1] is Python slice syntax that reverses the string:
    # [start:stop:step] - with step = -1, it traverses from end to beginning
    # This creates a new reversed string and compares it to the original
    return s == s[::-1]

def main():
    """
    Main function to demonstrate palindrome detection.
    
    Tests the findPalindrome function with a classic palindrome phrase:
    "Was it a car or a cat I saw?"
    
    This is a well-known palindrome that reads the same forwards and backwards
    when ignoring spaces, punctuation, and case.
    
    Expected output: True
    """
    # Classic palindrome phrase with spaces, punctuation, and mixed case
    string = 'Was it a car or a cat I saw?'
    
    # Check if it's a palindrome and print the result
    print(findPalindrome(string))

if __name__ == "__main__":
    main()
