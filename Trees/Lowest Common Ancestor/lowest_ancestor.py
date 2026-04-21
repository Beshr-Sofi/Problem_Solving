class treeNode:
    """Represents a single node in a Binary Search Tree (BST)."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # Value stored in this node
        self.left = left     # Left child (values < this node's value in a BST)
        self.right = right   # Right child (values > this node's value in a BST)


def lowestCommonAncestor(root, p, q):
    """
    Finds the Lowest Common Ancestor (LCA) of two nodes p and q in a BST.

    The LCA is defined as the deepest node in the tree that has both p and q
    as descendants (a node can be a descendant of itself).

    Key Insight — BST Property:
        In a BST, every node's left subtree contains only values LESS than
        the node, and the right subtree contains only values GREATER than it.
        This lets us navigate directly to the LCA without visiting every node:

        ┌─────────────────────────────────────────────────────────────────┐
        │  Both p and q > curr  →  LCA must be in the RIGHT subtree       │
        │  Both p and q < curr  →  LCA must be in the LEFT subtree        │
        │  Otherwise            →  curr is the split point = the LCA ✓    │
        └─────────────────────────────────────────────────────────────────┘

        The "otherwise" case covers three sub-situations:
          • p.val == curr.val  (curr IS p, and q is somewhere below it)
          • q.val == curr.val  (curr IS q, and p is somewhere below it)
          • p and q are on opposite sides of curr  (curr splits them)

    Time Complexity:  O(h) — h is the height of the BST.
                      O(log n) for a balanced BST, O(n) worst-case (skewed).
    Space Complexity: O(1) — iterative, no recursion stack needed.

    Args:
        root (treeNode): Root of the BST.
        p    (treeNode): First target node.
        q    (treeNode): Second target node.

    Returns:
        int: The value of the lowest common ancestor node.
    """
    curr = root  # Start the search from the root

    while curr:
        # Both nodes are in the right subtree — move right
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right

        # Both nodes are in the left subtree — move left
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left

        # The current node is the split point (one node on each side,
        # or one of the nodes IS the current node) — this is the LCA
        else:
            return curr.val


def main():
    """
    Builds a sample BST and finds the LCA of nodes p=2 and q=8.

    BST structure:
                  6
                /   \\
               2     8
              / \\   / \\
             0   4  7   9
                / \\
               3   5

    Finding LCA(2, 8):
      - Start at 6. p=2 < 6 and q=8 > 6  →  split point found!
      - Return 6.

    Expected output: 6
    """
    root = treeNode(6)
    root.left = treeNode(2)
    root.right = treeNode(8)
    root.left.left = treeNode(0)
    root.left.right = treeNode(4)
    root.right.left = treeNode(7)
    root.right.right = treeNode(9)
    root.left.right.left = treeNode(3)
    root.left.right.right = treeNode(5)

    p = treeNode(2)
    q = treeNode(8)
    print(lowestCommonAncestor(root, p, q))  # Output: 6


if __name__ == "__main__":
    main()
