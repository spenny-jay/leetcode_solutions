# LINK: https://leetcode.com/problems/max-area-of-island/description/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


        def bfs(r, c):
            # we call this function when we run into an island coordinate,
            # thus we start with an area of 1 and populated our data structures
            area = 1
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                (currRow, currCol) = queue.popleft()
                # check all 4 adjacent cells to see if we should traverse there
                for (dr, dc) in directions:
                    nr, nc = currRow + dr, currCol + dc
                    if nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr, nc))
                        area += 1
                        queue.append((nr, nc))
            return area
                

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(bfs(r, c), maxArea)

        
        return maxArea
        