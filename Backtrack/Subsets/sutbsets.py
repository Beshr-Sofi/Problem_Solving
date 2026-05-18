def subsets(nums: list[int]) -> list[list[int]]:
    """
    Generates all unique subsets (the power set) of an integer array that may contain duplicates.
    
    This function uses a backtracking algorithm (Depth-First Search) to explore the decision tree
    of either including or excluding each element. 
    
    To prevent duplicate subsets:
    1. The input array is sorted to group duplicate elements together.
    2. When exploring the "exclude element" branch, it skips over adjacent duplicate elements.

    Time Complexity: O(N * 2^N) where N is the length of nums.
    Space Complexity: O(N) for the recursion stack and the temporary list.
    """
    nums.sort()
    res = []
    def helper(index, temp):
        if index == len(nums):
            res.append(temp.copy())
            return

        temp.append(nums[index])
        helper(index+1,temp)
        temp.pop()
        while index < len(nums) - 1 and nums[index] == nums[index + 1]:
            index += 1

        helper(index+1,temp)
    helper(0,[])
    return res

def main():
    print(subsets([1,2,2]))

if __name__ == "__main__":
    main()
