def missingNumber(nums):
    """
    Finds the missing number in an array containing n distinct numbers from 0 to n.
    
    Approach 1: Mathematics (Gauss's Formula)
    -----------------------------------------
    We know exactly what the array SHOULD look like. If n = 3, the numbers should 
    be [0, 1, 2, 3]. 
    
    Algorithm:
    1. We can use Gauss's formula to calculate the EXPECTED sum of all numbers 
       from 0 to n: `expected_sum = n * (n + 1) // 2`.
    2. We can simply add up all the numbers ACTUALLY in the array: `sum(nums)`.
    3. The difference between the expected sum and the actual sum is exactly the 
       number that is missing!
       
    Example: nums = [3, 0, 1]
    - n = 3. Expected sum = 3 * 4 // 2 = 6.
    - Actual sum = 3 + 0 + 1 = 4.
    - Missing Number = 6 - 4 = 2!
    
    Time Complexity: O(N) - `sum(nums)` iterates through the array once.
    Space Complexity: O(1) - Constant extra space.
    (Note: In languages like C++ or Java, the sum could overflow for huge arrays, 
    but Python automatically handles arbitrarily large integers, making this perfectly safe).
    """
    n = len(nums)
    return (n * (n + 1)) // 2 - sum(nums)

def missingNumber2(nums):
    """
    Approach 2: Bitwise XOR Annihilation
    ------------------------------------
    This approach is highly optimized and avoids any potential integer overflow risks.
    It relies on two XOR properties:
    1. a ^ a = 0 (A number XORed with itself cancels out to 0).
    2. a ^ 0 = a (A number XORed with 0 remains unchanged).
    
    Algorithm:
    We know the array contains the numbers 0 through n, except one is missing.
    If we XOR all the indices (0 to n) and XOR all the actual values in the array, 
    every number that is present will pair up with its corresponding index and cancel 
    out to 0! The ONLY thing left will be the missing index.
    
    1. Initialize `res = n`. We do this because the loop only checks indices up 
       to n-1, so we manually include `n` from the start.
    2. Loop through the array. XOR `res` with the current index `i`, and XOR it 
       with the actual value `nums[i]`.
       
    Example: nums = [3, 0, 1]. n = 3.
    - Start: res = 3
    - i=0, val=3: res = 3 ^ (0 ^ 3) = 0
    - i=1, val=0: res = 0 ^ (1 ^ 0) = 1
    - i=2, val=1: res = 1 ^ (2 ^ 1) = 2
    - Result is 2! (All the 0s, 1s, and 3s perfectly canceled each other out).
    
    Time Complexity: O(N) - We iterate through the array exactly once.
    Space Complexity: O(1) - Constant extra space.
    """
    n = len(nums)
    res = n
    for i in range(n):
        res ^= i ^ nums[i]
    return res

def main():
    """
    Example demonstrating Missing Number algorithms.
    """
    print("Math Approach:", missingNumber([3, 0, 1]))   # Expected: 2
    print("XOR Approach: ", missingNumber2([3, 0, 1]))  # Expected: 2

if __name__ == "__main__":
    main()
