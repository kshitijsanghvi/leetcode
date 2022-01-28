class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m ,n = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        v = {}
        start = [1,0,0]
        v[0,0] = 1
        h = [start]
        
        while h:
            cd,cx,cy = h.pop(0)
            if (cx,cy) == (m-1,n-1):
                return cd 
            else:
                
                l = (cx,cy-1)
                r = (cx,cy+1)
                t = (cx-1,cy)
                b = (cx+1,cy)
                tld = (cx-1,cy-1)
                trd = (cx-1,cy+1)
                bld = (cx+1,cy-1)
                brd = (cx+1,cy+1)
                
                
                for nx,ny in [l,r,t,b,tld,trd,bld,brd]:
                    if 0<=nx<m and 0<= ny<n and grid[nx][ny] == 0:
                        if (nx,ny) not in v or v[nx,ny] > cd + 1:
                            v[nx,ny] = cd + 1
                            heapq.heappush(h,[cd+1,nx,ny])
        return -1