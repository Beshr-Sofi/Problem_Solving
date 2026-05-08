def getSum(a, b):
    """
    Calculates the sum of two integers without using the `+` or `-` operators.
    
    Approach: Bitwise Addition (Half Adder Logic)
    ---------------------------------------------
    To add two numbers without the `+` operator, we must simulate how hardware 
    logic gates perform addition at the binary level.
    
    Binary Addition Rules:
    1. Addition without carrying: 
       0+0=0, 1+0=1, 0+1=1, 1+1=0. 
       This perfectly matches the Bitwise XOR operator (`^`).
       So, `a ^ b` gives us the sum WITHOUT the carry bits.
       
    2. Finding the carries: 
       A carry only happens when both bits are 1 (1+1=10). 
       This matches the Bitwise AND operator (`&`).
       Since a carry shifts over to the next column on the left, we must also 
       Left Shift the result by 1 (`<< 1`).
       So, `(a & b) << 1` gives us all the carry bits.
       
    Algorithm:
    We continuously update `a` to hold the sum-without-carry, and `b` to hold 
    the carries. We repeat this in a loop until there are no more carries left (`b == 0`).
    
    The Python 32-bit Catch:
    Unlike Java or C++, Python integers have infinite precision (they never overflow). 
    If we try to add a negative number, the carry bits will shift to the left 
    forever, causing an infinite loop!
    
    To fix this, we force Python to act like a 32-bit system:
    - We use a 32-bit mask `0xFFFFFFFF` (which is 32 '1's). 
    - Applying `& mask` artificially truncates the numbers to 32 bits on every loop.
    - Finally, if the resulting 32-bit number is negative (i.e., it is greater 
      than `0x7FFFFFFF`, the max positive 32-bit int), we must convert it back 
      from a 32-bit two's complement binary into a standard Python negative integer 
      using `~(a ^ mask)`.
      
    Time Complexity: O(1) - The loop runs at most 32 times (size of the integer).
    Space Complexity: O(1) - No extra memory used.
    """
    # 32-bit mask of all 1s (to force 32-bit overflow behavior)
    mask = 0xFFFFFFFF
    
    # Maximum positive 32-bit integer (used to check if result is negative)
    max_int = 0x7FFFFFFF

    # Loop until there is no carry left
    while b != 0:
        # Calculate the carry bits and shift them left
        carry = (a & b) << 1
        
        # Calculate the sum WITHOUT carries, and apply the 32-bit mask
        a = (a ^ b) & mask
        
        # Update b to hold the carries for the next loop, applying the mask
        b = carry & mask

    # If the 32nd bit is 0, it's positive. Return 'a'.
    # If the 32nd bit is 1, it's negative. Convert it to a Python negative int.
    return a if a <= max_int else ~(a ^ mask)
  
def main():
    """
    Example demonstrating Bitwise Addition.
    """
    a = 1  # Binary: 01
    b = 2  # Binary: 10
    
    # Trace:
    # Loop 1:
    # a ^ b = 01 ^ 10 = 11 (3)
    # a & b = 01 & 10 = 00 << 1 = 00 (0)
    # Result: a=3, b=0. Loop ends.
    
    print(f"{a} + {b} = {getSum(a, b)}")  # Expected output: 3

if __name__ == "__main__":
    main()
