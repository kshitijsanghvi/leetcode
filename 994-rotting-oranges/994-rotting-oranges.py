class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        good = 0
        
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j,0])
                if grid[i][j] == 1:
                    good += 1
        
        ans = 0
        
        while q:
            ci,cj,cd = q.popleft()
            ans = max(ans,cd)
            
            l = [ci,cj-1]
            r = [ci,cj+1]
            t = [ci-1,cj]
            b = [ci+1,cj]
            
            for ni,nj in [l,r,t,b]:
                if 0 <= ni < m and 0 <= nj<n:
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        good -= 1
                        q.append([ni,nj,cd + 1])
                        
        return ans if good == 0 else -1