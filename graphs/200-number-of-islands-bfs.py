class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            # all possible moves from current position
            # each coordinate offers 4 options to traverse to
            directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            while q:
                currRow, currCol = q.popleft()
                # check if each possible direction is valid at current coordinate
                for dr, dc in directions:
                    nextRow, nextCol = dr + currRow, dc + currCol
                    # if coordinate is in range, is an island, and has yet to be visisted...
                    if nextRow in range(ROWS) and nextCol in range(COLS) and grid[nextRow][nextCol] == "1" 
                        and (nextRow, nextCol) not in visited:
                            visited.add((nextRow, nextCol))
                            q.append((nextRow, nextCol))

       
        # keep track of the coordinates we have traversed so far
        visited = set()
        islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                # check if the coordinate is an island an somewhere we have not yet visisted
                if (row, col) not in visited and grid[row][col] == "1":
                    islands += 1 + bfs(row, col)

        return islands
