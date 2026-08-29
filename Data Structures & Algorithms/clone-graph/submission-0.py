#Understanding: given input is node (starting point): node: (val, [neighbors])
# adjacency list-> node: [list_of_neighbors], where index of neighbors list starts from 1 and also node values starting from 1
# ex: i/p: adjList = [[2],[1,3],[2]]
# it will be like:   [ 1: [2],
            #          2: [1, 3],
            #          3: [2]    ]
#Imp: I’m given a "reference to one node" in a connected graph, and I can traverse the rest of the graph through each node’s neighbors list

#Recursive DFS:
        # Instead of visited set, I need to use a hash map: original Node -> cloned Node
        # 1. If node is None → return None
        # 2. If node already exists in clone_map → return its clone
        # 3. Create a new Node(node.val)
        # 4. Store clone_map[node] = clone
        # 5. For every neighbor:
        #         cloned_neighbor = dfs(neighbor)
        #         clone.neighbors.append(cloned_neighbor)
        # 6. Return clone
# Time: O(V + E)
# Space: O(V)
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone_map = {} # original node -> cloned node

        #Helper function to create clone graph
        def dfs(current):
            if current in clone_map:
                return clone_map[current]
            #otherwise
            copy = Node(current.val) #creating copy if current node
            clone_map[current] = copy #store in clone_map-> current: copy

            #clone all neighbors of current
            for neighbor in current.neighbors:
                cloned_neighbor = dfs(neighbor)
                copy.neighbors.append(cloned_neighbor)
            return copy
        
        #main continues - start dfs from given starting point -> node
        return dfs(node)