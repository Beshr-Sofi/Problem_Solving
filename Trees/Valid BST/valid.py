class TreeNode:
    """Represents a single node in a Binary Tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # Value stored in this node
        self.left = left     # Left child
        self.right = right   # Right child

def isValidBST(root):
    """
    Determines if a given binary tree is a valid Binary Search Tree (BST).
    
    A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys LESS THAN the node's key.
    - The right subtree of a node contains only nodes with keys GREATER THAN the node's key.
    - Both the left and right subtrees must also be valid binary search trees.
    
    Approach: Recursive DFS with Range Validation
    ---------------------------------------------
    We use a helper function that keeps track of the allowed range (min_val, max_val) 
    for the current node's value. 
    
    1. Base Case: An empty node (None) is a valid BST, so return True.
    2. Validation: If the current node's value falls outside the allowed range 
       (root.val <= min_val or root.val >= max_val), it violates the BST property. Return False.
    3. Recursive Step:
       - For the left child, the max value it can take is updated to the current node's value.
       - For the right child, the min value it can take is updated to the current node's value.
       Both left and right subtrees must be valid, so we use logical AND.
       
    Time Complexity: O(n) - We visit every node exactly once.
    Space Complexity: O(h) - Where h is the height of the tree (due to the recursion stack). 
                             In the worst case (skewed tree), this could be O(n).
    """
    def helper(node, min_val=float('-inf'), max_val=float('inf')):
        # Base case: empty tree is valid
        if not node:
            return True
            
        # Check if the current node's value is within the valid range
        if node.val <= min_val or node.val >= max_val:
            return False
            
        # Recursively check the left and right subtrees with updated bounds
        # Left child must be strictly less than node.val
        # Right child must be strictly greater than node.val
        return (helper(node.left, min_val, node.val) and
                helper(node.right, node.val, max_val))
                
    return helper(root)

def main():
    """
    Example usage demonstrating how to check if a tree is a valid BST.
    
    Constructed Tree:
          5
         / \\
        4   6
           / \\
          3   7
          
    Notice that the node with value 3 is in the right subtree of 5. 
    However, 3 is less than 5, which violates the BST property that all nodes 
    in the right subtree must be greater than the root.
    
    Expected output: False
    """
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    
    print(isValidBST(root))

if __name__ == "__main__":
    main()
