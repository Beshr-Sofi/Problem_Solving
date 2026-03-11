class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time O(1).
    
    This is achieved by maintaining two separate stacks:
    1. s1: The main stack that stores all the pushed elements.
    2. mini: An auxiliary stack that keeps track of the "minimum so far". 
             The top of this stack always represents the minimum value present in s1.
    
    Time Complexity: O(1) for all operations (push, pop, top, getMin).
    Space Complexity: O(N) where N is the number of elements in the stack.
    """

    def __init__(self):
        self.s1 = []   # Main stack
        self.mini = [] # Auxiliary stack for minimums

    def push(self, val: int) -> None:
        """Pushes the element val onto the stack."""
        self.s1.append(val)
        
        # If the minimum stack is empty, or the new value is smaller than or equal 
        # to the current minimum, we append it to the mini stack.
        # Otherwise, we duplicate the current minimum value on top of the mini stack
        # so that the sizes of both stacks remain synchronized.
        if not self.mini or self.mini[-1] > val:
            self.mini.append(val)
        else:
            self.mini.append(self.mini[-1])

    def pop(self) -> None:
        """Removes the element on the top of the stack."""
        # Pop from both stacks to keep them synchronized
        self.s1.pop()
        self.mini.pop()

    def top(self) -> int:
        """Gets the top element of the stack."""
        return self.s1[-1]

    def getMin(self) -> int:
        """Retrieves the minimum element in the stack in O(1) time."""
        return self.mini[-1]

def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) # return -3
    minStack.pop()
    print(minStack.top())    # return 0
    print(minStack.getMin()) # return -2

if __name__ == "__main__":
    main()
