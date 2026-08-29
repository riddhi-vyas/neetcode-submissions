#Recursive DFS
#Pattern - OUTER LOOP discovers components.
#        - DFS explores one component.
#Time comp: O(m+n), n is number of nodes and m is the number of edges.
#Space comp: O(m+n)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        component = 0

        #Helper function
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        #main continues - start dfs
        for node in range(n):
            if node not in visited:
                component += 1
                dfs(node)
        return component