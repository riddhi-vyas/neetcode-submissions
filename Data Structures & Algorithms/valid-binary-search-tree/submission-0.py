# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Approach: Recursive DFS - Create a helper function to compare (low, high and current node) to validate BST.
#Time comp: O(n), Space comp: O(h)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Helper function:
        def helper(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (helper(node.left, low, node.val) and
                   helper(node.right, node.val, high))
        
        #calling helper
        return helper(root, float('-inf'), float('inf'))
                
