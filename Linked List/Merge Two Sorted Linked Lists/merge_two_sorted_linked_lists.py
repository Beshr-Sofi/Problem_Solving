class ListNode:
    """Represents a single node in a singly linked list.
    
    Attributes:
        val: The value/data stored in the node
        next: Reference to the next node in the list (None if last node)
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """Merges two sorted linked lists into a single sorted linked list.
    
    Takes two sorted linked lists and combines them into one sorted list by
    comparing node values and appending the smaller value to the result.
    
    Args:
        list1 (ListNode): The head of the first sorted linked list (can be None)
        list2 (ListNode): The head of the second sorted linked list (can be None)
        
    Returns:
        ListNode: The head of the merged sorted linked list
        
    Time Complexity: O(n + m) where n and m are the lengths of the two lists
    Space Complexity: O(1) - only uses constant extra space
    """
    head = ListNode()
    current = None
    if list1 == None and list2 == None:
        return None
    elif list1 == None:
        return list2
    elif list2 == None:
        return list1
    elif current == None:
        if list1.val < list2.val:
            head.val = list1.val
            list1 = list1.next
        else:
            head.val = list2.val
            list2 = list2.next
        current = head
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
            current = current.next
        else:
            current.next = list2
            list2 = list2.next
            current = current.next

    current.next = list1 or list2

    return head

def main():
    """Main function that demonstrates the mergeTwoLists function.
    
    Creates two sample sorted linked lists and merges them together,
    then prints the result.
    """
    # Example usage:
    # Creating first sorted linked list: 1 -> 3 -> 5
    list1 = ListNode(1, ListNode(3, ListNode(5)))
    
    # Creating second sorted linked list: 2 -> 4 -> 6
    list2 = ListNode(2, ListNode(4, ListNode(6)))
    
    # Merging the two lists
    merged_list = mergeTwoLists(list1, list2)
    
    # Printing the merged linked list
    current = merged_list
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    
if __name__ == "__main__":
    main()
