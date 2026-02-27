"""
Problem: Product of Array Except Self
-------------------------------------
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to 
the product of all the elements of `nums` except `nums[i]`.
The algorithm must run in O(n) time and without using the division operation.

Explanation:
------------
To achieve O(n) time without division, we can use the concept of prefix and postfix products.
1. Prefix Pass: We first calculate the prefix product for each element. The result array 
   (called `prefix`) will initially store the product of all elements to the left of the current index.
2. Postfix Pass: We then iterate backward through the array, maintaining a running `postfix` 
   product of all elements to the right. We multiply this `postfix` product with our 
   previously calculated `prefix` product at each index to get the final result.

Complexity Analysis:
--------------------
- Time Complexity: O(n), where `n` is the length of the input array `nums`. We make two separate 
  linear passes over the array (one forward for prefix, one backward for postfix), each 
  taking O(n) time. The overall time complexity is O(n).
- Space Complexity: O(1) auxiliary space. The output array used to return the result does not count 
  towards extra space complexity for this problem. The `postfix` variable only takes constant O(1) space.
"""
def productArrayExceptSelf(nums):
    # Initialize the prefix array with 1s. This output array will first 
    # store the product of all elements to the left of the current index.
    prefix = [1] * len(nums)
    
    # First Pass (Left to Right): Calculate prefix products.
    # For index i+1, the prefix product is the current element nums[i] 
    # multiplied by the previous prefix product prefix[i].
    for i in range(len(nums) - 1):
        prefix[i+1] = nums[i] * prefix[i]
        
    # Initialize postfix product. It will keep a running product 
    # of all elements to the right of the current index.
    postfix = 1
    
    # Second Pass (Right to Left): Calculate final result.
    for i in range(len(nums)-1, -1, -1):
        # The result at index i is the product of all elements to the left (prefix[i])
        # multiplied by the product of all elements to the right (postfix).
        prefix[i] = postfix * prefix[i]
        
        # Update the postfix product to include the current element nums[i].
        # This will be used for the element at index i-1 in the next iteration.
        postfix = nums[i] * postfix
        
    # Return the modified prefix array which now holds our final answer.
    return prefix

def main():
    nums = [1,2,3,4]
    print(productArrayExceptSelf(nums))

if __name__ == '__main__':
    main()
