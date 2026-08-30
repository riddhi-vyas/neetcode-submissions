# Directed cycle DFS (Recursive approach)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #directed adjacency list for graph using prerequisites
        graph = [ [] for _ in range(numCourses) ]
        for course, preReq in prerequisites:
            graph[preReq].append(course)
        
        visited = set()
        path = set()

        #Helper function - to detect cycle in directed graph
        def dfs(course):
            if course in path:
                return False #cycle detected
            
            if course in visited:
                return True
            
            path.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            path.remove(course)
            visited.add(course)
            
            return True
        # main continues - dfs starts
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True 