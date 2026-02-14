class Node:
    """
    Node class for doubly linked list used in LRU Cache implementation.
    
    Each node stores:
    - key: The original key (needed for cache eviction)
    - val: The value associated with the key
    - next: Pointer to the next node in the list (towards MRU)
    - prev: Pointer to the previous node in the list (towards LRU)
    
    The doubly linked list allows O(1) removal and insertion of nodes
    from anywhere in the list.
    """
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.next = next      # Pointer to more recently used node
        self.val = val        # Value stored in cache
        self.prev = prev      # Pointer to less recently used node
        self.key = key        # Original key (for dictionary lookup during eviction)

class LRUCache:
    """
    Least Recently Used (LRU) Cache implementation.
    
    This data structure maintains a fixed-size cache where the least recently used
    items are evicted when the cache reaches capacity. It provides O(1) get and put
    operations by combining:
    1. A hash map (dictionary) for O(1) key lookup
    2. A doubly linked list for O(1) tracking of usage order
    
    Design:
    - Most Recently Used (MRU) items are at the end (near self.right)
    - Least Recently Used (LRU) items are at the beginning (near self.left)
    - Dummy head (self.left) and tail (self.right) nodes simplify edge cases
    
    Time Complexity: O(1) for both get() and put()
    Space Complexity: O(capacity) for storing up to capacity items
    """
    
    def __init__(self, capacity):
        """
        Initialize the LRU cache with given capacity.
        
        Creates:
        - capacity: Maximum number of items cache can hold
        - cache: Dictionary mapping keys to nodes for O(1) lookup
        - left: Dummy head node (always points to LRU item)
        - right: Dummy tail node (always points to MRU item)
        
        The dummy nodes are connected to each other initially (empty list).
        """
        self.capacity = capacity           # Maximum cache size
        self.cache = {}                    # Hash map: key -> Node
        self.left = Node()                 # Dummy head (LRU side)
        self.right = Node()                 # Dummy tail (MRU side)
        
        # Initialize empty doubly linked list: left <-> right
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        """
        Remove a node from the doubly linked list.
        
        This operation takes O(1) time by updating the pointers of
        the node's neighbors to bypass the current node.
        
        Args:
            node (Node): The node to remove from the linked list
        """
        # Get the neighbors of the current node
        prev = node.prev    # Node before current
        nxt = node.next     # Node after current
        
        # Bypass the current node by connecting prev directly to nxt
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        """
        Insert a node at the MRU position (just before the right dummy).
        
        Newly accessed or added nodes are always placed at the MRU end.
        This operation takes O(1) time.
        
        Args:
            node (Node): The node to insert at the MRU position
        """
        # Get the node currently before the right dummy (last real node)
        prev = self.right.prev
        nxt = self.right
        
        # Connect prev to new node, and new node to right dummy
        prev.next = nxt.prev = node
        
        # Set new node's pointers
        node.next = nxt
        node.prev = prev
    
    def get(self, key):
        """
        Retrieve a value from the cache by key.
        
        If the key exists:
        1. Remove it from its current position in the linked list
        2. Re-insert it at the MRU position (right end)
        3. Return its value
        
        This updates the usage order - accessed item becomes most recently used.
        
        Args:
            key: The key to look up in the cache
            
        Returns:
            The value associated with the key, or -1 if key doesn't exist
        """
        if key in self.cache:
            # Get the node from hash map
            node = self.cache[key]
            
            # Move to MRU position: remove then re-insert
            self.remove(node)    # Take out from current position
            self.insert(node)    # Put at MRU end (near right)
            
            return node.val
        return -1  # Key not found (LeetCode convention)
    
    def put(self, key, value):
        """
        Add or update a key-value pair in the cache.
        
        If key exists: Update its value and move to MRU position
        If key is new: Create new node and add to MRU position
        
        After insertion, if cache exceeds capacity:
        - Remove the LRU node (left.next) from both list and dictionary
        
        Args:
            key: The key to add or update
            value: The value to associate with the key
        """
        # If key already exists, remove it first (will re-insert as MRU)
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Create new node and insert at MRU position
        node = Node(value, key)    # Note: Node constructor expects (val, key)
        self.insert(node)
        self.cache[key] = node
        
        # Check if cache exceeded capacity
        if len(self.cache) > self.capacity:
            # The LRU node is the first real node after left dummy
            lru = self.left.next
            
            # Remove it from linked list
            self.remove(lru)
            
            # Remove it from hash map using stored key
            del self.cache[lru.key]

def main():
    """
    Main function to demonstrate LRU Cache operations.
    
    Tests with capacity 2:
    1. put(1,1) and put(2,2) - cache: [1,2] (2 is MRU)
    2. get(1) - returns 1, cache becomes [2,1] (1 is MRU)
    3. put(3,3) - evicts LRU (key 2), cache: [1,3] (3 is MRU)
    4. get(2) - returns -1 (evicted)
    5. put(4,4) - evicts LRU (key 1), cache: [3,4] (4 is MRU)
    6. get(3) - returns 3, cache: [4,3] (3 is MRU)
    7. get(4) - returns 4, cache: [3,4] (4 is MRU)
    
    Expected output: 1, -1, 3, 4
    """
    # Create LRU cache with capacity 2
    cache = LRUCache(2)
    
    # Add two items
    cache.put(1, 1)    # Cache: {1=1}
    cache.put(2, 2)    # Cache: {1=1, 2=2} (2 is MRU)
    
    # Access key 1 - becomes MRU
    print(cache.get(1))  # Returns 1, Cache: {2=2, 1=1} (1 is MRU)
    
    # Add new item - exceeds capacity, evicts LRU (key 2)
    cache.put(3, 3)      # Evicts 2, Cache: {1=1, 3=3} (3 is MRU)
    
    # Try to access evicted key
    print(cache.get(2))  # Returns -1 (not found)
    
    # Add another item - evicts LRU (key 1)
    cache.put(4, 4)      # Evicts 1, Cache: {3=3, 4=4} (4 is MRU)
    
    # Access remaining items
    print(cache.get(3))  # Returns 3, Cache: {4=4, 3=3} (3 is MRU)
    print(cache.get(4))  # Returns 4, Cache: {3=3, 4=4} (4 is MRU)

if __name__ == "__main__":
    main()
