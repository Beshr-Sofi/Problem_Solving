class treeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    """
    Inverts a binary tree by swapping the left and right children of all nodes.
    This essentially produces a mirror image of the original tree.
    
    Time Complexity: O(N) - N is the number of nodes, as we visit every node once.
    Space Complexity: O(H) - H is the height of the tree, representing the recursion stack depth.
    """
    if not root:
        return None
    
    # Recursively swap the left and right children for the current node
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

def inorderTraversal(root):
    """
    Traverses the tree to collect its node values.
    
    Note: The logic here actually implements a Pre-order Traversal (Root, Left, Right) 
    instead of an In-order Traversal (Left, Root, Right), since the node's value is 
    appended to the list before visiting its children.
    
    Time Complexity: O(N) - We visit every node exactly once.
    Space Complexity: O(N) - Space used by the output array and the recursion stack.
    """
    nodes = []
    def dfs(node):
        if not node:
            return
        # Appending before left/right calls makes this a Pre-order traversal
        nodes.append(node.val) 
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return nodes

def main():
    root = treeNode(1)
    root.left = treeNode(2)
    root.right = treeNode(3)
    root.left.left = treeNode(4)
    root.left.right = treeNode(5)

    print(inorderTraversal(root))
    print(inorderTraversal(invertTree(root)))

if __name__ == "__main__":
    main()
