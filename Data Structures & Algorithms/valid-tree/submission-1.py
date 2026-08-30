# A tree with n nodes must have exactly n - 1 edges. So if len(edges) != n - 1, you can immediately return False. Then you only need to verify connectivity.
# Recursive DFS - cycle detection with parent tracking
# Idea:
# 1) A valid tree must be connected and contain no cycle.
# 2) Build an undirected adjacency list from edges.
# 3) During DFS, keep track of the parent node.
# 4) If we see the parent again, ignore it because the edge is undirected.
# 5) If we see another already-visited node, we found a cycle.
# 6) After DFS, all n nodes must have been visited.
#Time comp: O(n+m), n are nodes, m are edges
#Space comp: O(n+m)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        #build adjacency list for graph using edges
        graph = [ [] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        #Helper function - returns False if cycle is found
        def dfs(node, parent):
            visited.add(node)
            #explore neighbors
            for neighbor in graph[node]:
                # Ignore the edge we used to reach this node
                if neighbor == parent:
                    continue
                # Already visited through another path -> cycle
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True
        
        #main continues - start from any node - here node 0
        if not dfs(0, -1):
            return False
        # Graph must also be connected
        return len(visited) == n