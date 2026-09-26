# Preorder + null markers preserves structure. Serialize node, left, right; deserialize by consuming tokens in that same order. # means return None.
# Time comp: O(n), Space comp: O(n) for tokens and up to O(h) for recursion call stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens = []

        #Helper - Preorder DFS (Root-L-R)
        def dfs(node):
            if not node:
                tokens.append('#')
                return
            tokens.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        #calling dfs
        dfs(root)
        return ",".join(tokens)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]: 
        tokens = data.split(',')
        index = 0  #index tracks the next token to read
        #Helper dfs
        def dfs():
            nonlocal index 
            #nonlocal index lets all recursive calls update the same index.


            value = tokens[index]
            index += 1  # Move to the next token

            if value == '#':
                return None
            
            node = TreeNode(int(value))
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()