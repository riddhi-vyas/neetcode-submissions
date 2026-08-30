# Kahn's BFS / Topological Sort
# 1) Build a directed graph from prerequisites.
#    For [course, preReq], edge is preReq -> course.
#
# 2) indegree[course] = number of prerequisites still required for that course.
#
# 3) Add all courses with indegree 0 to the queue
#    because they can be taken immediately.
#
# 4) While queue is not empty:
#    -> take one course
#    -> increment processed count
#    -> reduce indegree of all courses depending on it
#
# 5) If a neighbor's indegree becomes 0:
#    -> all its prerequisites are completed
#    -> add it to queue
#
# 6) At the end:
#    processed == numCourses -> no cycle -> can finish all courses
#    processed < numCourses  -> cycle exists -> cannot finish
#
# Time: O(V + E)
# Space: O(V + E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build directed adjacency list for graph using prerequisites
        # create indegree list initialized each value to 0
        graph = [ [] for _ in range(numCourses) ]
        indegree = [0] * numCourses
        for course, preReq in prerequisites:
            graph[preReq].append(course)
            indegree[course] += 1
        
        q = deque()
        # add all courses with no prerequisites to q == courses with indegree 0
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        processed = 0
        while q:
            course = q.popleft()
            processed += 1

            for neighbor in graph[course]:
                # one prerequisite is now completed
                indegree[neighbor] -= 1

                # if indegree becomes 0, push that neighbor to q
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        # Final check
        if processed == numCourses:
            return True      # no cycle / valid ordering
        if processed < numCourses:
            return False     # cycle exists