class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        n_rows,n_cols = len(grid), len(grid[0])
        visited = set()

        def dfs(i,j,d):
            #start from treasure chest locations and work upwards
            print(i,j,d)
            if i < 0 or i >= n_rows or j < 0 or j >= n_cols or grid[i][j] == -1:
                return
            
            elif grid[i][j] == 0 and d > 0:
                return
            
            elif grid[i][j] < d:
                return
            
            grid[i][j] = min(grid[i][j],d)
            for dx,dy in directions:
                nr,nc = i+dx,j+dy
                dfs(nr,nc,d+1)
        
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 0:
                    dfs(i,j,0)

