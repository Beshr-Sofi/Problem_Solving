from collections import deque

class MyStack:
    """
    Implements a Last-In-First-Out (LIFO) stack using a single First-In-First-Out (FIFO) queue.
    By using Python's collections.deque as the queue, we can simulate stack behavior.
    """
    def __init__(self):
        # Initialize a single queue
        self.q1 = deque()

    def push(self, x: int) -> None:
        """
        Pushes element x onto the stack.
        Time Complexity: O(1) - Just adding an element to the back of the queue.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on the top of the stack and returns it.
        Time Complexity: O(N) where N is the number of elements in the stack.
        
        How it works:
        Since a queue only allows us to remove from the front (popleft), but a stack requires
        removing from the back (the most recently added element), we will take all the 
        items in front of the newest item, remove them, and re-add them to the back.
        After doing this for (N - 1) elements, the newest element will be at the front, 
        allow us to safely remove and return it.
        """
        # Dequeue and re-enqueue all elements except the last one
        for i in range(len(self.q1) - 1):
            self.push(self.q1.popleft())
            
        # The last element added is now at the front of the queue, so we pop it
        return self.q1.popleft()

    def top(self) -> int:
        """
        Returns the element on the top of the stack without removing it.
        Time Complexity: O(1) - Python's deque allows checking the last element directly.
        (Note: In a pure queue where you can't use index -1, you would either do the same loop 
        as pop, or keep a separate variable tracking the top element).
        """
        return self.q1[-1]

    def empty(self) -> bool:
        """
        Returns true if the stack is empty, false otherwise.
        Time Complexity: O(1)
        """
        return len(self.q1) == 0

def main():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())     # Should print 2
    print(stack.pop())     # Should print 2
    print(stack.empty())   # Should print False (1 is still in the stack)

if __name__ == '__main__':
    main()
