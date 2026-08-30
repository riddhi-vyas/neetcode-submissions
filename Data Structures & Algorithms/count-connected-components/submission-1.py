#Iterative BFS - Outer loop discovers a new component. BFS explores that component.
#Time comp: O(n+m), n are nodes, m are edges
#Space comp: O(n+m)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        # build undirected adjacency list
        graph = [ [] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0

        #Helper function
        def bfs(start):
            q = deque([start])
            visited.add(start)

            while q:
                node = q.popleft()
                #explore neighbors
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                
        #main loop continues - start bfs
        for node in range(n):
            if node not in visited:
                components += 1
                bfs(node)
        return components