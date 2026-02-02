class ListNode:
    """
    A node in a singly linked list.
    
    Attributes:
        val: The value stored in the node
        next: Reference to the next node in the list (or None if it's the last node)
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def RemoveNodeFromEnd(head, n):
    """
    Remove the n-th node from the end of a linked list using two passes.
    
    Algorithm:
    1. First pass: Traverse the entire list to find its length
    2. Calculate the position of the node to remove from the start
    3. Second pass: Navigate to the node before the target and remove it
    
    Time Complexity: O(n) - Two passes through the list
    Space Complexity: O(1) - No extra space used
    
    Args:
        head: The head of the linked list
        n: The position from the end of the node to remove (1-indexed)
    
    Returns:
        The head of the modified linked list
    """
    # Edge case: If the list has only one node, return None
    if not head.next:
        return None
    
    # First pass: Count the total number of nodes
    curr = head
    i = 1
    while curr.next:
        i += 1
        curr = curr.next
    
    # Calculate how many steps from the beginning to reach the node before target
    i -= n
    
    # Second pass: Navigate to the node just before the one to remove
    prev, curr = None, head
    while i:
        prev = curr
        curr = curr.next
        i -= 1
    
    # If prev is None, the head itself is to be removed
    if not prev:
        return curr.next
    
    # Remove the target node by linking the previous node to the next node
    prev.next = curr.next
    curr.next = None
    return head

def RemoveNodeFromEnd2(head, n):
    """
    Remove the n-th node from the end of a linked list using the two-pointer technique.
    
    Algorithm (Two-Pointer / Fast-Slow Pointer):
    1. Use a dummy node pointing to the head (handles edge case of removing head)
    2. Create two pointers (first and second) both starting at dummy
    3. Move first pointer n+1 steps ahead
    4. Move both pointers together until first reaches the end
    5. The second pointer will be just before the node to remove
    6. Perform the removal by updating the next pointer
    
    Advantages:
    - Single pass through the list (after the initial n+1 advance)
    - Elegant handling of edge cases with dummy node
    
    Time Complexity: O(n) - Single pass through the list
    Space Complexity: O(1) - Only using two pointers
    
    Args:
        head: The head of the linked list
        n: The position from the end of the node to remove (1-indexed)
    
    Returns:
        The head of the modified linked list
    """
    # Create a dummy node to handle edge case of removing the head
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move first pointer n+1 steps ahead to create the gap
    for _ in range(n + 1):
        first = first.next

    # Move both pointers until first reaches the end
    # This positions second pointer just before the node to remove
    while first:
        first = first.next
        second = second.next

    # Remove the n-th node from the end by skipping it
    second.next = second.next.next

    return dummy.next

def print_linked_list(head):
    """
    Print the linked list in a readable format.
    
    Args:
        head: The head of the linked list
    """
    curr = head
    values = []
    # Traverse the entire list and collect values
    while curr:
        values.append(str(curr.val))
        curr = curr.next
    # Print the list with arrow separators for clarity
    print(" -> ".join(values))

def main():
    """
    Main function to demonstrate removing a node from the end of a linked list.
    """
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original linked list:")
    print_linked_list(head)

    # Remove the 2nd node from the end (node with value 4)
    n = 2
    head = RemoveNodeFromEnd2(head, n)

    print(f"Linked list after removing the {n}-th node from the end:")
    print_linked_list(head)
