#Logic builds directly on Maximum Depth problem:
    #1) Return to the parent: 1 + max(left_depth, right_depth)—a single branch the parent can extend.
    #2) Check for diameter: left_depth + right_depth—the path connecting both branches through this node.
#In short, Postorder DFS: update diameter with left depth + right depth at every node. Return 1 + max(left depth, right depth) to the parent—return height, track diameter separately.
#Time comp: O(n), Space comp: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        #helper
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            #Longest path passing through this node
            diameter = max(diameter, left+right)

            #return this node's height = 1 + the taller child's height
            return max(left, right)+1
        #call helper
        dfs(root)
        return diameter