#Time comp: O(V+E), Space comp: O(V+E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #cretae adjacency list to build a graph
        graph = [ [] for _ in range(numCourses)]
        # creating an edge: preReq -> course
        for course, preReq in prerequisites:
            graph[preReq].append(course)
            
        visited = set() #to store the courses already processed
        path = set() #to store courses in out current exploring path

        #Helper DFS - To Detect Cycle
        def dfs(course):
            if course in path:
                return False # visiting same course in current path -> cycle
            if course in visited:
                return True #visiting course already processed -> no cycle
            #otherwise: add the course to path
            path.add(course)
            #explore it's neighbors
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False # cycle detected
            #remove course from path and add to visited
            #because we explored course with neighbores -> no cycle detected
            path.remove(course)
            visited.add(course)
            return True
        
        #calling dfs
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True