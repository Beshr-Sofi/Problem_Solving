class ListNode:
    """Represents a single node in a Singly-Linked List."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertGreatestCommonDivisors(head):
    """
    Inserts the Greatest Common Divisor (GCD) between every pair of adjacent 
    nodes in a linked list.
    
    Approach: Euclidean Algorithm & Pointer Manipulation
    ----------------------------------------------------
    1. GCD Calculation (Euclidean Algorithm):
       The helper function `GCD(a, b)` finds the greatest common divisor efficiently.
       It repeatedly replaces `(a, b)` with `(b, a % b)`. When `b` reaches 0, 
       `a` contains the GCD. This is much faster than checking every number!
       
    2. Linked List Traversal & Insertion:
       We use a pointer `curr` to walk through the list. As long as we have a 
       current node AND a next node (`while curr.next:`), we have a pair to process.
       
       For each pair:
       - We calculate the GCD of `curr.val` and `curr.next.val`.
       - We create a NEW node with this GCD value.
       - We perform the standard linked list insertion:
         a. Point the new node's `next` to `curr.next`.
         b. Point `curr.next` to the new node.
         (The code cleverly does both in one line: `curr.next = ListNode(gcd, curr.next)`)
       - Crucially, we must move the `curr` pointer forward by TWO steps 
         (`curr = curr.next.next`). This skips over the newly inserted GCD node 
         and lands exactly on the second node of the original pair, ready for the 
         next iteration.
         
    Time Complexity: O(N * log(min(a,b))) - We visit each node once O(N), and at 
                     each step, the Euclidean algorithm takes logarithmic time.
    Space Complexity: O(1) - (Excluding the space used to allocate the new nodes, 
                      which would be O(N)).
    """
    def GCD(a, b):
        # Euclidean algorithm for finding the Greatest Common Divisor
        while b > 0:
            a, b = b, a % b
        return a

    curr = head
    
    # Loop as long as there is a PAIR of nodes to look at
    while curr.next:
        # Get the values of the two adjacent nodes
        val1, val2 = curr.val, curr.next.val
        
        # Calculate their GCD
        gcd = GCD(val1, val2)
        
        # Create a new node with the GCD. 
        # Its 'next' points to curr.next (the right node of the pair).
        # Then, update 'curr.next' to point to this new node.
        curr.next = ListNode(gcd, curr.next)
        
        # Move forward TWO steps to skip the newly inserted GCD node
        # and land on the next original node.
        curr = curr.next.next
        
    return head

def printList(head):
    """Helper function to print a linked list clearly."""
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def main():
    """
    Example demonstrating inserting GCDs into a linked list.
    
    Original list: 18 -> 6 -> 30 -> 12 -> None
    
    Processing pairs:
    - Pair (18, 6): GCD is 6.  Insert 6.
    - Pair (6, 30): GCD is 6.  Insert 6.
    - Pair (30, 12): GCD is 6. Insert 6.
    
    Expected Output: 18 -> 6 -> 6 -> 6 -> 30 -> 6 -> 12 -> None
    """
    # Create a sample linked list: 18 -> 6 -> 30 -> 12
    head = ListNode(18, ListNode(6, ListNode(30, ListNode(12))))
    
    print("Original list:")
    printList(head)
    
    # Insert GCDs
    new_head = insertGreatestCommonDivisors(head)
    
    print("\nList after inserting GCDs:")
    printList(new_head)

if __name__ == "__main__":
    main()
