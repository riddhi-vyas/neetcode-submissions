# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive DFS - Using helper function of Same Tree
#Time comp: O(m * n), where m = nodes in root, n = nodes in subRoot
#Space comp: O(h), due to recursive call stack
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Helper function - checks if two trees are exactly same
        def isSametree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return (isSametree(p.left, q.left) and isSametree(p.right, q.right))
        #isSubtree execution starts from here..
        if not subRoot:
            return True
        if not root:
            return False
        return (isSametree(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))