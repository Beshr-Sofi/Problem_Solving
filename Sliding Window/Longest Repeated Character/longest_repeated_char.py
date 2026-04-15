from collections import defaultdict

def longestRepeatedSubString(s: str, k: int) -> int:
    """
    Finds the length of the longest substring containing the same letter 
    you can get after replacing at most 'k' characters.
    
    Uses the Sliding Window technique with a frequency map.
    Time Complexity: O(N) where N is the length of string 's'.
    Space Complexity: O(26) = O(1) to store character frequencies.
    """
    # 'checker' keeps track of the frequency of each character in our current window.
    checker = defaultdict(int)
    maxLength = 0
    
    # 'start' marks the beginning of our current sliding window.
    start = 0
    
    for i in range(len(s)):
        # Expand the window by adding the current character's frequency
        checker[s[i]] += 1
        
        # Find the frequency of the most abundant character in our current window
        maxFreq = max(checker.values())
        
        # The equation: (window_length) - maxFreq 
        # tells us how many characters in the current window need to be replaced 
        # to make all characters in the window identical.
        # If this number exceeds our allowed replacements 'k', the window is invalid.
        while (i - start + 1) - maxFreq > k:
            # Shrink the window from the left until it becomes valid again
            checker[s[start]] -= 1
            start += 1
            
        # Update our maximum length found so far (since the window is now guaranteed valid)
        maxLength = max(maxLength, i - start + 1)
        
    return maxLength
        

def main():
    s = "aaabbb"
    k = 2
    # Expected output: 5 
    # Example valid string: replace the first two 'b's -> "aaaaab" (length 5)
    print(longestRepeatedSubString(s, k))

if __name__ == "__main__":
    main()
