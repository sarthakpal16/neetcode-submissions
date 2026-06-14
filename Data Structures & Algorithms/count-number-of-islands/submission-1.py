class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        n_rows = len(grid)
        n_cols = len(grid[0])
        count_island = 0
        def bfs(i,j):
            q = deque()
            grid[i][j] == "0"
            q.append((i,j))

            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if nr<0 or nr>=n_rows or nc<0 or nc>=n_cols or grid[nr][nc]=="0":
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"


        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == "1":
                    bfs(i,j)
                    count_island+=1    
                
                else:
                    continue
        return count_island

        
    
    
        
        