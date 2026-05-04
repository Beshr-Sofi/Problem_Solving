def numberOfOnes(n):
    """
    Calculates the number of '1' bits (also known as Hamming Weight) in the 
    binary representation of an integer.
    
    Approach 1: Bit Manipulation (Shift and Check)
    ----------------------------------------------
    We can count the '1's by checking one bit at a time, starting from the 
    rightmost bit (Least Significant Bit), and then shifting the bits over.
    
    Algorithm:
    1. Loop while `n` is greater than 0.
    2. Check the rightmost bit using Bitwise AND (`n & 1`). 
       - If the rightmost bit is 1, `n & 1` equals 1.
       - If the rightmost bit is 0, `n & 1` equals 0.
       We add this result directly to our counter.
    3. Shift all bits to the right by one position using Bitwise Right Shift (`n >>= 1`).
       - This effectively chops off the rightmost bit we just checked, and shifts 
         the next bit into the rightmost position to be checked on the next loop.
         
    Example Trace for n = 23 (Binary: 10111):
    - Loop 1: 10111 & 1 == 1. Count = 1. Shift -> 1011
    - Loop 2: 1011 & 1 == 1.  Count = 2. Shift -> 101
    - Loop 3: 101 & 1 == 1.   Count = 3. Shift -> 10
    - Loop 4: 10 & 1 == 0.    Count = 3. Shift -> 1
    - Loop 5: 1 & 1 == 1.     Count = 4. Shift -> 0 (Loop ends)
    
    Time Complexity: O(log N) - The loop runs once for every bit in the number.
    Space Complexity: O(1) - Only a single counter variable is used.
    """
    cnt = 0
    while n:
        # Check if the rightmost bit is a 1
        cnt += 1 if (n & 1) == 1 else 0
        # Shift bits right by 1 to process the next bit
        n >>= 1
    return cnt

def numberOfOnes2(n):
    """
    Approach 2: Python Built-in String Conversion
    ---------------------------------------------
    This is the "Pythonic" way to solve the problem using built-in methods.
    
    Algorithm:
    1. `bin(n)` converts the integer into a binary string. 
       For example, bin(23) returns the string "0b10111".
    2. `.count('1')` scans the string and counts how many times the character 
       '1' appears.
       
    Time Complexity: O(log N) - Converting to binary and counting takes time 
                     proportional to the number of bits.
    Space Complexity: O(log N) - To store the newly created binary string in memory.
    """
    return bin(n).count('1')

def main():
    """
    Example demonstrating both bit-counting approaches.
    23 in binary is: 10111
    Number of 1s: 4
    """
    print(f"Approach 1 (Bitwise): {numberOfOnes(23)}")    # Expected: 4
    print(f"Approach 2 (String):  {numberOfOnes2(23)}")   # Expected: 4

if __name__ == "__main__":
    main()
