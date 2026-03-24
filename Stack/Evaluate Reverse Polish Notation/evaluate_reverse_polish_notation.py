def evalRPN(tokens):
    """
    Evaluates an arithmetic expression in Reverse Polish Notation (RPN).
    Uses a stack to process tokens left to right.
    """
    stack = []
    for i in tokens:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            # The order matters for subtraction. 
            # -stack.pop() + stack.pop() effectively evaluates: (second popped) - (first popped)
            stack.append(-stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            # int() casts the float result to truncate towards zero, which is standard for RPN.
            # (Standard // integer division in python rounds down to negative infinity)
            first = stack.pop()
            second = stack.pop()
            stack.append(int(second / first))
        else:
            stack.append(int(i))
    return stack.pop()

def main():
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))

if __name__ == "__main__":
    main()

