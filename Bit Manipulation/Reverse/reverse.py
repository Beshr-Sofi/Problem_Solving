import math

def reverse(x):
    """
    Reverses the digits of a 32-bit signed integer.
    
    Approach: Pop and Push Digits & Handle Overflow
    -----------------------------------------------
    To reverse the integer mathematically (without converting to a string):
    1. We "pop" the last digit off the original number `x` using modulo (`% 10`).
    2. We "push" that digit onto the back of our result `res` by multiplying `res` 
       by 10 and adding the digit.
       
    The Python Negative Number Catch:
    In languages like C++ or Java, `-123 % 10` is `-3`, and `-123 / 10` is `-12`.
    In Python, `-123 % 10` is `7`, and `-123 // 10` is `-13`! (Python floors down).
    To force Python to behave like C++ so the math works for negative numbers, 
    the code cleverly uses `math.fmod(x, 10)` and `int(x / 10)` which truncates 
    towards zero instead of flooring.
    
    The 32-bit Overflow Catch:
    The problem assumes we are in an environment that CANNOT store 64-bit integers. 
    This means we can't just calculate a massive reversed number and check if it's 
    too big at the end. We must check if it's ABOUT to overflow *before* we multiply 
    `res` by 10.
    - Max 32-bit int:  2147483647
    - Min 32-bit int: -2147483648
    
    Before we do `res = res * 10 + digit`:
    - If `res` is strictly greater than `Max / 10` (214748364), multiplying by 10 
      will definitely overflow.
    - If `res` is exactly equal to `Max / 10`, it will overflow ONLY if the incoming 
      `digit` is greater than 7 (since the last digit of Max is 7).
    - We apply the exact same logic for the Min boundary (checking against -8).
    
    Time Complexity: O(log(x)) - There are roughly log10(x) digits in x.
    Space Complexity: O(1)
    """
    Min = -2147483648
    Max = 2147483647
    res = 0
    
    while x:
        # Pop the last digit. math.fmod ensures negative numbers yield negative digits
        # (e.g., math.fmod(-123, 10) -> -3.0)
        digit = int(math.fmod(x, 10))
        
        # Chop off the last digit. int() ensures truncation towards zero
        # (e.g., int(-123 / 10) -> -12)
        x = int(x / 10)
        
        # Check for positive overflow before pushing
        # Note: Max // 10 in Python is 214748364, Max % 10 is 7
        if res > Max // 10 or (res == Max // 10 and digit >= Max % 10):
            return 0
            
        # Check for negative overflow before pushing
        # Note: int(Min / 10) gives the proper C++ style truncation: -214748364
        # math.fmod(Min, 10) gives -8
        if res < int(Min / 10) or (res == int(Min / 10) and digit <= int(math.fmod(Min, 10))):
            return 0
            
        # Push the digit onto the result
        res = (res * 10) + digit

    return res

def main():
    """
    Example demonstrating Reversing an Integer.
    """
    print("Reverse of 123 is:", reverse(123))       # Expected: 321
    print("Reverse of -123 is:", reverse(-123))     # Expected: -321
    print("Reverse of 120 is:", reverse(120))       # Expected: 21
    
    # Example of an overflow returning 0
    print("Reverse of 1534236469 is:", reverse(1534236469)) # Expected: 0

if __name__ == "__main__":
    main()
