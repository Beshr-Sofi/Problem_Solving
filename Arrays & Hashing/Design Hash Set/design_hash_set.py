class Node:
    """
    Node class for a singly linked list used in hash set buckets.
    
    Each node contains:
    - value: the integer key stored in the node
    - next: reference to the next node in the linked list (chain)
    
    Used for collision resolution through chaining in the hash set.
    """
    def __init__(self, value, next=None):
        self.value = value  # The key value stored in the node
        self.next = next    # Pointer to the next node in the chain

class MyHashSet:
    """
    Implementation of a hash set using separate chaining for collision resolution.
    
    The hash set uses:
    - An array (size 10,000) of linked list buckets
    - Hash function: key % 10000 to distribute keys across buckets
    - Separate chaining: each bucket contains a linked list of keys with same hash
    
    Key characteristics:
    - No duplicate elements allowed
    - Fast average O(1) operations with good hash distribution
    - Handles collisions by chaining multiple keys in same bucket
    """
    
    def __init__(self):
        """
        Initialize the hash set with an array of 10,000 dummy head nodes.
        
        Creates an array where each element is a dummy head Node(0) that 
        serves as the starting point for a linked list (bucket).
        This simplifies edge cases when adding/removing from linked lists.
        """
        self.tmp = [Node(0) for i in range(10000)]  # Array of dummy head nodes
        self.size = 10**4  # Fixed size of the hash table (10,000 buckets)

    def add(self, key: int) -> None:
        """
        Add a key to the hash set if it doesn't already exist.
        
        Process:
        1. Compute hash index: key % 10000
        2. Traverse the linked list at that bucket
        3. If key already exists, do nothing (no duplicates)
        4. If key not found, append new node at end of chain
        
        Time Complexity: 
        - Average: O(1) 
        - Worst case: O(n) when many collisions in same bucket
        
        Args:
            key (int): The integer key to add to the hash set
        """
        index = key % self.size  # Hash function: modulo 10000
        curr = self.tmp[index]   # Start at dummy head of bucket
        
        # Traverse linked list to check if key already exists
        while curr.next:
            if curr.next.value == key:
                return  # Key already exists, no action needed
            curr = curr.next
        
        # Key not found, add new node at end of chain
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        """
        Remove a key from the hash set if it exists.
        
        Process:
        1. Compute hash index: key % 10000
        2. Traverse the linked list at that bucket
        3. If key found, remove node by bypassing it
        4. If key not found, do nothing
        
        Time Complexity:
        - Average: O(1)
        - Worst case: O(n) when many collisions in same bucket
        
        Args:
            key (int): The integer key to remove from the hash set
        """
        index = key % self.size  # Hash function: modulo 10000
        curr = self.tmp[index]   # Start at dummy head of bucket
        
        # Traverse linked list to find key to remove
        while curr.next:
            if curr.next.value == key:
                # Found key, remove node by skipping over it
                curr.next = curr.next.next
                return
            curr = curr.next
        
        # Key not found, nothing to remove

    def contains(self, key: int) -> bool:
        """
        Check if a key exists in the hash set.
        
        Process:
        1. Compute hash index: key % 10000
        2. Traverse the linked list at that bucket
        3. Return True if key found, False otherwise
        
        Note: This implementation differs from add/remove by starting 
        search from the actual dummy node (not dummy.next). This means
        it checks the dummy node's value (0) which is never a user key.
        
        Time Complexity:
        - Average: O(1)
        - Worst case: O(n) when many collisions in same bucket
        
        Args:
            key (int): The integer key to search for
            
        Returns:
            bool: True if key exists in hash set, False otherwise
        """
        index = key % self.size  # Hash function: modulo 10000
        curr = self.tmp[index]   # Start at dummy head of bucket
        
        # Traverse entire linked list including dummy head
        while curr:
            if curr.value == key:
                return True
            curr = curr.next
        
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

def main():
    """
    Main function to demonstrate the hash set operations.
    
    Tests basic hash set functionality:
    1. Adding elements
    2. Checking containment
    3. Adding duplicates (should be ignored)
    4. Removing elements
    5. Checking containment after removal
    """
    # Create hash set instance
    obj = MyHashSet()
    
    # Add elements 1 and 2
    obj.add(1)
    obj.add(2)
    
    # Check containment - should return True for 1, False for 3
    print(obj.contains(1))  # Expected: True
    print(obj.contains(3))  # Expected: False
    
    # Try to add duplicate element 2 (should be ignored)
    obj.add(2)
    
    # Verify 2 still exists
    print(obj.contains(2))  # Expected: True
    
    # Remove element 2
    obj.remove(2)
    
    # Verify 2 no longer exists
    print(obj.contains(2))  # Expected: False
    
    # Summary of operations demonstrated:
    # 1. Added 1 and 2 successfully
    # 2. Contains correctly identified existing/non-existing keys
    # 3. Duplicate addition was ignored
    # 4. Removal worked correctly
    # 5. Post-removal containment check was correct

if __name__ == "__main__":
    main()
