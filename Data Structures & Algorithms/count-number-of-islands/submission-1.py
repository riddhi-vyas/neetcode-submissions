# Iterative BFS using queue
# Time comp: O(rows*cols), since I am visiting each cell from grid
# Space comp: O(rows*cols), in the worst case due to the BFS queue storing numerous cells in a large island; plus the grid itself, which is modified in place. If we disregard the input grid, the auxiliary space is O(min(R*C, max(R, C))) in typical BFS usage, but in the worst-case (a single large island), the queue can hold up to O(R*C) elements.

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [ [-1, 0], [1, 0], [0, -1], [0, 1] ] # left, right, down, up

        #Helper function
        def bfs(r, c):
        #Initialize q -> mark visited -> pop -> check neighbors -> mark neibr visited -> push
            q = deque([(r, c)])
            grid[r][c] = "0"
            while q:
                row, col = q.popleft() #O(1)
                #explore neighbors
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == "1"):
                        # mark this neighbor as visited -> push to queue
                        grid[nr][nc] = "0"
                        q.append((nr,nc))
        #Main loop continues - start bfs
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        return count