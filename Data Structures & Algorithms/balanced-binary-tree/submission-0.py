# This uses the same height calculation as Maximum Depth, with one extra check:
    # At every node, the left and right heights must differ by at most 1.
# Use a DFS helper that returns:
# a) The subtree’s height if it is balanced.
# b) -1 if it is unbalanced. Since a height cannot be negative, this signals failure.
# Time complexity: O(n), where n is the number of nodes in the tree. The dfs visits each node once.
# Space complexity: O(h), where h is the height of the tree, due to the recursion stack. In the worst case (skewed tree), this is O(n); in a balanced tree it is O(log n).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs returns a height or -1.
        # isBalanced returns True or False
        def dfs(root):
            if not root:
                return True
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            
            if left_height == -1 or right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height)+1
            

        #call dfs
        return dfs(root) != -1