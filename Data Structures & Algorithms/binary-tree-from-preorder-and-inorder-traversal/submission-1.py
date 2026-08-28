# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Approach: Recursive DFS - Create helper function to split in left subtree and right subtree
# Preorder: Root-Left-Right
# Inorder: Left-Root-Right
# Time comp: O(n), where n is the number of nodes
# Space comp: O(n), for hashmap + recursion stack
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        #step - create hashmap for inorder
        in_map = {}
        for i in range(len(inorder)):
            in_map[inorder[i]] = i
        return self.splitTree(preorder, in_map, 0, 0, len(inorder)-1)
    
    #Helper function
    def splitTree(self, preorder, in_map, pre_idx, in_left, in_right):
        #step - create a root node using pre_idx
        root = TreeNode(preorder[pre_idx])

        #step - find mid and split tree into left and right subtree
        mid = in_map[preorder[pre_idx]] #inorder follows: Left-Root-Right (mid = root)
        #Left subtree if exists
        if mid > in_left:
            root.left = self.splitTree(preorder, in_map, (pre_idx+1), in_left, mid-1)
        #Right subtree if exists
        if mid < in_right:
            root.right = self.splitTree(
                preorder, 
                in_map, 
                pre_idx+mid-in_left+1,  #mid - in_left = left_subtree_size
                mid+1, 
                in_right)
        return root