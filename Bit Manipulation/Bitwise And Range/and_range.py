def rangeBitwiseAnd(left: int, right: int) -> int:
    """
    Returns the bitwise AND of all numbers in the range [left, right].
    
    Approach 1: Bit-by-Bit Flipping Math
    ------------------------------------
    A naive loop (left & left+1 & left+2 ...) is too slow if the range is huge.
    Instead, this approach checks each of the 32 bits individually.
    
    A bit in the final result will be '1' ONLY IF it is '1' in `left`, AND it 
    never flips to '0' while counting up to `right`. 
    Because binary bits flip at predictable intervals (the i-th bit flips every 
    2^(i+1) numbers), we can mathematically calculate exactly how many numbers 
    it will take for a '1' bit to flip to '0'. 
    If the range `right - left` is smaller than the distance to the next flip, 
    the bit survives and stays '1'!
    
    Time Complexity: O(1) - Always exactly 32 loop iterations.
    Space Complexity: O(1)
    """
    res = 0
    for i in range(32):
        # Extract the i-th bit of 'left'
        bit = (left >> i) & 1
        
        # If it's already 0, it will be 0 in the final result anyway. Skip.
        if not bit:
            continue
            
        # Mathematically calculate how many increments until this bit flips to 0
        remainder = left % (1 << (i + 1))
        diff = (1 << (i + 1)) - remainder
        
        # If the end of our range (right) is reached BEFORE the bit flips,
        # it means the bit stays '1' for the entire range! Add it to result.
        if right - left < diff:
            res ^= 1 << i
            
    return res

def rangeBitwiseAnd2(left: int, right: int) -> int:
    """
    Approach 2: Common Prefix (Shift Right then Left)
    -------------------------------------------------
    This is the most elegant and standard solution to this problem.
    
    The Core Idea:
    If `left` and `right` are different, it means we are counting up. 
    Whenever we count up enough to change a higher-order bit, ALL the lower-order 
    bits to its right will eventually cycle through a '0'. 
    Because `0 & anything = 0`, any bit that ever becomes 0 will be 0 in the result.
    
    Therefore, the problem literally just boils down to finding the "Common Prefix"
    of the binary representations of `left` and `right`!
    
    Algorithm:
    1. Keep right-shifting `left` and `right` by 1 until they are exactly equal. 
       This chops off the rightmost bits that don't match, leaving only the 
       common prefix. We keep a `shift` counter to remember how many times we chopped.
    2. Once they match, we left-shift that common prefix back by the `shift` 
       amount, filling all those chopped-off bits with 0s.
       
    Example: left = 5 (101), right = 7 (111)
    - Shift 1: left = 2 (10), right = 3 (11)
    - Shift 2: left = 1 (1),  right = 1 (1) -> MATCH!
    - Result: Left shift 1 by 2 spots -> 100 (which is 4)
    
    Time Complexity: O(log N) - Shifts at most 32 times.
    Space Complexity: O(1)
    """
    shift = 0
    
    # Chop off bits until the prefixes match
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
        
    # Restore the zeroes to the right of the common prefix
    return left << shift

def main():
    """
    Example demonstrating Bitwise AND Range.
    """
    left = 5
    right = 7
    print(f"Approach 1: Range Bitwise AND of {left} and {right} is {rangeBitwiseAnd(left, right)}")
    print(f"Approach 2: Range Bitwise AND of {left} and {right} is {rangeBitwiseAnd2(left, right)}")

if __name__ == "__main__":
    main()
