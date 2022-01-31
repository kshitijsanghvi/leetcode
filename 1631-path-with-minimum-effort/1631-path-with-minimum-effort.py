class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        
        l = 0
        r = 10**6
        
        
        def check(limit):
            nonlocal m,n
            q = deque()
            q.append([0,0,0])
            v = {}
            v[0,0] = 0
            while q:
                cd,cx,cy = q.pop()
                if cx == m-1 and cy == n-1:
                    return True
                else:
                    
                    l = (cx,cy-1)
                    r = (cx,cy+1)
                    t = (cx-1,cy)
                    b = (cx+1,cy)
                    
                    for nx,ny in [l,r,t,b]:
                        if 0<= nx< m and 0<=ny<n:
                            key = max(cd,abs(heights[nx][ny]-heights[cx][cy]))
                            if key <= limit:
                                if (nx,ny) not in v:
                                    v[nx,ny] = key
                                    q.append([key,nx,ny])
            return False
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid + 1
                
        if check(l):
            return l
        else:
            return r 