def gcdOfString(str1, str2):
    """
    Finds the Greatest Common Divisor (GCD) of two strings.
    
    A string `X` divides `Y` if and only if `Y` can be formed by concatenating `X` 
    to itself some number of times. The GCD of two strings is the longest string `X` 
    that divides both `str1` and `str2`.
    
    Approach: Brute-Force from Largest to Smallest
    ----------------------------------------------
    Since we want the *Greatest* Common Divisor, the longest possible candidate 
    string would have a length equal to the shorter of the two strings.
    
    Algorithm:
    1. Iterate backwards: We check candidate lengths from `min(len(str1), len(str2))` 
       down to 1. By checking the largest sizes first, the first valid divisor we 
       find is guaranteed to be the *greatest*.
    2. Length Check: For a candidate length `maxi`, it must perfectly divide the 
       lengths of BOTH `str1` and `str2`. If `len1 % maxi != 0` or `len2 % maxi != 0`, 
       it cannot be a divisor.
    3. String Construction Check: If the lengths are divisible, we take the prefix 
       of `str1` of length `maxi`. We then simulate building both strings:
       - Multiply the prefix by `len1 // maxi`. Does it equal `str1`?
       - Multiply the prefix by `len2 // maxi`. Does it equal `str2`?
       If both are true, we have found our GCD string!
       
    Time Complexity: O(min(len1, len2) * (len1 + len2)) 
                     - The loop runs at most min(len1, len2) times.
                     - String multiplication/comparison inside the loop takes O(len1 + len2).
    Space Complexity: O(len1 + len2) - For creating the temporary multiplied strings 
                      during comparison.
    """
    len1, len2 = len(str1), len(str2)
    
    def isDivisor(maxi):
        # 1. Check if the length perfectly divides both string lengths
        if len1 % maxi or len2 % maxi:
            return False
            
        # 2. Calculate how many times the prefix needs to be repeated
        l1, l2 = len1 // maxi, len2 // maxi
        
        # 3. Check if repeating the prefix perfectly reconstructs both strings
        return str1[:maxi] * l1 == str1 and str1[:maxi] * l2 == str2
   
    # Iterate from the largest possible length down to 1
    for i in range(min(len1, len2), 0, -1):
        if isDivisor(i):
            return str1[:i] # First valid divisor is the greatest
            
    return '' # No common divisor found

def main():
    """
    Example demonstrating GCD of strings.
    
    str1 = 'ABABAB'
    str2 = 'AB'
    
    Candidate lengths:
    - Length 2 ('AB'):
      - Divides len1 (6 % 2 == 0). 'AB' * 3 == 'ABABAB' (Match!)
      - Divides len2 (2 % 2 == 0). 'AB' * 1 == 'AB' (Match!)
      
    Since we check from largest to smallest, 'AB' is returned.
    """
    str1 = 'ABABAB'
    str2 = 'AB'
    print(gcdOfString(str1, str2))

if __name__ == "__main__":
    main()
