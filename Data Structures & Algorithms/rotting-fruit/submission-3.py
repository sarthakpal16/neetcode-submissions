class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows,n_cols = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        n_rotten = 0
        n_fresh = 0
        q = deque()
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    n_fresh+=1
                
                elif grid[r][c] == 2:
                    n_rotten+=1
                    q.append((r,c,0))
                
        # print(n_fresh,n_rotten)

        t=0
        iteration = 0
        visited = set()
        infected = 0
        while q and iteration<=100:
            print(q,visited)
            r,c,l = q.popleft()
            print("popped: ",r,c,l)
            if(r,c) in visited:
                continue
            infected+=1
            t = max(t,l)
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if nr<0 or nr>=n_rows or nc<0 or nc>=n_cols or grid[nr][nc]!=1 or (nr,nc) in visited:
                    continue

                q.append((nr,nc,l+1))
                
    
            iteration+=1
        # print(t) 
        print(infected,n_fresh)
        if infected-n_rotten != n_fresh:
            return -1
        return t     





        



