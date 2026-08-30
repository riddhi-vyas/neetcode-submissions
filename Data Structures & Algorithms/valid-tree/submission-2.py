# Approach: Iterative BFS
# 1) A valid tree must be connected and contain no cycle.
# 2) Build an undirected adjacency list.
# 3) Queue stores (node, parent).
# 4) Ignore the parent edge.
# 5) If another neighbor is already visited, a cycle exists.
# 6) Finally check that every node was reached.
#Time comp: O(n+m), n are nodes, m are edges
#Space comp: O(n+m)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        graph = [ [] for _ in range(n) ]
        for u, v, in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = {0}

        q = deque([(0, -1)]) #q stores node and parent
        while q:
            node, parent = q.popleft()
            #explore neighbors of node
            for neighbor in graph[node]:
                # Undirected edge back to parent is expected
                if neighbor == parent:
                    continue
                # Already reached from another path -> cycle
                if neighbor in visited:
                    return False
                visited.add(neighbor) #otherwise add to visited
                q.append((neighbor, node))
            
        #main continues
        # Must also be connected
        return len(visited)==n