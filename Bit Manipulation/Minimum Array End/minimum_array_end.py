def minEnd(n: int, x: int) -> int:
    """
    Finds the minimum possible last element of a strictly increasing array 
    of size 'n' where the bitwise AND of all elements equals 'x'.
    
    Approach: Bit Slotting (Merging n-1 into the zeros of x)
    --------------------------------------------------------
    If the bitwise AND of the entire array must exactly equal `x`, it means every 
    single number in the array MUST have all the '1' bits that `x` has.
    The '1' bits in `x` are strictly "fixed". We cannot change them.
    However, the '0' bits in `x` are "free". We can flip them to '1's to create 
    new, larger numbers!
    
    To make the numbers strictly increasing while keeping them as small as possible, 
    we want to build them by sequentially counting up (0, 1, 2, 3...) and placing 
    that binary count *only* into the "free" '0' spots of `x`.
    
    Because the first number in our array will just be `x` itself (which represents 
    adding a count of 0), the `n`-th number in the array will represent adding a 
    count of `n - 1`.
    
    Algorithm:
    1. Decrement `n` by 1. We now want to slot the binary representation of `n` 
       into the zero-bits of `x`.
    2. We use `i` to iterate through every bit position of `x` (from right to left).
    3. If the `i`-th bit of `x` is a `0`, it's a "free" spot!
       - We take the rightmost bit of `n` (`n & 1`).
       - We slide it over to position `i` (`<< i`).
       - We stick it into `x` using Bitwise OR (`x |=`).
       - We then shift `n` to the right (`n >>= 1`) to grab the next bit of `n`.
    4. We increment `i` to check the next bit of `x`, and repeat until `n` runs 
       out of bits.
       
    Example: minEnd(5, 3) 
    - x = 3 (Binary: 00011). The '1's are fixed. The '0's are free.
    - n = 5. n - 1 = 4 (Binary: 100).
    - We take the bits of '100' and slot them into the free zeros of '00011'.
    - Result: 10011 (which is 19 in decimal).
    
    Time Complexity: O(log N) - The loop runs exactly as many times as there are 
                     bits in `n` plus the number of '1' bits in `x` it has to skip.
    Space Complexity: O(1)
    """
    i = 0
    
    # We want the (n-1)th number after x
    n -= 1
    
    # Loop until we have slotted all bits of n
    while n > 0:
        # Check if the i-th bit of x is a '0' (a free spot)
        if ((1 << i) & x) == 0:
            # Slot the rightmost bit of n into this free spot
            x |= (n & 1) << i
            # Shift n to prepare its next bit for the next free spot
            n >>= 1
            
        # Always move to the next bit position in x
        i += 1

    return x

def main():
    """
    Example demonstrating Minimum Array End.
    """
    # Expected output: 19
    print(minEnd(5, 3))

if __name__ == "__main__":
    main()
