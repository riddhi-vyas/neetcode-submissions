# Recursive DFS
#Time comp: O(rows*cols), since I am, visiting each cell of the grid
#Space comp: O(rows*cols),  in the worst case due to the recursion stack for DFS on a grid of size R x C (e.g., a grid full of land). In the best/average case with shallow recursion, additional space aside from the input grid is O(H) where H is maximum depth of the DFS stack
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [ [0, -1], [0, 1], [-1, 0], [1, 0] ] # down, up, left, right
        
        #Helper function
        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0"):
                return
            #otherwise -> mark visited
            grid[r][c] = "0"
            # find neighbors
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                dfs(nr, nc)
        
        #Main loop continues from here - start dfs
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # if encounter a land -> increment count -> dfs neighbr
                    count += 1
                    dfs(r, c)
        return count