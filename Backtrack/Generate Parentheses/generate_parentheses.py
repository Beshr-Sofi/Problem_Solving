"""
Problem:
    Given n pairs of parentheses, write a function to generate all combinations
    of well-formed (valid) parentheses.

Backtracking Rules:
    1. Add '(' if l < n: We still have available opening brackets.
    2. Add ')' if r < l: We only close brackets that have already been opened.
    3. Base case: When l == r == n, we've constructed a valid string of length 2*n.

Decision Tree Example (n = 2):
                        "" (l=0, r=0)
                             |
                           + '('
                             v
                        "(" (l=1, r=0)
                       /              \
                   + '('              + ')'
                     v                  v
               "((" (l=2, r=0)     "()" (l=1, r=1)
                     |                  |
                   + ')'              + '('
                     v                  v
               "(()" (l=2, r=1)    "()(" (l=2, r=1)
                     |                  |
                   + ')'              + ')'
                     v                  v
               "(())" [Valid]      "()()" [Valid]

Complexity:
    - Time:  O(4^n / sqrt(n)) bounded by the n-th Catalan number
    - Space: O(n) for recursion stack
"""


def generateParenthesis(n):
    res = []

    def build(curr, l, r):
        # Base case: valid combination reached
        if l == r == n:
            res.append(curr)
            return

        # Choice 1: Add '(' if we still have opening brackets left
        if l < n:
            build(curr + '(', l + 1, r)

        # Choice 2: Add ')' only if it matches an open bracket
        if r < l:
            build(curr + ')', l, r + 1)

    build('', 0, 0)
    return res


if __name__ == '__main__':
    print("n = 1:", generateParenthesis(1))
    print("n = 2:", generateParenthesis(2))
    print("n = 3:", generateParenthesis(3))
