# This class represents a single node in a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # Store the node's value
        self.next = next    # Pointer to the next node

class Solution:
    """Solution class containing methods to manipulate linked lists."""
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head  # Initialize: prev=None, curr=head
        
        while curr:  # Continue until we reach the end of the list
            nxt = curr.next       # Step 1: Save the next node before we break the link
            curr.next = prev      # Step 2: Reverse the current node's pointer
            prev = curr           # Step 3: Move prev forward to current node
            curr = nxt            # Step 4: Move curr forward to next node
        
        return prev  # Return the new head (was the last node)

def main():
    # Create a Solution instance
    sol = Solution()
    
    # Step 1: Build a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Step 2: Reverse the linked list using the reverseList method
    reversed_head = sol.reverseList(head)

    # Step 3: Print the reversed linked list (should be: 5 -> 4 -> 3 -> 2 -> 1)
    current = reversed_head
    while current:
        # Print each node's value with an arrow separator
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    
    print()  # Print newline at the end

if __name__ == "__main__":
    main()
