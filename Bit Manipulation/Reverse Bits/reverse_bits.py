def reverseBits(n: int) -> int:
    """
    Reverses the bits of a given 32-bit unsigned integer.
    
    Approach: Bit-by-Bit Mirroring
    ------------------------------
    The goal is to take a 32-bit binary sequence and flip it backwards. The 0th bit 
    (from the right) should move to the 31st position. The 1st bit should move to 
    the 30th position, and so on.
    
    Algorithm:
    1. Initialize an empty result variable `res = 0` (all bits are 0).
    2. Loop exactly 32 times, once for each bit in a 32-bit integer.
    3. During each iteration `i` (from 0 to 31):
       - Check the rightmost bit of `n` using Bitwise AND (`n & 1`).
       - If the bit is a 1, we must place a 1 in its mirrored position in `res`.
         - The mirrored position for index `i` is `(31 - i)`.
         - We create a bitmask with a 1 in exactly that position using a Left 
           Shift: `(1 << (31 - i))`.
         - We write that 1 into `res` using Bitwise XOR (`res ^= ...`). 
           (Note: Bitwise OR `|=` would also work perfectly here since `res` starts 
           with 0s).
       - Finally, shift `n` one position to the right (`n >>= 1`) so that the next 
         bit drops into the rightmost position to be checked on the next loop.
         
    Time Complexity: O(1) - The loop runs exactly 32 times, which is a constant 
                     amount of work regardless of the input size.
    Space Complexity: O(1) - We only use a single `res` variable.
    """
    res = 0
    
    # Process all 32 bits of the integer
    for i in range(32):
        
        # If the current rightmost bit is a 1...
        if n & 1:
            # Place a 1 in the corresponding reversed position in our result
            res ^= (1 << (31 - i))
            
        # Shift n to the right to process the next bit
        n >>= 1
        
    return res

def main():
    """
    Example demonstrating Reverse Bits.
    
    Input:  10 (Binary: 00000000000000000000000000001010)
    Reversed:   (Binary: 01010000000000000000000000000000)
    Output: 1342177280
    """
    # 2818572288 is 10101000000000000000000000000000 in binary
    # When reversed, it becomes 21 (00000000000000000000000000010101)
    print(reverseBits(2818572288))  # Expected output: 21

if __name__ == '__main__':
    main()
