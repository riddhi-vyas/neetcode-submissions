# Time comp: O(n), where n is the number of nodes in the tree. The function visits each node once.
# Space comp: O(h), where h is the height of the tree, due to the recursion stack. In the worst case of a completely unbalanced tree, this can be O(n); for a balanced tree, O(log n).
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
        return max(left_depth, right_depth)+1 # adding 1 for root node
    