from collections import defaultdict

class Node:
    """
    Node class for doubly linked list used in the first LFU cache implementation.
    
    Each node stores:
    - key: The original key (for cache eviction)
    - val: The value associated with the key
    - next: Pointer to next node (higher frequency or same frequency, newer)
    - prev: Pointer to previous node (lower frequency or same frequency, older)
    - count: Access frequency counter
    """
    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.key = key        # Cache key
        self.val = val        # Cache value
        self.next = next      # Next node in list
        self.prev = prev      # Previous node in list
        self.count = 0        # Frequency of access (LFU count)

class LFUCache:
    """
    First LFU (Least Frequently Used) Cache implementation.
    
    This implementation uses a single doubly linked list ordered by frequency
    and recency. Nodes are inserted in a position based on their access count.
    
    Design:
    - Single doubly linked list with dummy head (left) and tail (right)
    - List is ordered by frequency (ascending) and within same frequency by recency
    - Right dummy node has count = infinity to simplify insertion logic
    - Hash map for O(1) key lookup
    
    Time Complexity: O(n) for put/get due to traversal to find insertion position
    Space Complexity: O(capacity)
    
    This is a custom implementation, not the standard approach for LFU cache.
    """
    
    def __init__(self, capacity: int):
        """
        Initialize LFU cache with given capacity.
        
        Args:
            capacity (int): Maximum number of items cache can hold
        """
        self.size = capacity           # Maximum cache size
        self.map = {}                  # Hash map: key -> Node
        self.left, self.right = Node(), Node()  # Dummy head and tail
        self.left.next = self.right    # Connect head to tail
        self.right.prev = self.left     # Connect tail to head
        self.right.count = float('inf')  # Tail has infinite count (always greater)

    def remove(self, node):
        """
        Remove a node from the doubly linked list.
        
        Updates the pointers of neighboring nodes to bypass the current node.
        
        Args:
            node (Node): The node to remove from the list
        """
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        """
        Insert a node at the correct position based on its frequency count.
        
        The list is ordered by count (ascending). Nodes with the same count
        maintain recency order (newer nodes after older ones).
        
        Args:
            node (Node): The node to insert into the list
        """
        curr = self.left
        # Traverse until we find a node with count >= current node's count
        # This ensures nodes with lower counts come first
        while node.count >= curr.count:
            curr = curr.next
        
        # Insert node before curr (which has count >= node.count)
        prev, nxt = curr.prev, curr
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        """
        Retrieve a value from the cache by key.
        
        If key exists:
        1. Increment its access count
        2. Remove it from its current position
        3. Re-insert it at new position based on updated count
        4. Return its value
        
        Args:
            key (int): The key to look up
            
        Returns:
            int: The value associated with the key, or -1 if key doesn't exist
        """
        if key in self.map.keys():
            node = self.map[key]
            node.count += 1           # Increment access frequency
            self.remove(node)         # Remove from current position
            self.insert(node)         # Re-insert at new position
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Add or update a key-value pair in the cache.
        
        If cache is at capacity, evict the least frequently used item
        (the node with smallest count, and if tie, least recently used).
        
        Note: This implementation has a bug - it doesn't check if key exists
        before creating a new node, leading to duplicate keys.
        
        Args:
            key (int): The key to add or update
            value (int): The value to associate with the key
        """
        # If cache is full, evict the LFU item (leftmost node after dummy)
        if len(self.map) == self.size:
            # Remove from hash map using key stored in node
            del self.map[self.left.next.key]
            # Remove from linked list
            self.remove(self.left.next)
        
        # Create new node (BUG: Doesn't check if key already exists)
        node = Node(key, value)
        self.map[key] = node
        node.count = 1                 # Initial access count
        self.insert(node)              # Insert at correct position


class ListNode:
    """
    Node class for doubly linked list used in the second LFU cache implementation.
    
    Simpler node structure used in the frequency-based linked lists.
    """
    def __init__(self, val, prev=None, next=None):
        self.val = val        # Value (key) stored in node
        self.prev = prev      # Previous node pointer
        self.next = next      # Next node pointer

class LinkedList:
    """
    Custom doubly linked list with map for O(1) access to nodes.
    
    This list maintains nodes in order of recency (most recent at right).
    Used to track keys with the same access frequency.
    """
    
    def __init__(self):
        """Initialize linked list with dummy head and tail."""
        self.left = ListNode(0)           # Dummy head
        self.right = ListNode(0, self.left)  # Dummy tail
        self.left.next = self.right
        self.map = {}                      # Map value -> node for O(1) access

    def length(self):
        """Return the number of nodes in the list."""
        return len(self.map)

    def pushRight(self, val):
        """
        Add a new node at the right end (most recent position).
        
        Args:
            val: The value to add to the list
        """
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        """
        Remove a node with given value from the list.
        
        Args:
            val: The value to remove
        """
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)

    def popLeft(self):
        """
        Remove and return the leftmost node (least recently used).
        
        Returns:
            The value of the removed node
        """
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res

    def update(self, val):
        """
        Update a value's position to most recent (right end).
        
        Args:
            val: The value to update
        """
        self.pop(val)        # Remove from current position
        self.pushRight(val)  # Add to right end

class LFUCache2:
    """
    Second LFU (Least Frequently Used) Cache implementation.
    
    This is the standard optimal implementation for LFU cache (LeetCode 460).
    It uses:
    - Three hash maps for O(1) operations
    - Frequency-to-linkedlist mapping for O(1) access to items with same count
    - Maintains min frequency for O(1) eviction
    
    Design:
    - valMap: key -> value (actual cache data)
    - countMap: key -> frequency count
    - listMap: frequency -> LinkedList of keys with that frequency
    - lfuCnt: current minimum frequency in cache
    
    Time Complexity: O(1) for both get and put
    Space Complexity: O(capacity)
    """
    
    def __init__(self, capacity: int):
        """
        Initialize LFU cache with given capacity.
        
        Args:
            capacity (int): Maximum number of items cache can hold
        """
        self.cap = capacity                # Maximum cache size
        self.lfuCnt = 0                    # Current minimum frequency
        self.valMap = {}                    # Map key -> value
        self.countMap = defaultdict(int)    # Map key -> access count
        # Map count of key -> linkedlist of keys with that count
        self.listMap = defaultdict(LinkedList)

    def counter(self, key):
        """
        Update the frequency counter for a key.
        
        When a key is accessed:
        1. Get its current count
        2. Increment count in countMap
        3. Remove key from old frequency list
        4. Add key to new frequency list
        5. Update lfuCnt if needed
        
        Args:
            key: The key being accessed
        """
        cnt = self.countMap[key]            # Current count
        self.countMap[key] += 1             # Increment count
        
        # Remove from old frequency list
        self.listMap[cnt].pop(key)
        # Add to new frequency list (at most recent position)
        self.listMap[cnt + 1].pushRight(key)
        
        # If this was the last key at the minimum frequency,
        # increment lfuCnt to the next higher frequency
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        """
        Retrieve a value from the cache by key.
        
        If key exists:
        1. Update its frequency counter
        2. Return its value
        
        Args:
            key (int): The key to look up
            
        Returns:
            int: The value associated with the key, or -1 if key doesn't exist
        """
        if key not in self.valMap:
            return -1
        
        self.counter(key)        # Update frequency
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        """
        Add or update a key-value pair in the cache.
        
        If key exists: Update value and increment frequency
        If key is new: Add to cache, may evict LFU item if at capacity
        
        Args:
            key (int): The key to add or update
            value (int): The value to associate with the key
        """
        if self.cap == 0:
            return
        
        # If key is new and cache is full, evict LFU item
        if key not in self.valMap and len(self.valMap) == self.cap:
            # Remove least frequently used (and least recent) item
            res = self.listMap[self.lfuCnt].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)
        
        # Update value in valMap
        self.valMap[key] = value
        
        # Update frequency (handles both new and existing keys)
        self.counter(key)
        
        # Update lfuCnt to the minimum of current and new key's count
        # For new keys, this ensures lfuCnt is at least 1
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    """
    Main function to demonstrate both LFU cache implementations.
    
    Tests both caches with the same sequence of operations:
    1. put(1,1) and put(2,2) - add two items
    2. get(1) - returns 1, increases frequency of key 1
    3. put(3,3) - evicts LFU item (key 2, frequency 1)
    4. get(2) - returns -1 (evicted)
    5. put(4,4) - evicts LFU item (key 3, frequency 1)
    6. get(3) - returns -1 (evicted)
    7. get(4) - returns 4
    
    Expected output:
    1
    -1
    -1
    4
    (same for both implementations)
    """
    # Test first LFU implementation
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))       # returns 1
    cache.put(3, 3)           # evicts key 2
    print(cache.get(2))       # returns -1 (not found)
    cache.put(4, 4)           # evicts key 3
    print(cache.get(3))       # returns -1 (not found)
    print(cache.get(4))       # returns 4
    
    print('=' * 20)
    
    # Test second (optimal) LFU implementation
    cache = LFUCache2(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))       # returns 1
    cache.put(3, 3)           # evicts key 2
    print(cache.get(2))       # returns -1 (not found)
    cache.put(4, 4)           # evicts key 3
    print(cache.get(3))       # returns -1 (not found)
    print(cache.get(4))       # returns 4

if __name__ == "__main__":
    main()
