def baseballGame(operations):
    """
    Calculate the total score for a baseball game based on special operations.
    
    This is LeetCode problem 682: Baseball Game. The function processes a list of
    operations that represent scores and special rules.
    
    Time Complexity: O(n) where n is the number of operations
    Space Complexity: O(n) for the stack storing scores
    
    Args:
        operations (list): List of strings representing operations
        
    Returns:
        int: The sum of all valid scores after processing all operations
    """
    # Stack to store valid scores
    stack = []
    
    for op in operations:
        # Handle each operation type
        if op == '+':
            # Sum of last two scores
            stack.append(stack[-1] + stack[-2])
        elif op == 'C':
            # Remove last score
            stack.pop()
        elif op == 'D':
            # Double last score
            stack.append(stack[-1] * 2)
        else:
            # Numeric operation - add the integer value
            stack.append(int(op))
    
    # Return the sum of all scores in the stack
    return sum(stack)

def main():
    """
    Main function to demonstrate baseball game scoring.
    
    Operations: ["5","-2","4","C","D","9","+","+"]
    
    Step-by-step execution:
    1. "5"  → stack: [5]
    2. "-2" → stack: [5, -2]
    3. "4"  → stack: [5, -2, 4]
    4. "C"  → remove 4 → stack: [5, -2]
    5. "D"  → double -2 → add -4 → stack: [5, -2, -4]
    6. "9"  → add 9 → stack: [5, -2, -4, 9]
    7. "+"  → sum of 9 and -4 = 5 → stack: [5, -2, -4, 9, 5]
    8. "+"  → sum of 5 and 9 = 14 → stack: [5, -2, -4, 9, 5, 14]
    
    Total sum: 5 + (-2) + (-4) + 9 + 5 + 14 = 27
    
    Expected output: 27
    """
    operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    result = baseballGame(operations)
    print(result)  # Should print 27

if __name__ == '__main__':
    main()
