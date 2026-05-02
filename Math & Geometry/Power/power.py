def myPow(x: float, n: int) -> float:
    """
    NOTE: This is a naive iterative attempt at fast exponentiation. 
    It attempts to square 'x' while doubling a counter 'tmp', and then linearly 
    adds the remaining powers. However, it has edge case bugs (especially with 
    negative 'n' and when n is not a power of 2) and runs in O(N) worst-case time 
    for the linear loop at the end.
    
    Please refer to myPow2 below for the optimal, correct approach!
    """
    flag = False
    if n < 0:
        flag = True
    tmp, num = 2, x
    
    while tmp < n:
        x *= x
        tmp *= 2
    tmp //= 2
    
    while tmp != n:
        x *= num
        tmp += 1
        
    if flag == True:
        x = 1 / x
    return x 

def myPow2(x, n):
    """
    Calculates x raised to the power n (x^n).
    
    Approach: Fast Exponentiation by Squaring (Recursive)
    -----------------------------------------------------
    A naive approach to calculate x^n is to multiply x by itself n times. 
    However, if n is very large, this takes O(N) time and will cause a Time 
    Limit Exceeded error.
    
    We can optimize this to O(log N) time using the math property of exponents:
    1. If 'n' is EVEN: x^n = x^(n/2) * x^(n/2)
       Example: 2^10 = 2^5 * 2^5. 
       Instead of multiplying 10 times, we only need to find 2^5 ONCE and square it!
    
    2. If 'n' is ODD: x^n = x * x^(n//2) * x^(n//2)
       Example: 2^5 = 2 * 2^2 * 2^2.
       
    Algorithm:
    1. Base Cases:
       - If n == 0, return 1 (anything to the power of 0 is 1).
       - If x == 0, return 0 (0 to the power of anything is 0).
    2. Recursive Step:
       - Calculate the result for half the power: `res = helper(x, n // 2)`.
       - Square the result: `res *= res`.
       - If `n` was odd, we missed one `x` due to integer division (e.g., 5//2 is 2). 
         So we multiply by `x` one more time.
    3. Negative Powers:
       - If the original `n` was negative, x^-n is mathematically equivalent to 1 / x^n.
       - We just calculate `helper(x, abs(n))` and return 1 divided by the result.
       
    Time Complexity: O(log N) - The power 'n' is halved at every recursive step.
    Space Complexity: O(log N) - Due to the call stack during recursion.
    """
    def helper(x, n):
        # Base cases
        if n == 0: return 1
        if x == 0: return 0

        # Recursively find x^(n/2)
        res = helper(x, n // 2)
        
        # Square the result (which handles the even case perfectly)
        res *= res
        
        # If n is odd, multiply by an extra x
        return x * res if n % 2 == 1 else res
    
    # Handle negative exponents at the very top level
    return helper(x, n) if n >= 0 else 1 / helper(x, abs(n))

def main():
    """
    Example demonstrating Fast Exponentiation.
    
    Calculate: 2.0 ^ 10
    
    Call Stack Trace:
    - helper(2, 10) -> calls helper(2, 5) -> returns 32, squared = 1024. (10 is even)
      - helper(2, 5)  -> calls helper(2, 2) -> returns 4, squared=16 * 2 = 32. (5 is odd)
        - helper(2, 2)  -> calls helper(2, 1) -> returns 2, squared = 4. (2 is even)
          - helper(2, 1)  -> calls helper(2, 0) -> returns 1, squared=1 * 2 = 2. (1 is odd)
            - helper(2, 0)  -> Base case! Returns 1.
            
    Expected Output: 1024.0
    """
    x = 2.00000
    n = 10
    print(myPow2(x, n))  

if __name__ == "__main__":
    main()
