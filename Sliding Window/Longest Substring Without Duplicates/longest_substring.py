def longestSubString(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    
    Uses an optimized Sliding Window approach with a Hash Map.
    Time Complexity: O(N) where N is the length of the string 's'.
    Space Complexity: O(min(N, M)) where M is the size of the character set (e.g., 256 for ASCII).
    """
    # 'checker' stores the most recent index of each character seen so far.
    checker = {}
    maxLength = 0
    
    # 'start' marks the beginning index of our current valid substring (the "window").
    start = 0
    
    for i in range(len(s)):
        # If we have seen the current character before, we must ensure it's not in our current valid window.
        if s[i] in checker:
            # We move the 'start' of our window to the right of the previous occurrence.
            # max() is used to ensure the 'start' pointer NEVER moves backward.
            # For example, in "abba", when reaching the second 'a', 'start' is already at index 2 (after the first 'b').
            # We don't want to move 'start' back to index 1 (after the first 'a').
            start = max(start, checker[s[i]] + 1)
            
        # Update/record the most recent index of the current character.
        checker[s[i]] = i
        
        # Calculate the length of the current window and update the maximum length found so far in the string.
        maxLength = max(maxLength, i - start + 1)
        
    return maxLength

def main():
    s = "abba"
    # Expected output: 2 (The sub strings are "ab" or "ba")
    print(longestSubString(s))

if __name__ == "__main__":
    main()
