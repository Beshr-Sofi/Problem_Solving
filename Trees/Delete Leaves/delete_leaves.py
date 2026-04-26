class TreeNode:
    """Represents a single node in a Binary Tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def removeLeafNodes(root, target):
    """
    Removes all leaf nodes in a binary tree that have a specific target value.
    If removing a leaf node causes its parent to become a leaf node with the 
    target value, that parent should also be removed.
    
    Approach: Post-order Traversal (Bottom-Up)
    ------------------------------------------
    Because removing a child node might turn its parent into a new leaf node, 
    we MUST process the children before we process the parent. This perfectly 
    aligns with a Post-order Traversal (Left, Right, Root).
    
    Algorithm:
    1. Base Case: If the current node is None, return None.
    2. Recursion (Left & Right): 
       - Recursively call the function on the left child and update `root.left`.
       - Recursively call the function on the right child and update `root.right`.
       This step ensures that all descendants are processed first, and any 
       removals "bubble up" from the bottom of the tree.
    3. Process Current Node:
       - Check if the current node is now a leaf node (`not root.left and not root.right`).
       - If it is a leaf AND its value equals the `target`, it needs to be removed.
       - To remove it, we simply return `None` to its parent.
    4. If the node shouldn't be removed, return the `root` itself to maintain the link.
    
    Time Complexity: O(N) - Every node in the tree is visited exactly once.
    Space Complexity: O(H) - Where H is the height of the tree. This is the space 
                      used by the recursion stack.
    """
    # 1. Base Case
    if not root:
        return None
    
    # 2. Process children first (Bottom-Up approach)
    root.left = removeLeafNodes(root.left, target)
    root.right = removeLeafNodes(root.right, target)
    
    # 3. After children are processed, check if the current node 
    #    has become a leaf node and matches the target.
    if root.val == target and not root.left and not root.right:
        # Returning None deletes this node from its parent
        return None
        
    # 4. Return the node itself if it's not deleted
    return root
    
def printTree(root):
    """Prints the tree using a Preorder traversal (Root, Left, Right)."""
    if not root:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

def main():
    """
    Example usage demonstrating the removal of leaf nodes.
    
    Initial Tree (Target = 2):
              1
            /   \\
           2     3
          / \\   / \\
         2   4 2   2
         
    Step-by-step removal (Bottom-up):
    - The bottom leaves with value 2 (leftmost 2, and the two 2s under 3) are removed.
    - After removing the bottom leaves, the tree looks like this:
              1
            /   \\
           2     3
            \\
             4
    - Now we check the parent nodes. The '2' on the left is NOT a leaf (it has child '4'), 
      so it is kept. The '3' on the right is a leaf, but its value isn't 2, so it's kept.
      
    Final Tree structure:
              1
            /   \\
           2     3
            \\
             4
             
    Preorder print output: 1 -> 2 -> 4 -> 3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(2)
    
    # Remove all leaf nodes with value 2, then print the result
    root = removeLeafNodes(root, 2)
    printTree(root)

if __name__ == "__main__":
    main()
