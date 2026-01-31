class ListNode:
    """
    Represents a single node in a linked list.
    
    Attributes:
        val: The value stored in the node
        next: Reference to the next node in the list (None if it's the last node)
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ReorderList(head):
    """
    Reorders a linked list by inserting the last node after the first,
    the second-to-last after the second, and so on.
    
    Example: 1->2->3->4->5 becomes 1->5->2->4->3
    
    Time Complexity: O(n^2) due to repeated traversals
    Space Complexity: O(1)
    
    Args:
        head: The head node of the linked list
    """
    # Base case: empty list or single node - no reordering needed
    if not head or not head.next:
            return

    curr = head
    
    def deleteTail(curr):
        """
        Helper function that finds the last node, removes it from the list,
        and inserts it after the current node.
        
        Args:
            curr: Current node position in the list
            
        Returns:
            The next node to process
        """
        # Traverse to find the second-to-last node
        prev, tmp = None, curr
        while tmp.next:
            prev = tmp
            tmp = tmp.next
        
        # Remove the last node by breaking the link
        prev.next = None
        
        # Insert the last node after current node
        tmp.next = curr.next
        curr.next = tmp
        
        # Move to the next position (skip the inserted node)
        curr = curr.next.next
        return curr
    
    # Keep reordering until we've processed all pairs
    while curr and curr.next:
        curr = deleteTail(curr)

def ReorderList2(head):
    """
    More efficient reordering of a linked list using two-pointer technique.
    
    Algorithm:
    1. Find the middle of the list using slow and fast pointers
    2. Reverse the second half of the list
    3. Merge the first half and reversed second half alternately
    
    Example: 1->2->3->4->5 becomes 1->5->2->4->3
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        head: The head node of the linked list
    """
    # Base case: empty list or single node - no reordering needed
    if not head or not head.next:
        return

    # Step 1: Find the middle of the linked list using slow and fast pointers
    # slow moves 1 step, fast moves 2 steps; when fast reaches end, slow is at middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    # Start from the middle node and reverse all nodes after it
    prev, curr = None, slow
    while curr:
        next_temp = curr.next  # Store next node
        curr.next = prev       # Reverse the link
        prev = curr            # Move prev forward
        curr = next_temp       # Move curr forward

    # Step 3: Merge the two halves alternately
    # first points to start of first half, second points to start of reversed second half
    first, second = head, prev
    while second.next:
        # Store next nodes from both halves
        temp1, temp2 = first.next, second.next
        
        # Insert second half node after first half node
        first.next = second
        second.next = temp1
        
        # Move pointers forward in both halves
        first = temp1
        second = temp2


def main():
    """
    Main function to test the ReorderList implementation.
    Creates a linked list and demonstrates the reordering.
    """
    # Create individual nodes with their values
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node5 = ListNode(1)
    node6 = ListNode(2)

    # Link the nodes together: 3->2->0->-4->1->2
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6 

    # Call ReorderList to reorder the linked list
    # Result: 3->2->2->0->1->-4
    ReorderList(node1)


if __name__ == "__main__":
    main()
