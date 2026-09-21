# This uses the same height calculation as Maximum Depth, with one extra check:
    # At every node, the left and right heights must differ by at most 1.
# Use a DFS helper that returns:
# a) The subtree’s height if it is balanced.
# b) -1 if it is unbalanced. Since a height cannot be negative, this signals failure.
#Time comp: O(n), n is number of nodes in tree since dfs visits each node.
#Space comp: O(h), h is height of tree due to recursion stack. In worst case(skewed tree), this is O(n); in a balanced tree, it is O(logn).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #helper dfs -> returns a height or -1
        # main function(isBalanced) -> returns True or False
        def dfs(node):
            if not node:
                return True
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if left_height == -1 or right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            #otherwise return max height + 1
            return max(left_height, right_height)+1
        #calling dfs
        return dfs(root) != -1
            