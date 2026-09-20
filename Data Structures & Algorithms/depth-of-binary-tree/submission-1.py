#Recursive DFS: Depth = 1 + max(left depth, right depth). Recurse on both children; the None base case returns 0, so no child-existence checks are needed.
# Time comp: O(n). Space comp: O(h) for recursion.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth)+1 # adding 1 for the root node