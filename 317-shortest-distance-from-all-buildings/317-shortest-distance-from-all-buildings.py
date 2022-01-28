class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        d = {}
        
        m,n  = len(grid), len(grid[0])
        c  = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    c+=1
                    v = {}
                    v[i,j]= 1
                    q = [(i,j,0)]
                    
                    while q:
                        cx,cy,cd = q.pop(0)
                        
                        l = (cx,cy-1)
                        r = (cx,cy+1)
                        t = (cx-1,cy)
                        b = (cx+1,cy)
                        
                        for nx,ny in [l,r,t,b]:
                            if 0 <= nx < m and 0 <= ny<n and grid[nx][ny] == 0 and (nx,ny) not in v:
                                v[nx,ny] = 1
                                if (nx,ny) in d:
                                    cc = d[nx,ny][0]
                                    if -1*cc < c - 1:
                                        continue
                                    d[nx,ny][1]+=cd + 1
                                    d[nx,ny][0]-=1
                                else:
                                    d[nx,ny] = [-1,cd+1]

                                q.append((nx,ny,cd+1))
        if d:
            ans = min(d.values())
            if ans[0] == c * -1:
                return ans[1]
        return -1