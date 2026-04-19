from collections import deque
class treeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Problem: Maximum Depth of Binary Tree
-------------------------------------
Given the `root` of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Complexity Analysis:
--------------------
1. Recursive DFS (maxDepth):
   - Time Complexity: O(n), where `n` is the number of nodes in the tree. We visit every node exactly once.
   - Space Complexity: O(h), where `h` is the height of the tree. This space is used by the call stack 
     during recursion. In the worst case (skewed tree) it's O(n), and in the best case (balanced) it's O(log n).

2. Iterative BFS (maxDepth2):
   - Time Complexity: O(n), as we visit each node exactly once.
   - Space Complexity: O(w), where `w` is the maximum width of the tree. This is the maximum 
     number of nodes in the queue at any level. In the worst case (a full balanced tree), 
     the last level contains roughly n/2 nodes, making it O(n).
"""

def maxDepth(root):
    # Base case: If the current node is None, it contributes 0 to the depth.
    if not root:
        return 0
    # Recursive step: 1 (current node) + the max depth between left and right subtrees.
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def maxDepth2(root):
    # Handle the edge case of an empty tree.
    if not root:
        return 0
        
    level = 0
    # Use a double-ended queue (deque) for O(1) appends and pops from the left.
    queue = deque([root])
    
    # Process nodes level by level.
    while queue:
        # Loop through all nodes present at the current level.
        for i in range(len(queue)):
            # Remove a node from the front of the queue.
            node = queue.popleft()
            
            # If children exist, add them to the queue for the next level's processing.
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        # After processing all nodes of the current level, increment our depth counter.
        level += 1
        
    return level

def main():
    root = treeNode(1)
    root.left = treeNode(2)
    root.right = treeNode(3)
    root.left.left = treeNode(4)
    root.left.right = treeNode(5)

    print(f"maxDepth using recursive DFS: {maxDepth(root)}")
    print(f"maxDepth using iterative BFS: {maxDepth2(root)}")

if __name__ == "__main__":
    main()
