def maxProduct(nums):
    """
    Find the contiguous subarray within an array (containing at least one number)
    which has the largest product.
    
    Approach: Dynamic Programming
    - A negative number can turn the largest positive product into the smallest negative product.
    - Conversely, a negative number can turn the smallest negative product into the largest positive product.
    - Therefore, at each step, we maintain BOTH the maximum and minimum product ending at the current element.
    - The `dp` tuple stores `(current_max, current_min)`.
    - If we encounter a 0, we effectively "break" the contiguous subarray and reset our dp values to 1.
    
    Time Complexity: O(N) where N is the length of `nums` (single pass through the array).
    Space Complexity: O(1) as we only use a tuple and a few variables to track state.
    """
    res = max(nums)
    dp = (1,1)
    
    for num in nums:
        if num == 0:
            # A zero breaks the contiguous product. Reset the current max/min to 1.
            # We don't need to worry about updating `res` with 0 here because `res` 
            # was initialized to `max(nums)`, which inherently accounts for 0.
            dp = (1,1)
        else:
            # Calculate potential new max by multiplying with the previous max
            temp = dp[0] * num
            
            # The new max is either:
            # 1. Previous max * num (if num is positive)
            # 2. Previous min * num (if num is negative and previous min was negative)
            # 3. Just `num` itself (starting a new subarray from this element)
            dp = (
                max(temp, dp[1] * num, num),
                min(temp, dp[1] * num, num)
            )
            
            # Update the global maximum
            res = max(res, dp[0])
            
    return res

def main():
    nums = [2,3,-2,4]
    print(maxProduct(nums))

if __name__ == "__main__":
    main()

