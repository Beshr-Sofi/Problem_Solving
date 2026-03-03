def rotate(nums, k):
    """
    Rotates the array `nums` to the right by `k` steps in-place.
    
    This is achieved using the array reversal algorithm in 3 steps:
    1. Reverse the entire array.
    2. Reverse the first `k % len(nums)` elements.
    3. Reverse the remaining elements.
    
    Time Complexity: O(N) where N is the length of the array.
    Space Complexity: O(1) as the operations are performed in-place.
    """
    
    # Step 1: Reverse the entire array
    l , r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1
    
    # Step 2: Reverse the first k % len(nums) elements
    l , r = 0, k % len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1
    
    # Step 3: Reverse the remaining elements backwards to their original internal order
    l , r = k % len(nums), len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1



def main():
    nums = [1,2,3,4,5,6,7]
    k = 3
    rotate(nums, k)
    print(nums)

if __name__ == '__main__':
    main()
