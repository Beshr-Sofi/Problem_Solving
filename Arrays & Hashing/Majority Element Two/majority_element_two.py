from collections import defaultdict

def majorityElementTwo(nums):
    """
    Finds all elements that appear more than ⌊n / 3⌋ times using a Hash Map.
    Time Complexity: O(N) - single pass to count frequencies.
    Space Complexity: O(N) - stores the frequencies of all unique elements in the dictionary.
    """
    temp = {}
    # Count the frequency of each element
    for i in nums:
        temp[i] = temp.get(i,0) + 1
        
    res = []
    n = len(nums) // 3
    # Filter elements that meet the ⌊n / 3⌋ threshold
    for i , j in temp.items():
        if j > n :
            res.append(i)
    return res


def majorityElementTwo2(nums):
    """
    Finds all elements that appear more than ⌊n / 3⌋ times using the Boyer-Moore Majority Vote algorithm.
    Time Complexity: O(N) - single pass to find candidates, and another pass via count() to verify.
    Space Complexity: O(1) - the 'temp' dictionary tracks at most 3 elements at any given time.
    """
    temp = defaultdict(int)
    
    # Step 1: Find potential candidates
    for i in nums:
        temp[i] += 1
        
        # At most 2 elements can appear more than ⌊n / 3⌋ times.
        if len(temp) <= 2:
            continue
            
        # If we have 3 distinct elements, we "cancel" them out by decrementing their counts
        new = defaultdict(int)
        for i , c in temp.items():
            if c > 1:
                new[i] = c - 1
        temp = new

    # Step 2: Verify the candidates
    res = []
    n = len(nums) // 3
    # Verify if the remaining candidates actually appear more than ⌊n / 3⌋ times in the original array
    for i , j in temp.items():
        if nums.count(i) > n :
            res.append(i)
    return res

def main():
    nums = [3,2,3]
    print(majorityElementTwo(nums))
    print(majorityElementTwo2(nums))

if __name__ == '__main__':
    main()
