"""
This script implements solutions for the "Reverse Nodes in k-Group" problem.
Given a singly linked list, it reverses the nodes of the list `k` at a time and returns its modified list.
If the number of nodes is not a multiple of `k`, then the left-out nodes at the end should remain as they are.

Classes:
    - ListNode: Represents a node in a singly linked list.

Functions:
    - reverseKGroup(head, k): A variant approach for reversing nodes in k-groups.
    - helper(curr, prev, k): A helper function for the first approach.
    - reverseKGroup_2(head, k): An optimized, iterative approach using a dummy node.
        - Uses `getKth` to find the end of the current k-group.
        - Reverses the links within the k-group in-place.
        - Reconnects the newly reversed group back to the main list.
    - getKth(curr, k): Helper function to find the k-th node from a given node.
    - printList(head): Utility function to print the values of the linked list.
    - main(): Creates a sample linked list and demonstrates `reverseKGroup_2`.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    tmp, curr, prev = head, head, None
    for i in range(length // k):
        if i == 0:
            tmp.next, lol = helper(curr, prev,k)
            prev = tmp
            tmp = tmp.next
            head = lol
        else:
            tmp.next, lol = helper(curr, prev,k)
            prev.next = lol
            prev = tmp
            tmp = tmp.next
        curr = tmp
    return head

def helper(curr, prev, k):
    for i in range(k):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return curr,prev

def reverseKGroup_2(head, k):
    dummy = ListNode(0,head)
    groupPrev = dummy
    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next
        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    return dummy.next

def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    k = 3
    printList(reverseKGroup_2(head, k))

if __name__ == "__main__":
    main()
