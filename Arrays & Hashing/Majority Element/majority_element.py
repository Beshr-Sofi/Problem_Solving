def majorityElement(nums):
    """
    Finds the element that appears more than half the time in a list.
    
    This function uses a dictionary (hash map) approach to count the frequency 
    of each element. It maintains a running maximum to identify which element 
    has the highest frequency.
    
    Note: This implementation assumes a majority element exists in the list.
    
    Args:
        nums (list): A list of elements where one element appears more than ⌊n/2⌋ times
        
    Returns:
        int: The majority element with the highest frequency in the list
    """
    dic = {}  # Dictionary to store frequency counts for each element
    for i in nums:
        # Initialize count to 0 if element doesn't exist, then increment
        if not dic.get(i, 0):
            dic[i] = 0
        dic[i] += 1
    
    maxi = 0  # Track the highest frequency found so far
    res = 0   # Track the element with the highest frequency
    for i, j in dic.items():
        # Update result if current element has higher frequency than current max
        if j > maxi:
            res = i
    return res

def majorityElement2(nums):
    """
    Finds the majority element using Boyer-Moore Voting Algorithm.
    
    This is an optimized approach that runs in O(n) time with O(1) space complexity.
    The algorithm works by maintaining a candidate element and a counter. When we see 
    the candidate, we increment the counter; when we see a different element, we 
    decrement it. If the counter reaches 0, we change the candidate.
    
    This algorithm assumes a majority element (appearing > n/2 times) exists.
    
    Args:
        nums (list): A list of elements where one element appears more than ⌊n/2⌋ times
        
    Returns:
        int: The majority element that appears more than half the time
    """
    res, count = 0, 0  # Initialize candidate element and counter
    for i in nums:
        # If counter is 0, set current element as new candidate
        if count == 0:
            res = i
        # Increment if element matches candidate, decrement otherwise
        count += (1 if i == res else -1)
    return res

def main():
    """
    Main function that demonstrates both majority element finding algorithms.
    
    This function tests both implementations on the same input list and prints 
    their results for comparison. Both should return the same value (2 in this case).
    """
    # Test case: 2 appears 4 times out of 7 elements (> half)
    nums = [2, 2, 1, 1, 1, 2, 2]
    
    print("Testing majorityElement (Dictionary approach):")
    result1 = majorityElement(nums)
    print(f"Majority element: {result1}")
    
    print("\nTesting majorityElement2 (Boyer-Moore Voting Algorithm):")
    result2 = majorityElement2(nums)
    print(f"Majority element: {result2}")
    
    # Verification
    print(f"\nBoth algorithms return the same result: {result1 == result2}")

if __name__ == "__main__":
    main()
