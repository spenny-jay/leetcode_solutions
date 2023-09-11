class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(row, col):
            # confirm if the row and col are inbounds
            rowBounds = row >= 0 and row < ROWS
            colBounds = col >= 0 and col < COLS
            # also check if we have already traversed in this direction
            # and check if we are still traversing an island
            if rowBounds and colBounds and (row, col) not in visited and grid[row][col] == "1":
                # track where we have progressed
                visited.add((row, col))
                # navigate in all directions for adjacent island coordinates
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
                return 1
            return 0
       
        # track which coordinates we have visited
        visited = set()
        islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                # if we have not visited this coordinate and it belongs to an island...
                if (row, col) not in visited and grid[row][col] == "1":
                    islands += dfs(row, col)

        return islands
