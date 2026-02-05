class Node:
    """
    Node class for a linked list with random pointers.
    
    Each node contains:
    - val: the value stored in the node
    - next: reference to the next node in the sequence
    - random: reference to a random node in the list (or None)
    
    This structure is used for creating complex linked lists where nodes
    can point to arbitrary other nodes in addition to the next sequential node.
    """
    def __init__(self, val, next=None, random=None):
        self.val = val        # Value of the node
        self.next = next      # Reference to next node
        self.random = random  # Reference to a random node in the list

def copyListWithRandomPointer(head):
    """
    Creates a deep copy of a linked list with random pointers.
    
    This function uses a two-pass approach with a dictionary (hash map) 
    to map original nodes to their copies. The algorithm ensures that 
    both the next pointers and random pointers are properly copied.
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(n) for the dictionary storing node mappings
    
    Args:
        head (Node): The head node of the original linked list
        
    Returns:
        Node: The head node of the deep copied linked list
    """
    # Dictionary to map original nodes to their copies
    # Initialize with None:None to handle edge cases where next or random is None
    oldCopy = {None: None}
    
    # First pass: Create copies of all nodes without setting pointers
    # Store mapping from original nodes to their copies
    curr = head
    while curr:
        # Create a new node with the same value
        copy = Node(curr.val)
        # Map original node to its copy
        oldCopy[curr] = copy
        # Move to next node in original list
        curr = curr.next
    
    # Second pass: Set next and random pointers for all copied nodes
    curr = head
    while curr:
        # Get the copy of current node
        copy = oldCopy[curr]
        
        # Set copy's next pointer to the copy of original's next node
        copy.next = oldCopy[curr.next]
        
        # Set copy's random pointer to the copy of original's random node
        copy.random = oldCopy[curr.random]
        
        # Move to next node in original list
        curr = curr.next
    
    # Return the head of the copied list (copy of original head)
    return oldCopy[head]

def main():
    """
    Main function that demonstrates the linked list copying functionality.
    
    Creates a sample linked list with random pointers, makes a deep copy,
    and verifies the copy by printing values from both the original structure
    and the copied structure.
    """
    # Create original linked list: 1 -> 2 -> None
    head = Node(1)
    head.next = Node(2)
    
    # Set random pointers:
    # Node 1's random points to Node 2
    # Node 2's random points to itself (Node 2)
    head.random = head.next
    head.next.random = head.next
    
    # Create a deep copy of the linked list
    copyHead = copyListWithRandomPointer(head)
    
    print("\nCopied linked list (should match original):")
    print(f"copyHead.val = {copyHead.val}")                # Expected: 1
    print(f"copyHead.next.val = {copyHead.next.val}")      # Expected: 2
    print(f"copyHead.random.val = {copyHead.random.val}")  # Expected: 2
    print(f"copyHead.next.random.val = {copyHead.next.random.val}")  # Expected: 2

if __name__ == "__main__":
    main()
