class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        v = {}
        h = []
        heapq.heappush(h,[0,0,0])
        v[0,0] = 0
        while h:
            cd,cx,cy = heapq.heappop(h)
            if cx ==  m-1 and cy == n - 1:
                return cd
            else:
                
                l = (cx,cy-1)
                r = (cx,cy+1)
                t = (cx-1,cy)
                b = (cx+1,cy)
                
                for nx,ny in [l,r,t,b]:
                    if 0<= nx < m and 0 <= ny < n:
                        key = max(cd,abs(heights[nx][ny]-heights[cx][cy]))
                        if (nx,ny) not in v or v[nx,ny] > key:
                            v[nx,ny] = key
                            heapq.heappush(h,[key,nx,ny])
        return 0