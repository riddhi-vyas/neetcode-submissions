# need two different jobs:
    # isSame checks whether two entire trees match.
    # isSubtree searches for a matching starting node anywhere in the main tree.
#Time comp: O(n × m), where n and m are the two tree sizes.
#Space comp: O(h) recursive stack, where h is the main tree’s height


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True # empty tree can be a subtree of a tree
        # helper - isSameTree(p, q)
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))
        
        #main contines - call helper
        return (isSameTree(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))