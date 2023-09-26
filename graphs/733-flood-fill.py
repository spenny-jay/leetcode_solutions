# LINK: https://leetcode.com/problems/flood-fill/description/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initColor = image[sr][sc]
        # avoid an infinite loop if the initColor is the same as the color
        # since we do not keep track the coordinates we have visited
        if initColor == color: return image
        ROWS = len(image)
        COLS = len(image[0])

        def dfs(r, c):
            # Check for OOB and whether the coordinates point to a value 
            # in need of updating
            if r in range(ROWS) and c in range(COLS) and initColor == image[r][c]:
                image[r][c] = color
                # check adjacent squares
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)


        dfs(sr, sc)
        return image