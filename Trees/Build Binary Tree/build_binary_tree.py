class TreeNode:
    """Represents a single node in a Binary Tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    """
    Constructs a Binary Tree from its Preorder and Inorder traversals.
    
    Approach: Recursion and Array Partitioning
    ------------------------------------------
    The properties of tree traversals provide the key to rebuilding the tree:
    1. Preorder Traversal (Root, Left, Right): The first element in the preorder 
       array is always the root of the current (sub)tree.
    2. Inorder Traversal (Left, Root, Right): Once we know the root (from preorder), 
       we can find it in the inorder array. All elements to the left of the root 
       in the inorder array form the left subtree, and all elements to the right 
       form the right subtree.
       
    Algorithm:
    1. Base Case: If either `preorder` or `inorder` is empty, there is no tree 
       to build, so return None.
    2. Identify Root: The first element of `preorder` is the root node. Create it.
    3. Find Split Index: Find the index of this root value in the `inorder` array. 
       Let's call this index `mid`.
       - Elements from `inorder[0]` to `inorder[mid-1]` belong to the left subtree.
       - The number of elements in the left subtree is exactly `mid`.
    4. Partition Arrays & Recurse:
       - Left Subtree: 
         - Preorder: `preorder[1 : mid+1]` (skip the root, take `mid` elements)
         - Inorder: `inorder[:mid]` (everything before the root)
       - Right Subtree:
         - Preorder: `preorder[mid+1:]` (everything after the left subtree elements)
         - Inorder: `inorder[mid+1:]` (everything after the root)
         
    Time Complexity: O(N^2) - In the worst case (skewed tree), finding the index 
                     in `inorder` takes O(N) at each step. This can be optimized 
                     to O(N) by using a hash map to store `inorder` value-to-index mappings.
    Space Complexity: O(N^2) - Due to array slicing creating new lists at each recursive 
                      step. Passing indices instead of slicing would optimize this to O(N).
    """
    # Base case: if traversals are empty, return None
    if not preorder or not inorder:
        return None
    
    # 1. The first element in preorder is always the root
    root = TreeNode(preorder[0])
    
    # 2. Find the root's position in inorder traversal
    mid = inorder.index(preorder[0])
    
    # 3. Recursively build the left and right subtrees
    # preorder[1:mid+1] gives the elements for the left subtree in preorder
    # inorder[:mid] gives the elements for the left subtree in inorder
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    
    # preorder[mid+1:] gives the elements for the right subtree in preorder
    # inorder[mid+1:] gives the elements for the right subtree in inorder
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    
    return root

def print_tree(root):
    """Prints the tree using a Preorder traversal (Root, Left, Right)."""
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

def main():
    """
    Example demonstrating tree construction.
    
    Traversals:
    preorder = [3, 9, 20, 15, 7]
    inorder  = [9, 3, 15, 20, 7]
    
    Constructed Tree:
          3
         / \\
        9   20
           /  \\
          15   7
          
    The print_tree function will output the Preorder traversal, 
    so it should match the input `preorder` list exactly.
    """
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    root = buildTree(preorder, inorder)
    
    # Print the reconstructed tree to verify
    print_tree(root)

if __name__ == "__main__":
    main()
