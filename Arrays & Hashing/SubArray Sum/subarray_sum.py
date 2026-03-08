def subArraySum(nums, k):
    """
    Finds the total number of continuous subarrays whose sum equals to k.
    
    Time Complexity: O(N) where N is the length of nums. We iterate through the array once.
    Space Complexity: O(N) to store the prefix sums in the hash map.
    """
    res = 0
    curSum = 0
    
    # prefixSum stores the frequency of each cumulative sum we've seen so far.
    # We initialize it with {0: 1} to handle cases where a valid subarray
    # starts from the very beginning of the array (i.e., when curSum exactly equals k).
    prefixSum = {0: 1}
    
    for i in nums:
        curSum += i # Update the cumulative sum up to the current element
        
        # We want to find a previous prefix sum such that:
        # curSum - previous_prefix_sum = k
        # Which means: previous_prefix_sum = curSum - k
        diff = curSum - k
        
        # If we have seen this difference before, it means there are subarrays
        # ending at the current index that sum up to k. We add their frequency.
        res += prefixSum.get(diff, 0)
        
        # Update the frequency of the current prefix sum in our hash map
        prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        
    return res

def main():
    nums = [2, 1, -1, 2]
    k = 2
    
    # Expected output: 4
    # Valid subarrays: [2], [2, 1, -1], [1, -1, 2], [2]
    print(subArraySum(nums, k))

if __name__ == '__main__':
    main()
