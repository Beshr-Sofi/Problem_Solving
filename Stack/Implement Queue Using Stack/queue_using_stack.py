from collections import deque

class MyQueue:
    """
    Implements a First-In-First-Out (FIFO) queue using two stacks.
    In Python, we use collections.deque as a fast stack.
    - s1 is the "input" stack where new elements are always pushed.
    - s2 is the "output" stack used to reverse the order of elements for pop/peek.
    """
    def __init__(self):
       self.s1 = deque()
       self.s2 = deque()

    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue.
        Time complexity: O(1)
        """
        self.s1.append(x)  # Always push new elements onto the input stack (s1)

    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns it.
        Time complexity: Amortized O(1)
        """
        # If the output stack is empty, we need to transfer elements from s1
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())
        # Now, the oldest element is at the top of s2
        return self.s2.pop()

    def peek(self) -> int:
        """
        Returns the element at the front of the queue without removing it.
        Time complexity: O(1)
        """
        # If s2 is not empty, the front of the queue is at the top of s2
        if len(self.s2) != 0:
            return self.s2[-1]
        # Otherwise, the front of the queue is the bottom (first inserted) element of s1
        return self.s1[0]

    def empty(self) -> bool:
        """
        Returns True if the queue is empty, False otherwise.
        Time complexity: O(1)
        """
        # The queue is empty only if both stacks have no elements
        return len(self.s1) == 0 and len(self.s2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
def main():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())

if __name__ == "__main__":
    main()
