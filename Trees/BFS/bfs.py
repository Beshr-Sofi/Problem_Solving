from collections import deque


class treeNode:
    """Represents a single node in a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # Value stored in this node
        self.left = left     # Pointer to the left child
        self.right = right   # Pointer to the right child


def levelOrder(root):
    """
    Returns the level-order (breadth-first) traversal of a binary tree.

    Level-order traversal visits nodes level by level, from left to right,
    starting at the root. Each level's values are collected into a separate
    sub-list, so the result is a list of lists.

    Approach — BFS with a queue:
        1. Initialise a deque with the root node.
        2. On each iteration of the outer `while` loop, the queue holds
           exactly all the nodes at the current level.
        3. Process every node at that level (snapshot the count with `len(q)`
           before the inner loop so newly added children don't interfere):
             • Pop the front node.
             • Enqueue its left child (if any).
             • Enqueue its right child (if any).
             • Record its value in a temporary list `tmp`.
        4. After the inner loop, append `tmp` (one complete level) to `res`.
        5. Repeat until the queue is empty (all levels processed).

    Why snapshot `len(q)` first?
        Without it, the `range` would grow as children are added mid-loop,
        causing nodes from the next level to be processed in the current level.

    Time Complexity:  O(n) — every node is enqueued and dequeued exactly once.
    Space Complexity: O(n) — the queue holds at most all nodes of the widest level.

    Args:
        root (treeNode): Root of the binary tree.

    Returns:
        list[list[int]]: A list where each element is a list of node values
                         at that depth, ordered left to right.
                         Returns [] if the tree is empty.
    """
    if not root:
        return []  # Edge case: empty tree

    res = []              # Final result — one sub-list per level
    q = deque([root])     # BFS queue, seeded with the root

    while q:              # Continue until all levels have been processed
        tmp = []          # Collects values for the current level
        for i in range(len(q)):   # Process only nodes already in the queue (current level)
            node = q.popleft()    # Dequeue the front node
            if node.left:
                q.append(node.left)   # Enqueue left child for the next level
            if node.right:
                q.append(node.right)  # Enqueue right child for the next level
            tmp.append(node.val)      # Record this node's value
        res.append(tmp)   # Add the completed level to the result

    return res


def main():
    """
    Builds a sample binary tree and prints its level-order traversal.

    Tree structure:
            3
           / \\
          9  20
            /  \\
           15   7

    Level-order traversal:
      Level 0: [3]
      Level 1: [9, 20]
      Level 2: [15, 7]

    Expected output: [[3], [9, 20], [15, 7]]
    """
    root = treeNode(3)
    root.left = treeNode(9)
    root.right = treeNode(20)
    root.right.left = treeNode(15)
    root.right.right = treeNode(7)

    print(levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]


if __name__ == "__main__":
    main()
