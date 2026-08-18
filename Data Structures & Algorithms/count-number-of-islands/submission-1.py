class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        col = len(grid[0])

        directions = [
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        ]
        islands = 0
        
        def dfs(r,c):
            if r >= rows or r < 0 or c >= col or c < 0:
                return
            
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'

            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i,j)
        return islands
            