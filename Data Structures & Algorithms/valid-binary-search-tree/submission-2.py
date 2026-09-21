# Time comp: O(n), Space comp: O(h) for recursion and O(n) in a skewed tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Helper function
        def helper(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (helper(node.left, low, node.val) and
                    helper(node.right, node.val, high))
        return helper(root, float('-inf'), float('inf'))