class TreeNode:
    """Represents a single node in a Binary Search Tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # Value stored in this node
        self.left = left     # Left child
        self.right = right   # Right child

def kthSmallest(root, k):
    """
    Finds the k-th smallest element in a Binary Search Tree (BST) iteratively.
    
    Approach: Iterative In-order Traversal
    --------------------------------------
    An in-order traversal (Left, Root, Right) of a BST visits the nodes in 
    ascending sorted order. We can use a stack to simulate the recursion of an 
    in-order traversal.
    
    1. Start at the root and go as far left as possible, pushing each node onto 
       a stack. The left-most node is the smallest element.
    2. Pop a node from the stack. This is the next smallest element in the traversal.
    3. Increment a counter `n`. If `n` equals `k`, we've found the k-th smallest 
       element, so return its value.
    4. Move to the popped node's right child and repeat the process.
    
    Time Complexity: O(H + k) - Where H is the height of the tree. We go down to the 
                     leaves (O(H)) and then process k nodes.
    Space Complexity: O(H) - The stack will hold at most H nodes at any given time.
    """
    n = 0
    stack = []
    curr = root
    
    # Loop as long as there are nodes to process or nodes in the stack
    while curr or stack:
        # Traverse as far left as possible
        while curr:
            stack.append(curr)
            curr = curr.left
            
        # Process the node at the top of the stack
        curr = stack.pop()
        n += 1
        
        # Check if we found the k-th smallest element
        if n == k:
            return curr.val
            
        # Move to the right subtree
        curr = curr.right

def kthSmallest_recursive(root, k):
    """
    Finds the k-th smallest element in a Binary Search Tree (BST) recursively.
    
    Approach: Recursive In-order Traversal
    --------------------------------------
    Similar to the iterative approach, this uses an in-order traversal but 
    relies on recursion. It uses non-local variables to keep track of the 
    result and the remaining count across recursive calls.
    
    1. Recursively traverse the left subtree.
    2. Decrement the `counter`. If `counter` reaches 0, the current node is 
       the k-th smallest. Save its value in `res` and return early.
    3. If the k-th smallest hasn't been found, recursively traverse the right subtree.
    
    Time Complexity: O(N) - In the worst case, we might visit all N nodes. However, 
                     the traversal stops effectively updating `res` once k is reached.
    Space Complexity: O(H) - Where H is the height of the tree, due to the recursion stack.
    """
    res = 0
    counter = k
    
    def dfs(node):
        nonlocal res, counter
        
        # Base case: reached a leaf
        if node is None:
            return
            
        # Traverse left subtree
        dfs(node.left)
        
        # Process current node
        counter -= 1
        if counter == 0:
            res = node.val
            return  # Found the target, no need to go deeper on the right
            
        # Traverse right subtree
        dfs(node.right)
        
    dfs(root)
    return res

def main():
    """
    Example usage demonstrating how to find the k-th smallest element.
    
    Constructed BST:
             5
           /   \\
          3     6
         / \\
        2   4
       /
      1
      
    In-order traversal: [1, 2, 3, 4, 5, 6]
    For k = 3, the 3rd smallest element is 3.
    """
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    
    print(kthSmallest_recursive(root, 3))

if __name__ == "__main__":
    main()
