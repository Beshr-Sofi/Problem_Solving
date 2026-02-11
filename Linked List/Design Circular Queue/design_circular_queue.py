class Node:
    """
    Node class for a singly linked list used in the circular queue implementation.
    
    Each node contains:
    - val: the integer value stored in the node
    - next: reference to the next node in the queue (not circularly linked)
    
    Note: This is not a circular linked list - the "circular" refers to the
    queue behavior (reusing space), not the underlying data structure.
    """
    def __init__(self, val=0, next=None):
        self.val = val      # The value/data stored in the node
        self.next = next    # Pointer to the next node in the queue

class MyCircularQueue:
    """
    Implementation of a circular queue using a singly linked list.
    
    A circular queue (also known as ring buffer) is a FIFO data structure that
    reuses the last position when elements are dequeued. This implementation
    uses a linked list with head and tail pointers to achieve O(1) operations.
    
    Key characteristics:
    - Fixed capacity defined at initialization
    - FIFO (First-In-First-Out) behavior
    - Space is reused - after dequeue, new elements can be added to the rear
    - Uses separate head and tail pointers for O(1) enqueue and dequeue
    
    Time Complexity: O(1) for all operations
    Space Complexity: O(k) where k is the capacity
    """
    
    def __init__(self, k: int):
        """
        Initialize the circular queue with a fixed capacity.
        
        Args:
            k (int): Maximum number of elements the queue can hold
        """
        self.space = k      # Maximum capacity of the queue
        self.head = None    # Pointer to the front of the queue (for dequeue)
        self.last = None    # Pointer to the rear of the queue (for enqueue)
        self.size = 0       # Current number of elements in the queue

    def enQueue(self, value: int) -> bool:
        """
        Add an element to the rear of the circular queue.
        
        Process:
        1. Check if queue is full - if so, cannot enqueue
        2. If queue is empty, create first node as both head and last
        3. Otherwise, append new node at the end and update last pointer
        4. Increment size counter
        
        Args:
            value (int): The value to add to the queue
            
        Returns:
            bool: True if successful, False if queue is full
        """
        # Check if queue is at maximum capacity
        if self.size == self.space:
            return False
        
        # Case 1: Queue is empty - create first node
        if not self.head:
            self.head = Node(value)  # New node becomes both head and last
            self.last = self.head
        # Case 2: Queue has elements - append to the end
        else:
            self.last.next = Node(value)  # Link new node after current last
            self.last = self.last.next    # Update last pointer to new node
        
        self.size += 1  # Increment element count
        return True

    def deQueue(self) -> bool:
        """
        Remove an element from the front of the circular queue.
        
        Process:
        1. Check if queue is empty - if so, cannot dequeue
        2. Remove head node by moving head pointer to head.next
        3. Detach the removed node by setting its next to None (cleanup)
        4. Decrement size counter
        
        Args:
            value (int): The value to add to the queue
            
        Returns:
            bool: True if successful, False if queue is empty
        """
        # Check if queue is empty
        if self.size == 0:
            return False
        
        # Remove the head node
        tmp = self.head          # Store reference to node being removed
        self.head = self.head.next  # Move head pointer to next node
        
        # Clean up the removed node (optional but good practice)
        tmp.next = None
        
        self.size -= 1  # Decrement element count
        if self.size == 0:
          self.last = None
        return True

    def Front(self) -> int:
        """
        Get the front element from the queue without removing it.
        
        Returns:
            int: The value at the front of the queue, or -1 if queue is empty
        """
        # Return -1 if queue is empty, otherwise return head node's value
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        """
        Get the last element from the queue without removing it.
        
        Returns:
            int: The value at the rear of the queue, or -1 if queue is empty
        """
        # Return -1 if queue is empty, otherwise return last node's value
        return -1 if self.isEmpty() else self.last.val

    def isEmpty(self) -> bool:
        """
        Check whether the circular queue is empty.
        
        Returns:
            bool: True if queue contains no elements, False otherwise
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Check whether the circular queue is full.
        
        Returns:
            bool: True if queue has reached maximum capacity, False otherwise
        """
        return self.size == self.space


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

def main():
    """
    Main function to demonstrate the circular queue operations.
    
    Tests the MyCircularQueue class with a capacity of 3:
    1. Enqueue 1, 2, 3 - should succeed
    2. Enqueue 4 - should fail (queue full)
    3. Check Rear - should be 3
    4. Check isFull - should be true
    5. Dequeue - removes front element (1)
    6. Enqueue 4 - should succeed (space freed up)
    7. Check Rear - should be 4
    
    Expected output:
    True, True, True, False, 3, True, True, True, 4
    """
    # Create a circular queue with capacity 3
    circularQueue = MyCircularQueue(3)
    
    # Test enqueue operations - first 3 should succeed
    print(circularQueue.enQueue(1))  # Queue: [1] - return true
    print(circularQueue.enQueue(2))  # Queue: [1,2] - return true
    print(circularQueue.enQueue(3))  # Queue: [1,2,3] - return true
    
    # Queue is now full, next enqueue should fail
    print(circularQueue.enQueue(4))  # Queue: [1,2,3] - return false
    
    # Check rear element (should be 3)
    print(circularQueue.Rear())      # Queue unchanged - return 3
    
    # Check if queue is full (should be true)
    print(circularQueue.isFull())    # Queue unchanged - return true
    
    # Dequeue front element (1) - should succeed
    print(circularQueue.deQueue())   # Queue: [2,3] - return true
    
    # Now there's space, enqueue 4 - should succeed
    print(circularQueue.enQueue(4))  # Queue: [2,3,4] - return true
    
    # Check rear element (should be 4)
    print(circularQueue.Rear())      # Queue unchanged - return 4

if __name__ == "__main__":
    main()
