# Similar problem hints - longest path between any two nodes”, especially when the path doesn’t have to pass through the root.
#Approach:
# Get the left and right heights.
# Combine both to check the longest path through this node.
# Return only the taller side + 1 to its parent.
#Time comp: O(n), Space comp: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            # Longest path passing through this node
            diameter = max(diameter,left_height + right_height)

            return max(left_height, right_height)+1
        
        #call helper dfs
        dfs(root)
        return diameter