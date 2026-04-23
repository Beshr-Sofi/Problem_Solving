class TreeNode:
    """Represents a single node in a Binary Search Tree (BST)."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # Value stored in this node
        self.left = left     # Left child  (values < this node's value)
        self.right = right   # Right child (values > this node's value)


# ─────────────────────────────────────────────────────────────
# Approach 1 — Iterative BST Insertion
# ─────────────────────────────────────────────────────────────

def insertIntoBST(root, val):
    """
    Inserts a new value into a BST iteratively and returns the (possibly new) root.

    Strategy:
        - If the tree is empty, create and return a new node as the root.
        - Otherwise, walk down the tree using BST ordering:
            • val > curr.val  →  go RIGHT
            • val <= curr.val →  go LEFT
          When the appropriate child slot is empty (None), place the new node there.

    Time Complexity:  O(h) — h is the height of the BST.
                      O(log n) average (balanced), O(n) worst case (skewed).
    Space Complexity: O(1) — iterative, no recursion stack.

    Args:
        root (TreeNode): Root of the BST (can be None for an empty tree).
        val  (int):      Value to insert.

    Returns:
        TreeNode: The root of the BST after insertion.
    """
    if not root:
        return TreeNode(val)   # Empty tree — new node becomes the root

    curr = root
    while True:
        if curr.val < val:         # New value belongs in the RIGHT subtree
            if curr.right:
                curr = curr.right  # Keep traversing right
            else:
                curr.right = TreeNode(val)  # Found the insertion spot
                break
        else:                      # New value belongs in the LEFT subtree
            if curr.left:
                curr = curr.left   # Keep traversing left
            else:
                curr.left = TreeNode(val)   # Found the insertion spot
                break

    return root  # Root is unchanged for a non-empty tree


# ─────────────────────────────────────────────────────────────
# Approach 2 — Recursive BST Insertion
# ─────────────────────────────────────────────────────────────

def insertIntoBSTRecursive(root, val):
    """
    Inserts a new value into a BST recursively and returns the (possibly new) root.

    Strategy:
        - Base case: if `root` is None, we've found the correct empty slot —
          create and return a new node.
        - Recursive case: compare `val` with `root.val` to decide which subtree
          to recurse into. Re-assign the child pointer so the new node is linked
          into the tree as the recursion unwinds.

    This is functionally identical to the iterative approach, but expressed
    more concisely. The trade-off is O(h) space on the call stack.

    Time Complexity:  O(h) — same as iterative.
    Space Complexity: O(h) — recursion depth equals the tree height.

    Args:
        root (TreeNode): Current subtree root (None when the slot is found).
        val  (int):      Value to insert.

    Returns:
        TreeNode: The root of the updated subtree.
    """
    if not root:
        return TreeNode(val)   # Base case — insert here

    if root.val < val:
        root.right = insertIntoBSTRecursive(root.right, val)  # Go right
    else:
        root.left = insertIntoBSTRecursive(root.left, val)    # Go left

    return root  # Return the (unchanged) current root so the parent can re-link


# ─────────────────────────────────────────────────────────────
# BST Deletion
# ─────────────────────────────────────────────────────────────

def deleteNode(root, val):
    """
    Deletes a node with the given value from a BST and returns the updated root.

    There are three cases when the target node is found:

    Case 1 — No left child:
        Replace the node with its right child (which may also be None).

    Case 2 — No right child:
        Replace the node with its left child.

    Case 3 — Two children (the tricky case):
        The node cannot simply be removed. Instead:
          1. Find the in-order successor — the smallest value in the RIGHT subtree
             (keep going left from root.right until there is no left child).
          2. Copy the successor's value into the current node.
          3. Recursively delete the successor from the right subtree
             (it has at most one child, so this reduces to Case 1 or 2).

    The in-order successor is chosen because it is the smallest value that is
    still larger than everything in the left subtree, preserving the BST property.

    Time Complexity:  O(h) — each recursive call moves one level deeper.
    Space Complexity: O(h) — recursion stack depth.

    Args:
        root (TreeNode): Root of the BST (or current subtree during recursion).
        val  (int):      Value of the node to delete.

    Returns:
        TreeNode: The root of the BST after deletion.
    """
    if not root:
        return root   # Value not found — nothing to delete

    if root.val < val:
        root.right = deleteNode(root.right, val)   # Target is in the right subtree
    elif root.val > val:
        root.left = deleteNode(root.left, val)     # Target is in the left subtree
    else:
        # Target node found — handle the three cases
        if not root.left:
            return root.right          # Case 1: no left child
        elif not root.right:
            return root.left           # Case 2: no right child
        else:
            # Case 3: two children — find the in-order successor
            temp = root.right
            while temp.left:
                temp = temp.left       # Walk left until the smallest node in right subtree
            root.val = temp.val        # Overwrite current node's value with successor's value
            root.right = deleteNode(root.right, temp.val)  # Delete the successor from right subtree

    return root


def printTree(root):
    """
    Prints tree values using pre-order traversal (root → left → right).

    Args:
        root (TreeNode): Root of the tree to print.
    """
    if not root:
        return
    print(root.val)       # Visit the current node first
    printTree(root.left)  # Then the left subtree
    printTree(root.right) # Then the right subtree


def main():
    """
    Demonstrates BST insertion (both iterative and recursive) and deletion.

    Values inserted: [4, 2, 7, 1, 3]

    Resulting BST:
            4
           / \\
          2   7
         / \\
        1   3

    After deleting 7 (a leaf node — Case 1: no left child):
            4
           /
          2
         / \\
        1   3
    """
    root = None   # Will be built using iterative insertion
    root1 = None  # Will be built using recursive insertion
    vals = [4, 2, 7, 1, 3]

    for val in vals:
        root = insertIntoBST(root, val)
        root1 = insertIntoBSTRecursive(root1, val)

    printTree(root)
    print("=" * 20)
    printTree(root1)

    # Delete node 7 from both trees
    root = deleteNode(root, 7)
    root1 = deleteNode(root1, 7)
    print("=" * 20)
    printTree(root)
    print("=" * 20)
    printTree(root1)


if __name__ == "__main__":
    main()
