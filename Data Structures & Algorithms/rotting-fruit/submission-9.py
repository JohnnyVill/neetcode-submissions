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
        #if no left over fresh fruit they have all rotted
        fresh = 0 
        #bfs for rotting waves
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        time_elapsed = -1
        while queue:
            for _ in range(len(queue)):
                qr,qc = queue.popleft()
                for dr, dc in directions:
                    r = dr + qr
                    c = dc + qc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append([r,c])
            time_elapsed += 1
        return time_elapsed if fresh == 0 else -1
        