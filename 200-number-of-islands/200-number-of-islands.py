class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])

        dp = [[i + j*n for i in range(n)] for j in range(m)]
        
        def find(x,y):
            if dp[x][y] == x*n + y:
                return x*n + y
            else:
                dp[x][y] = find(dp[x][y]//n,dp[x][y]-dp[x][y]//n*n)
            
            return dp[x][y]
        
        def union(p1,p2):
            c1 = find(p1[0],p1[1])
            c2 = find(p2[0],p2[1])
            
            dp[c1//n][c1-c1//n*n] = c2
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    l = (i,j-1)
                    r = (i,j+1)
                    t = (i-1,j)
                    b = (i+1,j)
                    
                    for nx,ny in [l,r,t,b]:
                        if 0 <= nx < m and 0 <= ny<n and grid[nx][ny]=='1':
                            if find(nx,ny) != find(i,j):
                                union([i,j],[nx,ny])
                                
        d = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    d[find(i,j)] = 1
        # print(dp)
        return len(d)