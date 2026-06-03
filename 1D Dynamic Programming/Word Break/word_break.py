def wordBreak(s, wordDict):
    """
    Determine if the string `s` can be segmented into a space-separated sequence of 
    one or more dictionary words.
    
    Approach: Bottom-Up Dynamic Programming
    - `dp[i]` represents whether the substring `s[i:]` can be successfully broken down.
    - Base case: `dp[len(s)] = True` because an empty string is always valid.
    - We iterate backward from the end of the string down to index 0.
    - At each index `i`, we check every word `j` in the `wordDict`.
    - If the word `j` matches the substring starting at `i` (`s[i: i + len(j)]`), 
      then `dp[i]` inherits the truth value of `dp[i + len(j)]`.
    - If `dp[i]` becomes True, we can stop checking other words for this index.
      
    Time Complexity: O(N * M * L) where N is the length of `s`, M is the number of words 
      in `wordDict`, and L is the max length of a word (due to string comparison/slicing).
    Space Complexity: O(N) for the DP array of size N + 1.
    """
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
        
    for i in range(len(s) - 1, -1, -1):
        for j in wordDict:
            # Check if the word fits within bounds and matches the substring
            if i + len(j) <= len(s) and s[i: i+ len(j)] == j:
                # If it matches, check if the remaining substring can also be broken down
                dp[i] = dp[i + len(j)]
                
                # If we found a valid segmentation from index i, no need to check other words
                if dp[i]:
                    break
    return dp[0]

def main():
    s = "leetcode"
    wordDict = ["leet","code"]
    print(wordBreak(s, wordDict))

if __name__ == "__main__":
    main()
