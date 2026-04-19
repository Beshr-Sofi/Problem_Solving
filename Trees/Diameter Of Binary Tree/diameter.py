class treeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Problem: Diameter of Binary Tree
--------------------------------
Given the `root` of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Complexity Analysis:
--------------------
- Time Complexity: O(n), where `n` is the number of nodes in the tree. The DFS function visits every node exactly once.
- Space Complexity: O(h), where `h` is the height of the tree. This space is used by the recursion call stack.
  In the worst case (skewed tree), it's O(n), and in the best case (balanced tree), it's O(log n).
"""
def diameterOfBinaryTree(root):
    # This variable keeps track of the maximum diameter found so far across all subtrees.
    maxi = 0
    
    def dfs(node):
        # Base case: an empty node has a height/depth of 0.
        if not node:
            return 0
            
        # Recursively find the maximum depth of the left and right subtrees.
        left = dfs(node.left)
        right = dfs(node.right)

        # Use nonlocal to modify the `maxi` variable defined in the outer scope.
        nonlocal maxi
        
        # The diameter passing through the current node is the sum of the depths of its left and right subtrees (left + right edges).
        # We update our global maximum diameter if this local diameter is larger.
        maxi = max(maxi, left + right)

        # Return the depth/height of the tree rooted at the current node.
        # It's 1 (for the current node's edge to its parent) + the max depth of its children.
        return 1 + max(left, right)
    
    # Kick off the DFS traversal starting from the root.
    dfs(root)
    
    # Return the maximum diameter that was recorded during the traversal.
    return maxi

def main():
    root = treeNode(1)
    root.left = treeNode(2)
    root.right = treeNode(3)
    root.left.left = treeNode(4)
    root.left.right = treeNode(5)

    print(f"Diameter of binary tree: {diameterOfBinaryTree(root)}")

if __name__ == "__main__":
    main()
