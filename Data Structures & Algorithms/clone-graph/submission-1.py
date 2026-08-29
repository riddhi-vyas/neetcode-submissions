#Iterative BFS using queue -> check leetcode
#Time comp: O(V+E)
#Space comp: O(V)
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
        clone_map = {}
        clone_map[node] = Node(node.val)

        q = deque([node])
        while q:
            current = q.popleft()

            for neighbor in current.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                clone_map[current].neighbors.append(clone_map[neighbor])
        return clone_map[node]