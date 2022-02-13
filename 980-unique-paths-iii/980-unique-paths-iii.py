class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m ,n = len(grid), len(grid[0])
        dist = 0
        start = None
        end = None
        found1 = found2 = True
        for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0:
                        dist+=1
                        
                    if found1 or found2:
                        if grid[i][j] == 1:
                            start = [i,j]
                            found1 = False
                        if grid[i][j] == 2:
                            found2 = False
                            end = [i,j]
        v = defaultdict(int)
        v[start[0],start[1]] = 1
        q = [start]
        ans=0        
        def dfs(cx,cy,cd):
            nonlocal ans
            if [cx,cy] == end and cd == dist+1:
                ans+=1
            else:
                l = [cx,cy-1]
                r = [cx,cy+1]
                t = [cx-1,cy]
                b = [cx+1,cy]

                for nx,ny in [l,r,t,b]:
                    if 0 <= nx < m and 0<=ny<n and v[nx,ny] == 0 and grid[nx][ny]!=-1:
                        v[nx,ny] = 1
                        dfs(nx,ny,cd+1)
            v[cx,cy] = 0
        dfs(start[0],start[1],0)
        return ans
                    
            