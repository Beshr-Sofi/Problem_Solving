def minSubArrayLen(target,nums):
    """
    Finds the minimal length of a contiguous subarray whose sum is greater than or equal to the target.
    Uses a Sliding Window (Two Pointers) approach.
    Time Complexity: O(N) - each element is added and removed at most once.
    Space Complexity: O(1) - only uses a few integer integer variables.
    """
    minLength = float('inf')
    start = 0
    sum = 0
    
    # Expand the window by moving the 'i' pointer (end of window) to the right
    for i in range(len(nums)):
        sum += nums[i]
        
        # Once the window's sum is valid (>= target), try to shrink it from the left
        while sum >= target:
            # Update the minimal length found so far
            minLength = min(minLength ,i - start + 1)
            
            # Shrink the window: subtract the element at the 'start' pointer and move 'start' right
            sum -= nums[start]
            start += 1
            
    # Return 0 if no valid subarray was found, otherwise return the minimal length
    return minLength if minLength != float('inf') else 0

def main():
    target = 7
    nums = [2,3,1,2,4,3]
    print(minSubArrayLen(target,nums))

if __name__ == "__main__":
    main()
