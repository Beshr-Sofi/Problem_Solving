def mergeAlternately(word1, word2):
    """
    Merge two strings alternately, character by character.
    
    This function takes two strings and merges them by alternating characters.
    If one string is longer than the other, the remaining characters from the
    longer string are appended to the end of the result.
    
    This is LeetCode problem 1768: Merge Strings Alternately.
    
    Example: 
        word1 = "abc", word2 = "pqr" -> "apbqcr"
        word1 = "ab", word2 = "pqrs" -> "apbqrs"
        word1 = "abcd", word2 = "pq" -> "apbqcd"
    
    Time Complexity: O(n + m) where n = len(word1), m = len(word2)
    Space Complexity: O(n + m) for the result string
    
    Args:
        word1 (str): First string to merge
        word2 (str): Second string to merge
        
    Returns:
        str: Merged string with alternating characters from word1 and word2
    """
    result = ''  # Initialize empty result string
    
    # Iterate through the length of word1 (shorter or equal to word2)
    for i in range(len(word1)):
        # Add character from word1 at position i
        result += word1[i]
        
        # Add character from word2 at position i if word2 has enough characters
        # If i is beyond word2's length, add nothing (empty string)
        result += word2[i] if i < len(word2) else ''
    
    # After processing all characters from word1, append any remaining
    # characters from word2 starting from index len(word1)
    # This handles cases where word2 is longer than word1
    result += word2[len(word1):]
    
    return result

def main():
    """
    Main function to demonstrate merging strings alternately.
    
    Tests the mergeAlternately function with:
    - word1 = "abc"
    - word2 = "pqr"
    
    Expected output: "apbqcr"
    """
    word1 = "abc"
    word2 = "pqr"
    
    # Merge the strings and print the result
    print(mergeAlternately(word1, word2))  # Output: "apbqcr"

if __name__ == "__main__":
    main()
