class ListNode:
    """
    Standard definition for a node in a singly linked list.
    Holds a value (val) and a pointer to the next node (next).
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLinkedLists(lists):
    """
    Approach 1: Brute Force.
    Finds the minimum value across the heads of all remaining linked lists one by one.
    Time Complexity: O(N * k) where N is the total number of nodes and k is the number of lists.
    *Note: Returns `res` instead of `res.next`, which includes an extra dummy node (0) at the start.
    """
    res = ListNode()
    head = res
    def check(lists):
        for i in lists:
            if i:
                return True
        return False
    def get_min(lists):
        mini = ListNode(val=float('inf'))
        min_index = 0
        for i in range(len(lists)):
            if lists[i] and lists[i].val < mini.val:
                mini = lists[i]
                min_index = i
        value = mini.val
        lists[min_index] = lists[min_index].next
        return value

    while check(lists):
        value = get_min(lists)
        head.next = ListNode(value)
        head = head.next
    return res

def mergeKLinkedLists_2(lists):
    """
    Approach 2: Divide and Conquer (Optimized).
    Repeatedly merges pairs of linked lists until only one giant list remains.
    Time Complexity: O(N log k) where N is the total number of nodes and k is the number of lists.
    """
    if not lists or len(lists) == 0:
            return None

    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeList(l1, l2))
        lists = mergedLists
    return lists[0]

def mergeList(l1, l2):
    """
    Helper function to merge exactly two sorted linked lists using a dummy node.
    """
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

def print_list(head):
    """Utility function to print out a linked list."""
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

def main():
    lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
    res = mergeKLinkedLists_2(lists)
    print_list(res)

if __name__ == "__main__":
    main()
