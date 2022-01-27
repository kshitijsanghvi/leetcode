class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        v = {}
        m, n = len(grid),len(grid[0])
        start  = [-1*grid[0][0],0,0]
        end = (m-1,n-1)
        v[0,0] = grid[0][0]
        
        h = []
        heapq.heappush(h,start)
        
        while h:
            cs,cx,cy = heapq.heappop(h)
            cs = -1 * cs
            if (cx,cy) == end:
                return min(grid[m-1][n-1],cs)
            else:
                
                l = (cx,cy-1)
                r = (cx,cy+1)
                t = (cx-1,cy)
                b = (cx+1,cy)
                
                for nx, ny in [l,r,t,b]:
                    
                    if 0 <= nx < m and 0 <= ny < n:
                        d = min(v[cx,cy],grid[nx][ny])
                        if (nx,ny) not in v or  d > v[nx,ny]:
                            v[nx,ny] = d
                            heapq.heappush(h,[-1*d,nx,ny])
                            