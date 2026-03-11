def splitArray(nums, k):
    """
    Solves the 'Split Array Largest Sum' problem using Binary Search.
    
    Given an array of non-negative integers (nums) and an integer k, the goal is to 
    split the array into at most k contiguous sub-arrays such that the largest sum 
    among these sub-arrays is minimized.
    
    Time Complexity: O(N * log(S)) where N is len(nums) and S is sum(nums) - max(nums)
    Space Complexity: O(1)
    """
    # l: lower bound (max single element, if we split into N subarrays)
    # r: upper bound (sum of all elements, if we don't split at all)
    l, r = max(nums), sum(nums)
    
    # Binary search for the minimized maximum sum
    while l <= r:
        mid = (l + r) // 2 # mid is our current guess for the minimized maximum sum
        count = tmp = 0    # count: number of splits, tmp: current subarray sum
        
        for i in nums:
            tmp += i
            # If current subarray sum exceeds our guessed max capacity (mid)
            if tmp > mid:
                count += 1 # We must split here
                tmp = i    # Start a new subarray with the current element
                
        # If we needed more than k subarrays, our guess (mid) was too small
        if count + 1 > k:
            l = mid + 1
        # If we split into k or fewer subarrays, our guess works, 
        # but let's try to find a smaller maximum sum
        else:
            r = mid - 1
            
    # l stops precisely at the smallest possible maximum sum
    return l

def main():
    nums = [1,0,2,3,5]
    k = 4
    print(splitArray(nums, k))

if __name__ == "__main__":
    main()
