def containsNearbyDuplicate(nums, k):
    """
    Checks if the array contains nearby duplicates.
    Specifically, it returns True if there are two identical elements 
    within a distance 'k' from each other (i.e., abs(i - j) <= k).
    
    This uses a Sliding Window approach with a HashSet.
    
    Time Complexity: O(N) where N is the length of nums.
    Space Complexity: O(min(N, k)) to store the sliding window elements.
    """
    checker = set() # Acts as our sliding window
    
    for i in range(len(nums)):
        # If the current number is already in our window, we found a nearby duplicate
        if nums[i] in checker:
            return True
            
        # If our window size is about to exceed 'k', remove the oldest element
        # (the element that is exactly 'k' steps behind the current index)
        if k and i >= k:
            checker.remove(nums[i - k])
            
        # Add the current number to the sliding window
        checker.add(nums[i])
        
    return False

def main():
    nums = [1,2,3,1]
    k = 3
    print(containsNearbyDuplicate(nums, k))

if __name__ == "__main__":
    main()
