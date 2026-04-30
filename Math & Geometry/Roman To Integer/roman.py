def romanToInt(s: str) -> int:
    """
    Converts a Roman numeral string to an integer.
    
    Approach: Add Everything, Compensate for Subtractions
    -----------------------------------------------------
    Normally, Roman numerals are written largest to smallest from left to right. 
    However, there are six instances where subtraction is used:
    - I can be placed before V (5) and X (10) to make 4 and 9. 
    - X can be placed before L (50) and C (100) to make 40 and 90. 
    - C can be placed before D (500) and M (1000) to make 400 and 900.
    
    This algorithm takes a clever "compensatory" approach:
    1. It iterates through every character in the string and unconditionally ADDS 
       its raw value to the total sum.
    2. To handle the subtraction rules, it looks backwards. If it sees a subtractive 
       pair (like "IV"), it corrects the sum by subtracting.
       
    Why subtract 2, 20, or 200?
    Let's take "IV" (4) as an example. 
    - In loop 1, we see 'I' and add 1. Sum = 1.
    - In loop 2, we see 'V' and add 5. Sum = 6. 
    - Since we wanted 4, our sum is over by exactly 2! 
      (Because we ADDED the 'I' instead of subtracting it).
    - So, we simply subtract 2 to correct the sum back to 4.
    
    Time Complexity: O(N) - We iterate through the string exactly once.
    Space Complexity: O(1) - We only use a single integer variable to store the sum.
    """
    total_sum = 0
    
    for i in range(len(s)):
        # Check for the subtractive compensation rules 
        # (Make sure we are not on the first character, i.e., i > 0)
        if i:
            # If current is V/X and previous was I, we over-added by 2
            if s[i] in 'VX' and s[i-1] == 'I':
                total_sum -= 2
            # If current is L/C and previous was X, we over-added by 20
            elif s[i] in 'LC' and s[i-1] == 'X':
                total_sum -= 20
            # If current is M/D and previous was C, we over-added by 200
            elif s[i] in 'MD' and s[i-1] == 'C':
                total_sum -= 200
                
        # Always add the raw value of the current Roman numeral
        if s[i] == 'I':
            total_sum += 1
        elif s[i] == 'V':
            total_sum += 5
        elif s[i] == 'X':
            total_sum += 10
        elif s[i] == 'L':
            total_sum += 50
        elif s[i] == 'C':
            total_sum += 100
        elif s[i] == 'D':
            total_sum += 500
        elif s[i] == 'M':
            total_sum += 1000
            
    return total_sum

def main():
    """
    Examples demonstrating Roman to Integer conversion.
    
    'III' = 3
    'LVIII' = L(50) + V(5) + III(3) = 58
    'MCMXCIV' = M(1000) + CM(900) + XC(90) + IV(4) = 1994
    """
    print(romanToInt('III'))       # Expected: 3
    print(romanToInt('LVIII'))     # Expected: 58
    print(romanToInt('MCMXCIV'))   # Expected: 1994

if __name__ == '__main__':
    main()
