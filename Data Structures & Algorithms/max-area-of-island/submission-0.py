class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        n_rows = len(grid)
        n_cols = len(grid[0])
        max_area = 0

        def bfs(i,j):
            q = deque()
            grid[i][j] = 0
            q.append((i,j))
            area=1
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if nr<0 or nr>=n_rows or nc<0 or nc>=n_cols or grid[nr][nc]==0:
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 0
                    area+=1
            return area

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    area = bfs(i,j)
                    max_area = max(area,max_area)
                
                else:
                    continue
        return max_area