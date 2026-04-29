def isHappy(n):
    """
    Determines if a number 'n' is a "Happy Number".
    
    A Happy Number is defined by the following process:
    1. Starting with any positive integer, replace the number by the sum of the 
       squares of its digits.
    2. Repeat the process until the number equals 1 (where it will stay), or it 
       loops endlessly in a cycle which does not include 1.
    3. Those numbers for which this process ends in 1 are happy.
    
    Approach: Hash Set to Detect Cycles
    -----------------------------------
    We can continually calculate the sum of the squared digits. There are only 
    two possible outcomes:
    A. The sum eventually reaches 1. (Happy!)
    B. The sum gets stuck in an infinite loop/cycle of numbers. (Not Happy)
    
    To detect the infinite loop (Outcome B), we use a `set()` to keep track of 
    every sum we have seen so far. If we ever generate a sum that is ALREADY 
    in our set, we know we are looping endlessly and can safely return False.
    
    Algorithm:
    1. Define a helper function `sumSquare(n)` to calculate the sum of the squares 
       of the digits using modulo (`% 10`) and integer division (`// 10`).
    2. Initialize an empty set `seen`.
    3. Loop infinitely:
       - Calculate the new sum `tmp`.
       - If `tmp == 1`, return True.
       - If `tmp` is in `seen`, we found a cycle! Return False.
       - Otherwise, add `tmp` to `seen` and update `n = tmp` for the next loop.
       
    Time Complexity: O(log n) - Finding the next number costs log(n) operations.
    Space Complexity: O(log n) - To store the numbers in our HashSet.
    """
    
    def sumSquare(n):
        # Extracts each digit from right to left, squares it, and adds to total
        total_sum = 0
        while n != 0:
            total_sum += (n % 10) ** 2
            n //= 10
        return total_sum
        
    seen = set()
    
    while True:
        tmp = sumSquare(n)
        
        # Outcome A: We reached 1
        if tmp == 1:
            return True
            
        # Outcome B: We reached a number we've already seen (Infinite Loop)
        if tmp in seen:
            return False
            
        # Record the number and continue
        seen.add(tmp)
        n = tmp
    
def main():
    """
    Example demonstrating a Happy Number.
    
    Let's trace n = 19:
    1^2 + 9^2 = 1 + 81 = 82
    8^2 + 2^2 = 64 + 4 = 68
    6^2 + 8^2 = 36 + 64 = 100
    1^2 + 0^2 + 0^2 = 1 + 0 + 0 = 1 (Happy!)
    
    Expected output: True
    """
    print(isHappy(19))

if __name__ == "__main__":
    main()
