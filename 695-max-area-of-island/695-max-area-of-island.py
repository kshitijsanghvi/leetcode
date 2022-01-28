class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        v = {}
        
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in v:
                    
                    v[i,j] = 1
                    q = [[i,j]]
                    cans = 0
                    while q:
                        cx,cy = q.pop()
                        cans +=1
                        
                        l = (cx,cy-1)
                        r = (cx,cy+1)
                        t = (cx-1,cy)
                        b = (cx+1,cy)
                        
                        for nx,ny in [l,r,t,b]:
                            if 0<= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and (nx,ny) not in v:
                                v[nx,ny] = 1
                                q.append([nx,ny])
                        
                    ans = max(cans,ans)
                    
        return ans