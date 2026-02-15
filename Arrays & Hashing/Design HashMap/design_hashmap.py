class Node:
    """
    Node class for a singly linked list used in hash map buckets.
    
    Each node stores a key-value pair and a pointer to the next node.
    This is used for collision resolution through separate chaining.
    
    Attributes:
        key (int): The key associated with this node
        value (int): The value stored for this key (default -1 for dummy nodes)
        next (Node): Pointer to the next node in the chain
    """
    def __init__(self, key=0, value=-1, next=None):
        self.key = key        # The key (hash map key)
        self.value = value    # The associated value
        self.next = next      # Pointer to next node in chain

class MyHashMap:
    """
    Implementation of a hash map using separate chaining for collision resolution.
    
    This is a custom implementation of a hash map (similar to Java's HashMap or
    Python's dict) that stores key-value pairs with O(1) average time complexity
    for put, get, and remove operations.
    
    Design:
    - Array of size 10,000 (fixed) for buckets
    - Hash function: key % 10000 to distribute keys
    - Separate chaining: each bucket contains a linked list of nodes
    - Dummy head nodes simplify insertion and deletion
    
    Time Complexity:
    - Average: O(1) for put, get, remove
    - Worst case: O(n) when many collisions occur in same bucket
    
    Space Complexity: O(capacity + number of keys) for storing the hash table
    
    This is the standard solution for LeetCode problem 706: Design HashMap.
    """
    
    def __init__(self):
        """
        Initialize the hash map with an array of 10,000 dummy head nodes.
        
        Each bucket gets a dummy node with key=0, value=-1 to simplify
        edge cases when inserting or removing from an empty bucket.
        The dummy node itself never stores actual key-value pairs.
        """
        # Create an array of dummy nodes (one per bucket)
        self.hash = [Node(0) for i in range(10000)]
        self.size = 10**4  # Number of buckets (10,000)

    def put(self, key: int, value: int) -> None:
        """
        Insert or update a key-value pair in the hash map.
        
        Process:
        1. Compute hash index: key % 10000
        2. Traverse the linked list at that bucket
        3. If key already exists, update its value
        4. If key not found, append new node at the end of the chain
        
        Note: This implementation checks both the dummy head and subsequent nodes,
        which may cause redundant checks.
        
        Args:
            key (int): The key to insert or update
            value (int): The value to associate with the key
        """
        index = key % self.size  # Hash function
        curr = self.hash[index]  # Start at dummy head
        
        # Traverse the linked list to find the key
        while curr.next:
            if curr.key == key:
                curr.value = value  # Update existing key
                return
            curr = curr.next
        
        # Check the last node (including dummy head if list is empty)
        if curr.key == key:
            curr.value = value  # Update if key matches (dummy head or last node)
            return
        
        # Key not found, create new node and append to end
        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Retrieve the value associated with a key.
        
        Process:
        1. Compute hash index: key % 10000
        2. Traverse the linked list at that bucket
        3. If key found, return its value
        4. If key not found, return -1
        
        Args:
            key (int): The key to look up
            
        Returns:
            int: The value associated with the key, or -1 if key doesn't exist
        """
        index = key % self.size
        curr = self.hash[index]
        
        # Traverse entire linked list including dummy head
        while curr:
            if curr.key == key:
                return curr.value  # Key found
            curr = curr.next
        
        return -1  # Key not found (LeetCode convention)

    def remove(self, key: int) -> None:
        """
        Remove a key-value pair from the hash map.
        
        Process:
        1. Compute hash index: key % 10000
        2. Traverse the linked list to find the node before the target
        3. If target found, bypass it by updating the previous node's next pointer
        
        Note: This implementation only removes nodes after the dummy head,
        preserving the dummy node itself.
        
        Args:
            key (int): The key to remove
        """
        index = key % self.size
        curr = self.hash[index]
        
        # Traverse until we find the node just before the target
        # Stop when either:
        # - We reach the end (curr.next is None), or
        # - The next node has the target key
        while curr.next and curr.next.key != key:
            curr = curr.next
        
        # If we found the target node (curr.next exists)
        if curr.next:
            # Bypass the target node
            curr.next = curr.next.next
            # The removed node will be garbage collected


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

def main():
    """
    Main function to demonstrate hash map operations.
    
    Tests the MyHashMap implementation with:
    1. put(1,1) and put(2,2) - add two key-value pairs
    2. get(1) - should return 1
    3. get(3) - should return -1 (key not found)
    4. put(2,1) - update existing key 2 to value 1
    5. get(2) - should return 1 (updated value)
    6. remove(2) - delete key 2
    7. get(2) - should return -1 (key removed)
    
    Expected output: 1, -1, 1, -1
    """
    obj = MyHashMap()
    
    # Add key-value pairs
    obj.put(1, 1)   # Insert key 1 with value 1
    obj.put(2, 2)   # Insert key 2 with value 2
    
    # Retrieve values
    print(obj.get(1))  # Expected: 1
    print(obj.get(3))  # Expected: -1 (key not found)
    
    # Update existing key
    obj.put(2, 1)      # Update key 2 from value 2 to 1
    print(obj.get(2))  # Expected: 1
    
    # Remove key
    obj.remove(2)      # Delete key 2
    print(obj.get(2))  # Expected: -1 (key removed)

if __name__ == "__main__":
    main()
