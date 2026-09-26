class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [ [] for _ in range(numCourses)]
        for course, preReq in prerequisites:
            graph[preReq].append(course)
        visited = set()
        path = set()

        #heper dfs - to detect cycle in graph
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            path.remove(course)
            visited.add(course)
            return True
        
        #calling dfs
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True