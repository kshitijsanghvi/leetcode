class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = defaultdict(int)
        d = [[0 for i in range(n)] for j in range(m)]
        d[0][0] = 1
        q = [[0,0]]
        v = {}
        v[0,0] = 1
        while q:
            cx,cy = q.pop(0)
            # print(cx,cy)
            r = [cx,cy+1]
            b = [cx+1,cy]
            
            for nx,ny in [r,b]:
                if 0<=nx<m and 0<=ny<n:
                    d[nx][ny]+=d[cx][cy]
                    if (nx,ny) not in v:
                        v[nx,ny] = 1
                        q.append([nx,ny])
        # print(d)
        return d[m-1][n-1]