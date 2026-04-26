def convertToTitle(columnNumber: int) -> str:
    """
    Converts an integer column number to its corresponding Excel column title.
    
    Examples:
        1 -> "A"
        2 -> "B"
        ...
        26 -> "Z"
        27 -> "AA"
        28 -> "AB"
        ...
        701 -> "ZY"
        
    Approach: Base-26 Conversion (1-Indexed)
    ----------------------------------------
    This problem is very similar to converting a standard base-10 number into a base-26 
    number. However, the standard base-26 system uses digits from 0 to 25. The Excel 
    column system uses "digits" from A to Z, which correspond to 1 to 26 (it is 1-indexed, 
    there is no representation for 0).
    
    To fix this 1-index offset:
    1. In each iteration, we subtract 1 from `columnNumber` BEFORE doing the modulo (`% 26`) 
       and division (`// 26`) operations.
    2. `(columnNumber - 1) % 26` gives us an exact mapping from 0 to 25:
       - 0 -> 'A'
       - 1 -> 'B'
       - ...
       - 25 -> 'Z'
    3. We convert this 0-25 number into an ASCII character by adding it to `ord('A')` 
       (which is 65) and wrapping it in `chr()`.
    4. We PREPEND this character to our result string `s`, because we are extracting 
       the "least significant digit" first.
    5. We then update `columnNumber` by dividing `(columnNumber - 1)` by 26 to move to 
       the next digit position.
       
    Time Complexity: O(log base 26 of N) - The number of loop iterations is proportional 
                     to the number of "digits" in the base-26 representation.
    Space Complexity: O(1) - Only a few variables are used (ignoring the space used to 
                      store the output string).
    """
    s = ""
    while columnNumber > 0:
        # Subtract 1 to adjust for 1-indexing, then find the remainder for the current letter
        s = chr(ord('A') + (columnNumber - 1) % 26) + s
        
        # Subtract 1 to adjust for 1-indexing, then divide by 26 to move to the next "digit"
        columnNumber = (columnNumber - 1) // 26
        
    return s

# 701 corresponds to "ZY"
# How 701 is processed:
# Loop 1: (701 - 1) % 26 = 700 % 26 = 24.  ord('A') + 24 -> 'Y'. String 's' becomes "Y".
#         columnNumber = (701 - 1) // 26 = 700 // 26 = 26.
# Loop 2: (26 - 1) % 26 = 25 % 26 = 25.    ord('A') + 25 -> 'Z'. String 's' becomes "ZY".
#         columnNumber = (26 - 1) // 26 = 25 // 26 = 0.
# Loop terminates. Returns "ZY".
print(convertToTitle(701))
