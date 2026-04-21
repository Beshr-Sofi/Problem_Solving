class treeNode:
    """Represents a single node in a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # Value stored in this node
        self.left = left     # Pointer to the left child
        self.right = right   # Pointer to the right child


# ─────────────────────────────────────────────────────────────
# Approach 1 — DFS with a nonlocal flag (iterative-style DFS)
# ─────────────────────────────────────────────────────────────

def isSubTree(root, subRoot):
    """
    Checks whether `subRoot` is a subtree of `root` using DFS + exact-match helper.

    Strategy:
        1. `helper(p, q)` — recursively checks if two trees are exactly identical
           (same structure and same values at every node).
        2. `dfs(root)` — traverses the main tree via DFS. Whenever a node whose
           value matches `subRoot.val` is found, `helper` is called to confirm a
           full structural match.
        3. A `nonlocal flag` is used so that once a match is found the DFS stops
           exploring further (`if flag: return` short-circuits all future calls).

    Time Complexity:  O(n * m) — for each of the n nodes in `root`, the helper
                      may compare up to m nodes of `subRoot` in the worst case.
    Space Complexity: O(h) — h is the height of the main tree (recursion stack).

    Args:
        root    (treeNode): Root of the main tree to search within.
        subRoot (treeNode): Root of the tree to find as a subtree.

    Returns:
        bool: True if `subRoot` is a subtree of `root`, False otherwise.
    """

    def helper(p, q):
        """Returns True if the trees rooted at p and q are exactly identical."""
        if not p and not q:
            return True                      # Both empty → match
        if not p or not q or q.val != p.val:
            return False                     # One empty or values differ → no match
        # Recurse on both children — both sides must match
        return helper(p.left, q.left) and helper(p.right, q.right)

    flag = False  # Will be set to True as soon as a matching subtree is found

    def dfs(root):
        nonlocal flag
        if not root or flag:  # Stop if tree is exhausted or match already found
            return
        if root.val == subRoot.val:
            flag = helper(root, subRoot)  # Candidate node found — verify full match
        dfs(root.left)   # Explore left subtree
        dfs(root.right)  # Explore right subtree

    dfs(root)
    return flag


# ─────────────────────────────────────────────────────────────
# Approach 2 — Clean recursion (no nonlocal flag)
# ─────────────────────────────────────────────────────────────

def isSubtree2(root, subRoot):
    """
    Checks whether `subRoot` is a subtree of `root` using clean recursion.

    Strategy:
        1. `isSameTree(p, q)` — recursively verifies that two trees are identical.
        2. At every node of `root`, first check if the subtree rooted there equals
           `subRoot`. If yes, return True immediately.
        3. Otherwise, recurse into the left and right children of `root`.
           If either side contains `subRoot` as a subtree, return True.

    This approach is cleaner than Approach 1 because it avoids a nonlocal variable
    and expresses the logic in a purely recursive, functional style.

    Time Complexity:  O(n * m) — same worst-case as Approach 1.
    Space Complexity: O(h) — recursion depth equals the height of `root`.

    Args:
        root    (treeNode): Root of the main tree to search within.
        subRoot (treeNode): Root of the tree to find as a subtree.

    Returns:
        bool: True if `subRoot` is a subtree of `root`, False otherwise.
    """

    def isSameTree(p, q):
        """Returns True if trees rooted at p and q are structurally identical."""
        if not p and not q:
            return True                        # Both empty → identical
        if not p or not q or p.val != q.val:
            return False                       # One empty or values differ → not identical
        # Both children must also be identical
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    if not root:
        return False                           # Exhausted the main tree — not found

    if isSameTree(root, subRoot):
        return True                            # Current node is the root of a matching subtree

    # Check if subRoot exists in either the left or right subtree
    return isSubtree2(root.left, subRoot) or isSubtree2(root.right, subRoot)


def main():
    """
    Builds two trees and verifies that subRoot is a subtree of root.

    Main tree (root):          Subtree (subRoot):
            3                        4
           / \\                      / \\
          4   5                    1   2
         / \\
        1   2

    subRoot (4 → 1, 2) matches the left subtree of root exactly.
    Expected output:
        True   (isSubtree2)
        True   (isSubTree)
    """
    root = treeNode(3)
    root.left = treeNode(4)
    root.right = treeNode(5)
    root.left.left = treeNode(1)
    root.left.right = treeNode(2)

    subRoot = treeNode(4)
    subRoot.left = treeNode(1)
    subRoot.right = treeNode(2)

    print(isSubtree2(root, subRoot))  # Output: True
    print(isSubTree(root, subRoot))   # Output: True


if __name__ == "__main__":
    main()
