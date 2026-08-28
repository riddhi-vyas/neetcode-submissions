# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Approach: Iterative DFS using stack - Inorder Traversal
# In BST, inorder traversal gives values in sorted order
# Time comp: O(h + k), where h is tree height
# Space comp: O(h), for stack
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root or not k:
            return
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop(-1)
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right