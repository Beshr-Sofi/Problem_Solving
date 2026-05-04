def singleNumber(nums):
    """
    Finds the single number in an array where every other element appears exactly twice.
    
    Approach: Bitwise XOR
    ---------------------
    This is an elegant and highly optimized solution using the bitwise XOR operator (^).
    
    XOR has three incredibly useful properties for this specific problem:
    1. A number XORed with itself evaluates to 0 (e.g., 5 ^ 5 = 0).
       - This means that any number that appears TWICE in the array will perfectly 
         cancel itself out to 0!
    2. A number XORed with 0 remains completely unchanged (e.g., 5 ^ 0 = 5).
    3. XOR is commutative and associative. This means the order in which we XOR 
       the numbers doesn't matter at all (e.g., 2 ^ 1 ^ 2 is exactly the same 
       as 2 ^ 2 ^ 1).
       
    Algorithm:
    By starting a running total (`res`) and simply XORing every single number in 
    the array together, all the duplicate pairs will annihilate each other and 
    turn into 0s. The only thing left standing at the very end of the loop will 
    be the single number that didn't have a pair to cancel it out!
    
    Example Trace: [2, 1, 2]
    - Start: res = 2
    - Loop 1 (val = 1): res = 2 ^ 1
    - Loop 2 (val = 2): res = 2 ^ 1 ^ 2 
    - The two 2s cancel out (2 ^ 2 = 0), leaving res = 0 ^ 1 = 1.
    
    Time Complexity: O(N) - We iterate through the array exactly once.
    Space Complexity: O(1) - We only use a single variable to keep the running total,
                      meaning this takes constant extra memory!
    """
    res = nums[0]
    
    # Loop through the rest of the array and apply XOR to the running total
    for i in range(1, len(nums)):
        res ^= nums[i]
        
    return res

def main():
    """
    Example demonstrating the Single Number algorithm.
    """
    # The two 2s will cancel out, leaving just the 1.
    print(singleNumber([2, 2, 1]))  # Expected output: 1

if __name__ == "__main__":
    main()
