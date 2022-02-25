class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        
        parent = [[(i,j) for j in range(n)] for i in range(m)]
        
        
        def find(i,j):
            ci = i
            cj = j
            
            while parent[i][j] != (i,j):
                (i,j) = parent[i][j]
            
            parent[ci][cj] = (i,j)
            return (i,j)
        
        def union(i1,j1,i2,j2):
            ci1 = i1 
            cj1 = j1
            ci2 = i2 
            cj2 = j2
            
            pi1,pj1 = find(i1,j1)
            pi2,pj2 = find(i2,j2)
            
            parent[pi2][pj2] = (pi1,pj1)
            parent[ci1][cj1] = (pi1,pj1)
            parent[ci2][cj2] = (pi1,pj1)
            
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    l = [i,j-1]
                    r = [i,j+1]
                    t = [i-1,j]
                    b = [i+1,j]
                    
                    for ni,nj in [l,r,t,b]:
                        if 0<= ni< m and 0<= nj < n and grid[ni][nj] == '1':
                            if find(i,j) != find(ni,nj):
                                union(i,j,ni,nj)
        ans = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if parent[i][j] == (i,j):
                        ans +=1
        
        return ans