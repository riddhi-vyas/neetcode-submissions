# outer loop explores components
# inner loop (dfs) works on one component
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        graph = [[] for _ in range(n) ]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        # Helper function
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dfs(neighbor)
        #main continues
        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        return components