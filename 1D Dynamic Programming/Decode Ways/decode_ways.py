def numDecodings(s: str) -> int:
    """
    Find the total number of ways to decode a string of digits into letters.
    
    Approach: Top-Down Dynamic Programming (Memoization)
    - We use a recursive function `helper(index)` that calculates the number of valid 
      decodings for the substring starting at `index`.
    - Base case 1: If we reach the end of the string, it means we found 1 valid decoding path.
    - Base case 2: If the current digit is '0', it cannot be decoded (no mapping for '0').
    - Recursive step: We can always take a single digit (if it's not '0'). We can also take 
      two digits if they form a number between 10 and 26.
    - We cache the result of each index in a dictionary `dp` to avoid recalculating overlapping subproblems.
      
    Time Complexity: O(N) where N is the length of `s`. Due to memoization, each index 
      is evaluated at most once. Without memoization, it would be O(2^N).
    Space Complexity: O(N) for the recursion stack and the `dp` dictionary.
    """
    dp = {}
    
    def helper(index):
        # Return cached result if already computed
        if index in dp:
            return dp[index]

        # Reached the end of the string successfully
        if index >= len(s):
            return 1

        # A string starting with '0' cannot be decoded
        if s[index] == '0':
            return 0

        # Decode as a single digit
        total_ways = helper(index + 1)
        
        # Decode as a pair of digits (if they form a valid letter A-Z, i.e., <= 26)
        if index + 1 < len(s) and int(s[index:index+2]) <= 26:
            total_ways += helper(index + 2)
            
        # Cache the result
        dp[index] = total_ways
        return total_ways

    return helper(0)

def main():
    s = '226'
    print(numDecodings(s))

if __name__ == "__main__":
    main()
