def countSubstrings(s):
    """
    Find the number of palindromic substrings in a string.
    
    Approach: Brute-Force
    - Generates all possible substrings of length `i` starting from index `tmp`.
    - For each substring, it checks if it is a palindrome by comparing characters
      from the outside in.
      
    Time Complexity: O(N^3) where N is the length of `s`. Generating all substrings 
      takes O(N^2), and checking if each is a palindrome takes O(N) time.
    Space Complexity: O(N) due to the string slicing creating new string objects.
    """
    def check(s):
        for i in range(len(s)//2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    res = 0
    for i in range(1,len(s) + 1):
        tmp = 0
        while tmp <= len(s) - i:
            res += check(s[tmp:tmp+i])
            tmp += 1

    return res

def countSubstrings2(s):
    """
    Find the number of palindromic substrings in a string.
    
    Approach: Expand Around Center
    - Instead of checking all substrings, we treat each character (and each pair 
      of adjacent characters) as the potential center of a palindrome.
    - For each center, we expand outwards `l -= 1` and `r += 1` as long as the 
      characters match.
    - We do this twice per character: once for odd-length palindromes (single 
      character center) and once for even-length palindromes (two character center).
      
    Time Complexity: O(N^2) where N is the length of `s`. There are 2N-1 centers, 
      and expanding from each takes at most O(N) time.
    Space Complexity: O(1) as we only use pointers `l` and `r` without creating 
      new strings.
    """
    res = 0

    for i in range(len(s)):
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
    return res

def main():
    s = 'aaa'
    print(countSubstrings2(s))

if __name__ == '__main__':
    main()
