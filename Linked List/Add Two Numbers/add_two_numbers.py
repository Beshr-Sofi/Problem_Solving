class ListNode:
    """
    Node class for singly linked list.
    
    Each node contains:
    - val: integer value stored in the node (defaults to 0)
    - next: reference to the next node in the list (defaults to None)
    
    Used to represent numbers where each digit is stored in reverse order.
    """
    def __init__(self, val=0, next=None):
        self.val = val        # Digit value (0-9)
        self.next = next      # Pointer to next digit

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Adds two numbers represented as linked lists (digits in reverse order).
    
    This implementation modifies one of the input lists in-place to store the result.
    It first determines which list is longer, then uses the longer list as the base
    to store the sum, reducing memory usage by reusing existing nodes.
    
    Strategy:
    1. Calculate lengths of both lists (m and n)
    2. Use the longer list as the base for storing result (modify in-place)
    3. Add corresponding digits with carry-over (one)
    4. Handle remaining carry by creating a new node if needed
    
    Args:
        l1: First number as linked list (digits in reverse order)
        l2: Second number as linked list (digits in reverse order)
        
    Returns:
        ListNode: Head of resulting linked list representing the sum
    """
    def getSum(l1, l2):
        """
        Helper function to add two numbers where l2 is modified in-place.
        
        Adds digits from l1 to l2 node by node, handling carry-over.
        l2 must be at least as long as l1 for this to work correctly.
        
        Args:
            l1: Shorter list (or equal length) to add to l2
            l2: Longer list that will be modified in-place to store result
            
        Returns:
            ListNode: Modified l2 list containing the sum
        """
        one = 0                # Carry flag (0 or 1 since digits are 0-9)
        curr = l2              # Current node in l2 (longer list)
        prev = None            # Track previous node for adding carry node
        
        # Add corresponding digits from l1 to l2
        while curr:
            # Calculate sum: l2.val + (l1.val if exists) + carry
            tmp = curr.val + (l1.val if l1 else 0) + one
            one = 1 if tmp >= 10 else 0  # Determine new carry
            curr.val = tmp % 10          # Store single digit result
            
            # Move pointers forward
            l1 = l1.next if l1 else None
            prev = curr
            curr = curr.next
        
        # Handle remaining carry by adding new node
        if one:
            prev.next = ListNode(1)
        
        return l2
    
    # Calculate length of l1
    curr = l1
    m = 0
    while curr:
        m += 1
        curr = curr.next
    
    # Calculate length of l2  
    curr = l2
    n = 0
    while curr:
        n += 1
        curr = curr.next
    
    # Use longer list as base to minimize node creation
    # If l1 is longer, add l2 to l1; otherwise add l1 to l2
    return getSum(l2, l1) if m > n else getSum(l1, l2)

def addTwoNumbers2(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Alternative implementation that creates a new result list.
    
    This approach creates a completely new linked list for the result,
    preserving the original input lists. It's simpler and more readable.
    
    Strategy:
    1. Create dummy head node to simplify edge cases
    2. Add corresponding digits from l1 and l2 with carry
    3. Create new nodes for result digits
    4. Handle remaining carry at the end
    
    Args:
        l1: First number as linked list (digits in reverse order)
        l2: Second number as linked list (digits in reverse order)
        
    Returns:
        ListNode: Head of new linked list representing the sum
    """
    dummy = ListNode()  # Dummy head to simplify list construction
    curr = dummy        # Pointer to current position in result list
    one = 0             # Carry flag (0 or 1)
    
    # Process digits while either list has nodes
    while l1 or l2:
        # Sum current digits plus carry
        tmp = (l1.val if l1 else 0) + (l2.val if l2 else 0) + one
        one = 1 if tmp >= 10 else 0  # Calculate new carry
        
        # Create new node for result digit
        curr.next = ListNode(tmp % 10)
        curr = curr.next
        
        # Move to next digits in input lists
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    # Handle final carry if exists
    if one:
        curr.next = ListNode(1)
    
    return dummy.next  # Skip dummy head

def printListNode(node):
    """
    Utility function to print linked list in readable format.
    
    Args:
        node: Head node of linked list to print
    """
    while node:
        print(node.val, end="->")
        node = node.next
    print("None")

def main():
    """
    Main function demonstrating both implementations.
    
    Creates two sample numbers:
    - l1 represents 342 (2->4->3 in reverse)
    - l2 represents 465 (5->6->4 in reverse)
    
    Expected sum: 807 (7->0->8 in reverse)
    """
    # Create first number: 342 (2->4->3 in linked list)
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    # Create second number: 465 (5->6->4 in linked list)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    printListNode(addTwoNumbers2(l1, l2))

if __name__ == "__main__":
    main()
