"""Utilities for palindrome substring solving.

This module implements a simple, easy-to-understand algorithm to find
the longest palindromic substring in a given string using the
"expand around center" technique.

Time complexity: O(n^2) in the worst case (two nested loops of expansion).
Space complexity: O(1) extra space (not counting the returned substring).
"""

def longest_palindromic_substring(s: str) -> str:
    """Return the longest palindromic substring of `s`.

    Algorithm:
    - For each index `i` in the string consider two centers:
      1) odd-length palindromes centered at `i` (left and right both start at `i`).
      2) even-length palindromes centered between `i` and `i+1`.
    - Expand outward from each center while the characters match and
      keep track of the longest palindrome seen.

    The function returns one longest palindrome (if multiple exist, the
    first found is returned).

    Examples:
    >>> longest_palindromic_substring('babad')
    'bab'  # or 'aba'
    >>> longest_palindromic_substring('cbbd')
    'bb'
    """

    if not s:
        return ''

    start = 0  # start index of longest palindrome found
    max_len = 0  # length of longest palindrome found

    for i in range(len(s)):
        # Odd-length palindromes: center at i
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            current_len = r - l + 1
            if current_len > max_len:
                max_len = current_len
                start = l
            l -= 1
            r += 1

        # Even-length palindromes: center between i and i+1
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            current_len = r - l + 1
            if current_len > max_len:
                max_len = current_len
                start = l
            l -= 1
            r += 1

    return s[start:start + max_len]

def main():
    test_string = "babad"
    print("Longest Palindromic Substring of '{}' is: '{}'".format(test_string, longest_palindromic_substring(test_string)))

if __name__ == "__main__":
    main()
