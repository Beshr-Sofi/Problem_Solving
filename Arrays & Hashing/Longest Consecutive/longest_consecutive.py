def longestConsecutive(nums):
    """
    Finds the length of the longest consecutive elements sequence by sorting the array.
    
    Time Complexity: O(N log N) where N is the length of the array (due to sorting).
    Space Complexity: O(N) or O(1) depending on the sorting algorithm implementation.
    """
    if len(nums) == 0:
        return 0
        
    # Sort the array to bring consecutive elements next to each other
    nums.sort()
    
    tmp = res = 0
    last = nums[0]
    
    for i in range(1, len(nums)):
        # Skip duplicate numbers
        if nums[i] == last:
            continue
            
        # If the difference is exactly 1, they are consecutive
        if nums[i] - last == 1:
            tmp += 1
        else:
            # If sequence breaks, update maximum length found and reset temporary counter
            res = max(tmp, res)
            tmp = 0
            
        last = nums[i]
        
    # Update max one last time in case the longest sequence is at the end
    res = max(tmp, res)
    
    # Add 1 to include the starting element of the sequence
    return res + 1

def longestConsecutive2(nums):
    """
    Finds the length of the longest consecutive elements sequence using a HashSet.
    
    Time Complexity: O(N) because each number is processed at most twice (checked in 
                     outer loop and incremented in the inner while loop).
    Space Complexity: O(N) for storing the numbers in the HashSet.
    """
    # Convert list to a set for O(1) average time complexity lookups
    setNums = set(nums)
    res = 0
    
    for num in setNums:
        # Check if 'num' is the start of a sequence.
        # It is the start ONLY if its predecessor (num - 1) is not in the set.
        if num - 1 not in setNums:
            tmp = 1
            
            # Keep looking for the next consecutive numbers in the set
            while num + 1 in setNums:
                tmp += 1
                num += 1
                
            # Update the maximum length found so far
            res = max(res, tmp)
            
    return res

def main():
    nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    print(longestConsecutive2(nums))

if __name__ == '__main__':
    main()
