class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        count_island = 0
        def dfs(i,j):
            if i<0 or i>=n_rows or j<0 or j>=n_cols:
                return

            elif grid[i][j] == "0":
                return
          
            grid[i][j] = "0"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count_island+=1    
                
                else:
                    continue
        return count_island

        
    
    
        
        