class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m , n = len(grid),len(grid[0])
        
        q = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append([i,j])
        ans = 0
        while q:
            [cx,cy] = q.popleft()
            
            l = (cx,cy-1)
            r = (cx,cy+1)
            t = (cx-1,cy)
            b = (cx+1,cy)
            
            
            for nx,ny in [l,r,t,b]:
                if 0<= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = grid[cx][cy] + 1
                    ans = max(ans,grid[nx][ny])
                    q.append([nx,ny])
        return ans-1