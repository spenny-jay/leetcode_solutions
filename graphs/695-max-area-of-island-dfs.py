# LINK: https://leetcode.com/problems/max-area-of-island/description/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        # used to prevent revisited already traversed islands
        visited = set()

        def dfs(r, c):
            area = 0
            # check OOB and whether the coordinate is an unvisited island point
            if r in range(ROWS) and c in range(COLS) and (r, c) not in visited and grid[r][c] == 1:
                visited.add((r, c))
                # add results of adjacent coordinates
                area = 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
                return area

            return 0
                

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(dfs(r, c), maxArea)

        
        return maxArea
        