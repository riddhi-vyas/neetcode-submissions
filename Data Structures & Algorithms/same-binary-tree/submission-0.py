# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive DFS
#Time comp: O(n), where n is the number of nodes compared
#Space comp: O(h), where h is the height of the trees due to recursion stack. In the worst case of a completely unbalanced tree, this is O(n); in a balanced tree, it is O(log n).
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))