def permutations(nums: list[int]) -> list[list[int]]:
    """
    Generates all possible permutations of an integer array.
    
    This function uses a recursive approach:
    1. Base case: If the array is empty, return a list containing an empty list.
    2. Recursive step: Recursively find all permutations of the array excluding the first element.
    3. For each permutation found, insert the first element into every possible position 
       (from index 0 up to the length of the permutation) to form new permutations.

    Time Complexity: O(N * N!) where N is the length of nums. There are N! permutations, 
    and for each, we perform array copying and insertion which takes O(N) time.
    Space Complexity: O(N * N!) to store all the generated permutations in the result list.
    The recursion stack depth is O(N).
    """
    if len(nums) == 0:
        return [[]]
    
    perm = permutations(nums[1:])
    res = []
    for i in perm:
        for index in range(len(i) + 1):
            tmp = i.copy()
            tmp.insert(index,nums[0])
            res.append(tmp)
    return res

def main():
    print(permutations([1,2,3]))

if __name__ == "__main__":
    main()
