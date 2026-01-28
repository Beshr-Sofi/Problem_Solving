# Linked List Reversal

## Problem Statement

Reverse a singly-linked list in-place. Convert a linked list from its original order to completely reversed order.

## Problem Breakdown

1. You have a linked list with nodes connected via `next` pointers
2. You need to reverse the direction of all pointers
3. Return the new head of the reversed linked list

## Example

- Original: `1 → 2 → 3 → 4 → 5 → None`
- Reversed: `5 → 4 → 3 → 2 → 1 → None`

## Code Structure

### ListNode Class

Represents a single node in the linked list

- **val**: stores the node's value
- **next**: pointer to the next node in the list

### Solution Class - reverseList() Method

**Purpose:** Reverses a singly-linked list in-place using an iterative approach

**Algorithm (3-Pointer Technique):**

The key insight is to use three pointers to reverse each link:

- **prev**: tracks the previous node (starts as None)
- **curr**: tracks the current node being processed (starts at head)
- **nxt**: temporarily stores the next node before we break the link

**Steps:**

1. Save the next node: `nxt = curr.next` (before we lose access to it)
2. Reverse the pointer: `curr.next = prev` (make current point backward)
3. Move prev forward: `prev = curr`
4. Move curr forward: `curr = nxt`
5. Repeat until curr reaches the end
6. Return prev (which is now the new head)

**Visual Example:**

```
Initial:  None ← 1 ← 2 ← 3 ← 4 ← 5
Process:  None ← 1 ← 2 ← 3 ← 4 ← 5 → ...
Result:   5 → 4 → 3 → 2 → 1 → None
```

## Complexity Analysis

- **Time Complexity**: O(n) - visits each node exactly once
- **Space Complexity**: O(1) - uses only constant extra space (no recursion, no additional data structures)

## Edge Cases

- Empty list (head is None) - returns None
- Single node - returns the node itself
- List with two nodes - reverses correctly
- Very long lists - handles efficiently with O(1) space
