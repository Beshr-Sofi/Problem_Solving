class treeNode:
    """
    Represents a single node in a Binary Tree.
    Each node contains a value (val), and pointers to its left and right children.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    """
    Performs an Inorder Traversal of a Binary Tree.
    Inorder Traversal order: Left Child -> Current Node -> Right Child.
    
    Time Complexity: O(N), where N is the number of nodes in the tree, since we visit every node exactly once.
    Space Complexity: O(H), where H is the height of the tree (due to the recursive call stack).
                      In the worst case (skewed tree), this is O(N). In the best case (balanced tree), it's O(log N).
    """
    nodes = [] # List to store the traversal sequence
    
    def dfs(node):
        # Base case: if the node is None, stop going deeper and return
        if not node:
            return
            
        # 1. Traverse the left subtree recursively
        dfs(node.left)
        
        # 2. Process (visit) the current node
        nodes.append(node.val)
        
        # 3. Traverse the right subtree recursively
        dfs(node.right)
        
    # Start the Depth-First Search recursion from the root
    dfs(root)
    
    return nodes

def main():
    # Constructing the following binary tree:
    #         1
    #       /   \
    #      2     3
    #     / \
    #    4   5
    root = treeNode(1)
    root.left = treeNode(2)
    root.right = treeNode(3)
    root.left.left = treeNode(4)
    root.left.right = treeNode(5)
    
    # Executing Inorder Traversal...
    # Expected output: [4, 2, 5, 1, 3]
    # Because:
    # 1's left is 2. 2's left is 4. 4 has no children, so we print 4.
    # We go back up to 2, print 2, then visit 2's right (5). 5 has no children, print 5.
    # We go back up to 1, print 1, then visit 1's right (3). 3 has no children, print 3.
    print(inorderTraversal(root))

if __name__ == "__main__":
    main()
