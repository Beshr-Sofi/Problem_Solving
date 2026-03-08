def firstMissingPositive(nums):
    """
    Brute-force approach to find the first missing positive integer.
    
    Time Complexity: O(N^2) in the worst case where the array contains [1, 2, ..., N].
    Space Complexity: O(1) as it only uses a few variables.
    """
    start = 1
    while True:
        flag = False
        for i in nums:
            # Check if our current target 'start' exists in the array
            if i == start:
                flag = True
                break
        
        # If 'start' was not found in the entire array, it is the first missing positive
        if not flag:
            return start
        else:
            # Otherwise, increment and search for the next positive integer
            start += 1

def firstMissingPositive2(nums):
    """
    Optimal approach using Index Mapping (in-place marking).
    
    Time Complexity: O(N) as we iterate through the array a constant number of times.
    Space Complexity: O(1) since we modify the input array in-place.
    """
    # Step 1: Clean up irrelevant numbers (negatives).
    # We only care about positive integers [1, len(nums)].
    # Replace negative numbers with 0 so they don't interfere with our negative markers later.
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0

    # Step 2: Use the array indices as a hash map to mark the presence of a number.
    # If we see a number 'val' in the range [1, len(nums)], we mark index 'val - 1' as negative.
    for i in range(len(nums)):
        val = abs(nums[i])
        if val > 0 and val <= len(nums):
            # If the value at index 'val-1' is positive, negate it to mark 'val' as seen.
            if nums[val-1] > 0:
                nums[val-1] = -nums[val-1]
            # If the value is 0, we can't negate it. We replace it with a negative 
            # out-of-bounds dummy value to mark 'val' as seen.
            elif nums[val-1] == 0:
                nums[val-1] = -(len(nums) + 1)
    
    # Step 3: Find the first missing positive integer.
    # The first index 'i' that has a non-negative value means the number 'i + 1' was never seen.
    for i in range(1, len(nums) + 1):
        if nums[i - 1] >= 0:
            return i
            
    # If all indices [0, len-1] are negative, all numbers from 1 to len(nums) are present.
    # Therefore, the first missing positive is len(nums) + 1.
    return len(nums) + 1

def main():
    nums = [1, 2, 0]
    print(firstMissingPositive(nums))
    print(firstMissingPositive2(nums))

if __name__ == '__main__':
    main()
            
