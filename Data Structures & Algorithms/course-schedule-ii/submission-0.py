# same as Course Schedule problem, but just track a list to store ordered coruses
#Time and space comp: O(V+E), where V is the number of courses and E is the number of prerequisite pairs.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [ [] for _ in range(numCourses)]
        for course, preReq in prerequisites:
            graph[preReq].append(course)
        
        visited = set()
        path = set()
        order = []

        #Helper dfs - To Detect Cycle + add courses in order to a resulting list
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
            order.append(course) # Add after exploring its neighbors
            return True
        
        #calling dfs
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order[::-1] #reverse order to put prerequisites first