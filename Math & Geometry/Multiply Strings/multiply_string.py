def multiply(num1, num2):
    """
    Multiplies two non-negative integers represented as strings and returns the 
    result as a string.
    
    Approach: Custom String-to-Integer and Integer-to-String Conversion
    -------------------------------------------------------------------
    Instead of using Python's built-in `int()` and `str()` functions, this code 
    manually builds the integers from the characters using ASCII math, multiplies 
    them, and then manually builds the final string from the integer result.
    
    Algorithm:
    1. Base Case: If either string is '0', the product is immediately '0'.
    2. String to Integer (Manual):
       - We iterate through every character in the string.
       - `ord(char) - ord('0')` is a clever trick to get the actual integer value 
         of a digit character. For example, the ASCII value of '5' is 53, and '0' 
         is 48. 53 - 48 = 5.
       - We multiply that digit by its place value (e.g., 100, 10, or 1).
         For a 3-digit number, the first digit is multiplied by 10^(3-1-0) = 10^2 = 100.
       - We accumulate this in `val1` and `val2`.
    3. Multiplication: We multiply the two completely constructed integers.
    4. Integer to String (Manual): 
       - The `convertToString` function does the exact opposite. It takes the integer, 
         uses modulo (`% 10`) to extract the last digit, converts it back to a character 
         using `chr(ord('0') + remainder)`, and prepends it to a result string. 
         It then divides by 10 to move to the next digit.
         
    Note: A more strict version of this problem usually asks you to simulate grade-school 
    multiplication (array-based multiplication) to avoid integer overflow in languages 
    other than Python (since Python handles arbitrarily large integers automatically).
    """
    if num1 == '0' or num2 == '0':
        return '0'
        
    n, m = len(num1), len(num2)
    
    # Initialize the values. (The code initially sets these to a power of 10, 
    # but immediately subtracts it on the first loop iteration to correct it).
    val1, val2 = 10 ** (n - 1), 10 ** (m - 1)
    
    # Convert num1 to an integer
    for i in range(len(num1)):
        # Calculate the integer value of the current character
        digit_val = ord(num1[i]) - ord('0')
        # Calculate its place value (e.g., hundreds, tens, ones)
        place_val = 10 ** (len(num1) - 1 - i)
        
        if i == 0:
            val1 += (digit_val * place_val) - val1
        else:
            val1 += (digit_val * place_val)
            
    # Convert num2 to an integer
    for i in range(len(num2)):
        digit_val = ord(num2[i]) - ord('0')
        place_val = 10 ** (len(num2) - 1 - i)
        
        if i == 0:
            val2 += (digit_val * place_val) - val2
        else:
            val2 += (digit_val * place_val)
            
    # Multiply and convert the result back to a string
    return convertToString(val1 * val2)

def convertToString(n):
    """
    Helper function to manually convert an integer to a string representation 
    using ASCII character mapping.
    """
    res = ''
    while n > 0:
        # Get the rightmost digit
        remainder = n % 10
        # Convert it back to its ASCII character representation and prepend it
        res = chr(ord('0') + remainder) + res
        # Remove the rightmost digit
        n = n // 10
    return res

def main():
    """
    Example demonstrating string multiplication.
    
    '40' -> converted to int 40
    '58' -> converted to int 58
    40 * 58 = 2320
    2320 -> converted back to string '2320'
    """
    num1 = '40'
    num2 = '58'
    print(multiply(num1, num2)) # Expected: 2320
    
if __name__ == "__main__":
    main()
