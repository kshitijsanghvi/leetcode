class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        v = {}
        
        m ,n = len(grid), len(grid[0])
        ans = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                
                if grid[i][j] == 0 and (i,j) not in v:
                    
                    v[i,j] = 1
                    q = [(i,j)]
                    flag = 0
                    while q:
                        cx,cy = q.pop(0)
                        l = (cx,cy-1)
                        r = (cx,cy+1)
                        t = (cx-1,cy)
                        b = (cx+1,cy)
                        
                        for (nx,ny) in [l,r,t,b]:
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx,ny) not in v:
                                if nx == 0 or nx == m-1 or ny == 0 or ny == n-1:
                                    flag = 1
                                v[nx,ny] = 1
                                q.append((nx,ny))
                    

                    if flag == 0:
                        ans +=1
        return ans
                    