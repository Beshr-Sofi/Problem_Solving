def plusOne(digits: list[int]) -> list[int]:
    """
    Increments a large integer represented as an array of digits by one.
    
    Approach: Grade-School Addition (Right-to-Left)
    -----------------------------------------------
    When we add 1 to a number by hand, we start at the rightmost digit (the ones place).
    If the digit is less than 9, we simply add 1 and we are done. 
    However, if the digit is a 9, adding 1 gives us 10. We must write down a 0 and 
    "carry over" the 1 to the next digit to the left.
    
    Algorithm:
    1. Start a pointer (`index`) at the very last digit in the array.
    2. While we are pointing at a 9:
       - The 9 turns into a 0 (because 9 + 1 = 10).
       - We move our pointer one step to the left (`index -= 1`) to carry the 1 over.
    3. The loop stops for one of two reasons:
       - Case A: We found a digit that wasn't a 9. (e.g., [1, 2, 9] -> pointer stops at 2).
                 We just add 1 to this digit and we're finished!
       - Case B: Every single digit was a 9. (e.g., [9, 9, 9] -> [0, 0, 0]). 
                 Our pointer ran off the left edge of the array (`index < 0`).
                 To fix this, we insert a brand new `1` at the very front of the array,
                 making it [1, 0, 0, 0].
                 
    Time Complexity: O(N) - In the worst case (all 9s), we loop through the entire array.
    Space Complexity: O(1) - We modify the array in-place. (Inserting at the front takes 
                      O(N) time under the hood, but doesn't strictly scale up extra memory).
    """
    index = len(digits) - 1
    
    # Keep changing 9s to 0s and moving left
    while index >= 0 and digits[index] == 9:
        digits[index] = 0
        index -= 1
        
    # Case B: We ran off the edge, meaning the number was all 9s
    if index < 0:
        digits.insert(0, 1)
        
    # Case A: We stopped on a normal digit, just add 1 to it
    else:
        digits[index] += 1
        
    return digits

def main():
    """
    Examples demonstrating the Plus One algorithm.
    """
    # Simple addition (No carry)
    print(plusOne([1, 2, 3]))       # Expected: [1, 2, 4]
    
    # Simple addition (No carry)
    print(plusOne([4, 3, 2, 1]))    # Expected: [4, 3, 2, 2]
    
    # Worst case addition (All 9s, requires inserting a new digit)
    print(plusOne([9, 9, 9]))       # Expected: [1, 0, 0, 0]

if __name__ == '__main__':
    main()
