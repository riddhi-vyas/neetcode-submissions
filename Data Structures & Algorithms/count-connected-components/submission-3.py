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
        #Helper function
        def bfs(start):
            q = deque([start])
            visited.add(start)
            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        #main continues
        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                bfs(node)
        return components