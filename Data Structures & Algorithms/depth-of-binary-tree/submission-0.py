# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive DFS
#Time comp: O(n) where n is number of nodes in tree
#Spcae comp: O(h), O(h) space is O(log n) for a balanced tree and O(n) in the worst case for a skewed tree.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)
        return max(max_left, max_right)+1      #+1 is for root node