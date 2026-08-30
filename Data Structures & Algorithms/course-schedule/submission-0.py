# Approach: Recursive DFS - Directed Cycle Detection
# 1) Build a directed adjacency list from prerequisites.
#    For [course, preReq], edge is preReq -> course.
#
# 2) Use two sets:
#    visited = courses that are fully processed and proven safe
#    path = courses currently being explored in the current DFS path
#
# 3) If a course is already in path:
#    -> we came back to a course in the current DFS path
#    -> cycle found
#    -> cannot finish all courses
#
# 4) If a course is already in visited:
#    -> this course was already fully processed earlier
#    -> no cycle from this course
#    -> safe to return True
#
# 5) Otherwise:
#    -> add course to current path
#    -> DFS all courses that depend on it
#
# 6) If any neighbor detects a cycle:
#    -> propagate False upward
#
# 7) Once all neighbors are safely processed:
#    -> remove course from current path
#    -> add course to visited
#
# 8) Start DFS from every course because the directed graph
#    can have disconnected components.
#
# Time: O(V + E)
# Space: O(V + E) for adjacency list + O(V) recursion/sets

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Build directed adjacency list
        # preReq -> courses that depend on it
        graph = [[] for _ in range(numCourses)]

        for course, preReq in prerequisites:
            graph[preReq].append(course)

        # Permanently processed / already proven safe
        visited = set()

        # Temporarily processing in current DFS recursion path
        path = set()

        # Helper function - detect cycle in directed graph
        def dfs(course):

            # If course is already in current DFS path,
            # we found a back edge -> cycle
            if course in path:
                return False

            # If course was already completely processed,
            # it is already proven safe
            if course in visited:
                return True

            # Mark course as currently being explored
            path.add(course)

            # Explore all neighboring courses
            for neighbor in graph[course]:

                # If any neighbor leads to a cycle,
                # propagate False upward
                if not dfs(neighbor):
                    return False

            # Done exploring this course in current path
            path.remove(course)

            # Mark course as completely processed / safe
            visited.add(course)

            return True

        # Start DFS from every course because
        # the graph can have disconnected components
        for course in range(numCourses):
            if not dfs(course):
                return False

        # No cycle found anywhere
        return True