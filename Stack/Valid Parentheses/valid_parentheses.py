def validParentheses(s):
    """
    Determine if a string containing brackets is valid.
    
    This is LeetCode problem 20: Valid Parentheses. The function checks if the input
    string has properly matched and nested brackets of three types: (), [], {}.
    
    Rules for valid parentheses:
    1. Every opening bracket must be closed by the same type of closing bracket
    2. Brackets must be closed in the correct order (proper nesting)
    3. Every closing bracket must have a corresponding opening bracket
    
    The algorithm uses a stack data structure:
    - Push opening brackets onto the stack
    - When encountering a closing bracket, check if it matches the top of the stack
    - If it matches, pop the stack; if not, the string is invalid
    
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(n) in worst case (all opening brackets)
    
    Args:
        s (str): String containing only characters '(', ')', '{', '}', '[', ']'
        
    Returns:
        bool: True if the parentheses are valid, False otherwise
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing brackets to their corresponding opening brackets
    # This allows O(1) lookup when checking matches
    closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

    # Iterate through each character in the string
    for c in s:
        # Case 1: Character is a closing bracket
        if c in closeToOpen:
            # Check if stack is not empty AND the top of stack matches the expected opening bracket
            if stack and stack[-1] == closeToOpen[c]:
                # Valid match - pop the opening bracket from stack
                stack.pop()
            else:
                # Invalid case:
                # - Stack is empty (no opening bracket for this closing bracket)
                # - Top of stack doesn't match (wrong bracket type)
                return False
        # Case 2: Character is an opening bracket
        else:
            # Push opening bracket onto stack
            stack.append(c)

    # After processing all characters, the string is valid if the stack is empty
    # If stack still has elements, there are unmatched opening brackets
    return True if not stack else False

def main():
    """
    Main function to demonstrate valid parentheses checking.
    
    Tests with s = "[(])" which is a classic invalid case:
    - '[' pushes to stack: stack = ['[']
    - '(' pushes to stack: stack = ['[', '(']
    - ']' closes: top is '(' which doesn't match ']' → returns False
    
    Expected output: False
    """
    s = "[(])"
    print(validParentheses(s))

if __name__ == '__main__':
    main()
