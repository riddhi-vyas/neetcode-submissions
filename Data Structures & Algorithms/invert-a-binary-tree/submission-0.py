# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive DFS
#Time comp: O(n), n is nodes in tree
#Space comp: O(h), h is height of tree. O(h) recursion space means O(log n) for a balanced tree, but O(n) in the worst case for a completely skewed tree.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root