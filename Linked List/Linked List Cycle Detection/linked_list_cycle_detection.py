"""
LinkedList Cycle Detection - A program to detect cycles in a linked list using two different approaches.

This module implements two algorithms to detect whether a linked list contains a cycle:
1. LinkedListCycleDetection - Uses a list to track visited nodes
2. LinkedListCycleDetection2 - Uses Floyd's Cycle Detection (Tortoise and Hare)
"""

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

def LinkedListCycleDetection(head):
    """
    Detects if a linked list contains a cycle using a list to track visited nodes.
    
    Algorithm:
    - If the list is empty, return False (no cycle possible)
    - Traverse the list, storing each node in a list
    - Before moving to the next node, check if it's already been visited
    - If we find a node that points to an already visited node, a cycle exists
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(n) for the list storing visited nodes
    
    Args:
        head: The starting node of the linked list
        
    Returns:
        True if a cycle is detected, False otherwise
    """
    if not head:
        return False
    curr = head
    check = []
    while curr.next and curr.next not in check:
        check.append(curr)
        curr = curr.next
    return True if curr.next else False

def LinkedListCycleDetection2(head):
    """
    Detects if a linked list contains a cycle using Floyd's Cycle Detection Algorithm 
    (also known as Tortoise and Hare).
    
    Algorithm:
    - Two pointers are initialized: slow moves 1 step at a time, fast moves 2 steps
    - If there's a cycle, the fast pointer will eventually catch up to the slow pointer
    - If fast reaches the end (None), there's no cycle
    - When fast and slow point to the same node, a cycle is detected
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(1) - only uses two pointers, no extra space
    
    Args:
        head: The starting node of the linked list
        
    Returns:
        True if a cycle is detected, False otherwise
    """
    slow , fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        if slow == fast:
            return True
    return False

def main():
    """
    Main function that demonstrates both cycle detection algorithms with test cases.
    
    Test Case 1: A linked list with a cycle
        - Creates nodes: 3 -> 2 -> 0 -> -4 -> 2 (cycle back to node 2)
        - Both methods should return True
        
    Test Case 2: A linked list without a cycle
        - Creates nodes: 1 -> 2
        - Both methods should return False
    """
    # Example usage:
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle

    print(LinkedListCycleDetection(node1))  # Output: True
    print(LinkedListCycleDetection2(node1)) # Output: True

    node5 = ListNode(1)
    node6 = ListNode(2)

    node5.next = node6  # No cycle

    print(LinkedListCycleDetection(node5))  # Output: False
    print(LinkedListCycleDetection2(node5)) # Output: False

if __name__ == "__main__":
    main()
