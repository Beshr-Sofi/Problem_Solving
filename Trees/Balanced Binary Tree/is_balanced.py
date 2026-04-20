class treeNode:
    """Represents a single node in a binary tree."""
    def __init__(self, val):
        self.val = val       # The value stored in the node
        self.left = None     # Pointer to the left child
        self.right = None    # Pointer to the right child


def isBalanced(root):
    """
    Determines whether a binary tree is height-balanced.

    A binary tree is considered balanced if, for every node in the tree,
    the heights of its left and right subtrees differ by at most 1.

    Approach:
        - Use a nested helper function `height()` that computes the height
          of each subtree via post-order traversal (left -> right -> root).
        - During the height calculation, if any node is found to be unbalanced
          (i.e. |left_height - right_height| > 1), a `flag` variable in the
          outer scope is set to False using the `nonlocal` keyword.
        - After the full traversal, return the flag.

    Time Complexity:  O(n) — each node is visited exactly once.
    Space Complexity: O(h) — where h is the height of the tree (call stack).

    Args:
        root (treeNode): The root node of the binary tree.

    Returns:
        bool: True if the tree is balanced, False otherwise.
    """
    if not root:
        return True  # An empty tree is trivially balanced

    flag = True  # Assume balanced until proven otherwise

    def height(node):
        """
        Recursively computes the height of a subtree rooted at `node`.
        As a side effect, sets `flag = False` if any subtree is unbalanced.

        Args:
            node (treeNode): Current node being evaluated.

        Returns:
            int: Height of the subtree (0 if node is None).
        """
        nonlocal flag  # Must be declared before any use inside this scope

        if not node:
            return 0  # Base case: null node has height 0

        left = height(node.left)    # Recursively get height of left subtree
        right = height(node.right)  # Recursively get height of right subtree

        # Check balance condition at the current node
        if abs(left - right) > 1:
            flag = False  # This node violates the balance property

        return max(left, right) + 1  # Height = tallest subtree + 1 for current node

    height(root)  # Kick off the traversal from the root

    return flag  # True if all nodes were balanced, False if any was not


def main():
    """
    Builds a sample binary tree and tests the isBalanced function.

    Tree structure:
            1
           / \\
          2   3
         / \\
        4   5

    This tree is balanced because:
      - Node 1: left height = 2, right height = 1 → diff = 1 ✓
      - Node 2: left height = 1, right height = 1 → diff = 0 ✓
      - Leaf nodes (3, 4, 5): height = 0 on both sides → diff = 0 ✓
    Expected output: True
    """
    root = treeNode(1)
    root.left = treeNode(2)
    root.right = treeNode(3)
    root.left.left = treeNode(4)
    root.left.right = treeNode(5)

    print(isBalanced(root))  # Output: True


if __name__ == "__main__":
    main()
