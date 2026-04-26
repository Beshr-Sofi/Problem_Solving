class TreeNode:
    """Represents a single node in a Binary Tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def robHouseThree(root):
    """
    Solves the "House Robber III" problem.
    
    Problem Statement:
    The neighborhood forms a binary tree. You want to rob the maximum amount 
    of money, but you cannot rob two directly linked houses (i.e., you cannot 
    rob a parent node and its direct child node).
    
    Approach: Dynamic Programming on Trees (Tree DP)
    ------------------------------------------------
    For every node, we have two choices:
    1. Rob this node: If we rob the current node, we CANNOT rob its direct children.
       Our profit will be: node.val + (profit from NOT robbing left child) + 
                                     (profit from NOT robbing right child)
    2. Do NOT rob this node: If we skip the current node, we are free to either rob 
       or not rob its children to maximize our profit.
       Our profit will be: max(robbing left, not robbing left) + 
                           max(robbing right, not robbing right)
                           
    Algorithm:
    We use a recursive `helper` function that returns a tuple for each node:
    (max_profit_if_we_rob_this_node, max_profit_if_we_do_NOT_rob_this_node)
    
    Time Complexity: O(N) - We visit every node exactly once.
    Space Complexity: O(H) - Where H is the height of the tree, representing the 
                      maximum depth of the recursion stack.
    """
    def helper(node):
        # Base case: an empty node yields 0 profit regardless of the choice.
        if not node:
            return 0, 0

        # Recursively get the tuples (robbed, not_robbed) for left and right children.
        left = helper(node.left)
        right = helper(node.right)

        # Choice 1: We ROB the current node. 
        # We must add its value to the profits of NOT robbing its children.
        # left[1] is the profit of not robbing left child.
        # right[1] is the profit of not robbing right child.
        with_root = node.val + left[1] + right[1]

        # Choice 2: We do NOT ROB the current node.
        # We can take the maximum possible profit from the left subtree 
        # (whether we robbed the left child or not) AND the maximum from the right.
        without_root = max(left) + max(right)

        # Return the tuple for the current node
        return with_root, without_root

    # The final answer is the maximum profit we can get at the root node,
    # whether we decided to rob the root itself or not.
    return max(helper(root))
        
def main():
    """
    Example usage demonstrating the House Robber III solution.
    
    Constructed Tree:
             1
            /
           4
          / \\
         2   3
        /
       3
       
    Possible choices:
    - Rob (1) and (2, 3), but wait, 2 has a child 3.
    - Optimal: Rob (4) -> gives 4. Rob the bottom-most (3) -> gives 3. Total = 7.
      (We cannot rob 4 and 2 or 3, but we can rob 4 and the left-most 3 because 
       it's not directly connected to 4).
    
    Expected output: 7
    """
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(3)
    
    print(robHouseThree(root))

if __name__ == "__main__":
    main()
