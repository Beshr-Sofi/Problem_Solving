def permutationsUnique(nums:list[int])->list[list[int]]:
    """
    Generates all unique permutations of a collection of numbers that might contain duplicates.
    
    Approach: Backtracking with a Hash Map (Frequency Counter)
    - To avoid generating duplicate permutations, we count the frequency of each number.
    - In each recursive step, we iterate through the unique numbers in our counter.
    - If a number's count is > 0, we can add it to the current permutation and decrement its count.
    - We recursively call our helper function to build the rest of the permutation.
    - After returning from the recursive call (backtracking), we undo our choice by incrementing
      the count and popping the number from our current permutation.
      
    Time Complexity: O(N * N!) in the worst case (all elements unique) since there are N!
    permutations and copying the permutation to the result list takes O(N) time.
    Space Complexity: O(N) auxiliary space for the recursion stack, the frequency hash map,
    and the temporary permutation list.
    """
    res = []
    perm = []
    
    # Create a frequency map of the elements
    count = {n:0 for n in nums}
    for i in nums:
        count[i] += 1
    
    def helper():
        # Base case: if the current permutation length matches nums, we found a valid permutation
        if len(nums) == len(perm):
            res.append(perm.copy())
            return
        
        # Iterate through the unique numbers in the frequency map
        for n in count:
            if count[n] > 0:
                # Decision: choose number 'n'
                perm.append(n)
                count[n] -= 1

                # Explore down this path
                helper()
                
                # Undo the decision (backtrack)
                count[n] += 1
                perm.pop()
        
    helper()
    return res

def main():
    print(permutationsUnique([1,1,2]))

if __name__ == "__main__":
    main()
