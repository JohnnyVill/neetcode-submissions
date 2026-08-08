class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]
        queue = deque()
        res = 0
        fresh = 0
        rotted = 0
        if rows == 1 and cols == 1 and grid[rows-1][cols-1] == 0:
            return 0
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j]:
                    fresh += 1
        if fresh == 0 and rotted == 0:
            return 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    qr = r + dr
                    qc = c + dc
                    if qr >= rows or qc >= cols or qr < 0 or qc < 0:
                        continue
                    elif grid[qr][qc] == 1:
                        grid[qr][qc] = 2
                        queue.append((qr, qc))
            rotted += len(queue)
            res += 1
        
        return res - 1 if rotted - fresh == 0 else -1
                
