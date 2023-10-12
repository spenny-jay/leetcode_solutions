class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS = len(mat)
        COLS = len(mat[0])
        MAX_VAL = ROWS * COLS
        queue = deque()
        # collect all 0's in list, set 1's to the MAX_VAL
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = MAX_VAL

        while queue:
            # coordinates of a zero location
            r, c = queue.popleft()
            # check each adjacent cell for a 1 value
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # check for OOB and if the current path is less
                # than the value of the next cell
                if nr in range(ROWS) and nc in range(COLS) and mat[r][c] + 1 < mat[nr][nc]:
                    # continue path and update next cell's value
                    queue.append((nr, nc))
                    # AKA current path + the current cell (1)
                    mat[nr][nc] = mat[r][c] + 1
        

        return mat