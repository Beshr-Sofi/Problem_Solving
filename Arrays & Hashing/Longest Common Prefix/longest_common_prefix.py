def longestCommonPrefix(strs):
    """
    Find the longest common prefix string amongst an array of strings.
    
    Approach: Horizontal Scanning
    - Compare characters at each position across all strings
    - If any string is shorter or characters don't match, return the prefix found so far
    - Otherwise, add the character to the result
    
    Time Complexity: O(S) where S is the sum of all characters in all strings
    Space Complexity: O(1) excluding the output string
    
    Example:
    Input: ["cog","racecar","car"]
    Output: "" (no common prefix)
    """
    # Initialize an empty string to store the common prefix
    long = ""
    
    # Iterate through each character position in the first string
    for i in range(len(strs[0])):
        # Check if the character at position i is the same in all strings
        for string in strs:
            # If current string is shorter than position i, or character doesn't match
            if i >= len(string) or string[i] != strs[0][i]:
                # Return the prefix found so far
                return long
        
        # If we reach here, the character at position i is common to all strings
        # Add it to the result
        long += strs[0][i]
    
    # Return the complete common prefix
    return long

def main():
    print(longestCommonPrefix(["cog","racecar","car"]))

if __name__ == "__main__":
    main()
