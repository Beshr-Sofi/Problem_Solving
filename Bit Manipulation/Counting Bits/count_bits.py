def countBits(n):
    """
    Returns an array where the i-th element is the number of 1s in the binary 
    representation of i (for 0 <= i <= n).
    
    Approach 1: Built-in Conversion (Brute Force)
    ---------------------------------------------
    This is the most straightforward approach. For every single number from 0 to n, 
    we convert it to a binary string and count the '1's.
    
    Time Complexity: O(n log n) - For each of the n numbers, counting the bits 
                     takes time proportional to the number of bits (log n).
    Space Complexity: O(n) - To store the result array.
    """
    return [bin(x).count('1') for x in range(n + 1)]

def countBits1(n):
    """
    Approach 2: Dynamic Programming (Most Significant Bit / Offset)
    ---------------------------------------------------------------
    This is a highly optimized O(n) approach that uses patterns in binary numbers
    and Dynamic Programming (DP) to build the answers iteratively.
    
    The Pattern:
    Let's look at the number of 1s for the first few numbers:
    0: 0000 -> 0 1s
    -------- (Offset 1, power of 2)
    1: 0001 -> 1 1s  (1 + dp[0])
    -------- (Offset 2, power of 2)
    2: 0010 -> 1 1s  (1 + dp[0])
    3: 0011 -> 2 1s  (1 + dp[1])
    -------- (Offset 4, power of 2)
    4: 0100 -> 1 1s  (1 + dp[0])
    5: 0101 -> 2 1s  (1 + dp[1])
    6: 0110 -> 2 1s  (1 + dp[2])
    7: 0111 -> 3 1s  (1 + dp[3])
    
    Notice that the number of 1s repeats itself! Every time we hit a new power of 2
    (1, 2, 4, 8, 16...), the binary representation resets to having exactly one '1' at 
    the very front, followed by the exact same sequence of bits as the numbers we 
    already calculated.
    
    Algorithm:
    1. We maintain an `offset` which represents the highest power of 2 we have seen 
       so far.
    2. We iterate from 1 to n.
    3. If `i` hits the NEXT power of 2 (`offset * 2 == i`), we update our offset 
       to this new power of 2.
    4. The answer for `i` is simply `1` (for the new most-significant bit) PLUS the 
       answer we previously calculated for `i - offset`.
       
    Time Complexity: O(n) - We calculate the answer for each number in O(1) time 
                     using our pre-calculated DP array!
    Space Complexity: O(n) - To store the result DP array.
    """
    dp = [0] * (n + 1)
    offset = 1  # Tracks the highest power of 2 seen so far
    
    for i in range(1, n + 1):
        # If we reach the next power of 2 (e.g. 1->2, 2->4, 4->8), update the offset
        if offset * 2 == i:
            offset = i
            
        # The bits for 'i' are exactly the bits for (i - offset), plus one extra '1' 
        # at the front.
        dp[i] = 1 + dp[i - offset]
        
    return dp

def main():
    """
    Example demonstrating Counting Bits.
    
    n = 5
    Expected output: [0, 1, 1, 2, 1, 2]
    """
    n = 5
    print("Approach 1 (Brute Force):", countBits(n))
    print("Approach 2 (DP Optimized):", countBits1(n))

if __name__ == "__main__":
    main()
