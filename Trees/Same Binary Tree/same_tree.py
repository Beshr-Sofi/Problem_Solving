from collections import deque


class treeNode:
    """Represents a single node in a binary tree."""
    def __init__(self, val, left=None, right=None):
        self.val = val       # The value stored in this node
        self.left = left     # Pointer to the left child node
        self.right = right   # Pointer to the right child node


def isSameTree(p, q):
    """
    Determines whether two binary trees are identical in both structure and values.

    Two trees are considered the same if:
      1. They have the exact same shape (structure).
      2. Every corresponding pair of nodes holds the same value.

    Approach — BFS (Breadth-First Search / Level-order traversal):
        - Both trees are traversed simultaneously level by level using two queues.
        - At each step, the front nodes of both queues are compared:
            • If both are None  → both subtrees are absent here, continue.
            • If only one is None → structural mismatch, return False.
            • If values differ   → value mismatch, return False.
        - If one queue still has remaining nodes while the other is empty,
          the trees have different sizes, so return False.
        - If the entire traversal completes without a mismatch, return True.

    Time Complexity:  O(n) — every node in both trees is visited once.
    Space Complexity: O(n) — at most O(n) nodes can be held in the queues at once.

    Args:
        p (treeNode): Root of the first binary tree.
        q (treeNode): Root of the second binary tree.

    Returns:
        bool: True if the two trees are identical, False otherwise.
    """
    # Initialise a queue for each tree, starting with their roots
    queue1 = deque([p])
    queue2 = deque([q])

    # Process both trees level by level as long as both queues have nodes
    while queue1 and queue2:
        # Process all nodes at the current level (snapshot the length first)
        for i in range(len(queue1)):
            node1 = queue1.popleft()  # Dequeue from tree 1
            node2 = queue2.popleft()  # Dequeue from tree 2

            # Case 1: Both positions are empty — structurally identical here
            if node1 is None and node2 is None:
                continue

            # Case 2: One is empty, the other is not — structural mismatch
            if node1 is None or node2 is None:
                return False

            # Case 3: Both exist but hold different values — value mismatch
            if node1.val != node2.val:
                return False

            # Enqueue children of both nodes for the next level
            queue1.append(node1.left)
            queue1.append(node1.right)
            queue2.append(node2.left)
            queue2.append(node2.right)

    # If one queue still has nodes, the trees have different sizes
    if queue1 or queue2:
        return False

    return True  # All nodes matched — trees are identical


def main():
    """
    Builds a sample binary tree and tests isSameTree by comparing it with itself.

    Tree structure:
          1
         / \\
        2   3

    Since both arguments are the same tree object, the result is True.
    Expected output: True
    """
    root = treeNode(1)
    root.left = treeNode(2)
    root.right = treeNode(3)

    print(isSameTree(root, root))  # Output: True


if __name__ == "__main__":
    main()
