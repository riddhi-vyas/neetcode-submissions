# Recursive DFS
# Reverse traversal - I will start from the borders for these 2 oceans while maintaining-
# -invariant: curr_cell_height >= prev_cell_height
#Time comp: O(m*n), m is rows, n is cols
#Space comp: O(m*n)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows = len(heights)
        cols = len(heights[0])
        pacific_set = set()
        atlantic_set = set()
        directions = [ [0, -1], [0, 1], [-1, 0], [1, 0] ] #up, down, left, right

        #Helper function
        def dfs(r, c, visited, prev_height):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                heights[r][c] < prev_height): # invariant
                return
            #otherwise
            visited.add((r, c))

            # dfs on neighbors
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, visited, heights[r][c]) #heights[r][c] = current_cell_height

        # step - start calling dfs
        # Top row -> Pacific
        # Bottom row -> Atlantic
        for c in range(cols):
            dfs(0, c, pacific_set, heights[0][c]) #top row
            dfs(rows-1, c, atlantic_set, heights[rows-1][c]) #bottom row

        # Left col - Pacific
        # Right col - Atlantic
        for r in range(rows):
            dfs(r, 0, pacific_set, heights[r][0]) #left col
            dfs(r, cols-1, atlantic_set, heights[r][cols-1]) #right col

        # At this point, I will have my visited sets ready for both oceans
        # Final step - create a list of (r, c) that appears in both sets
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_set and (r, c) in atlantic_set:
                    result.append([r, c])
        return result