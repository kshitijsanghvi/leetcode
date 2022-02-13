class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        v = {}
        ans = 0
        def bfs(cx,cy):
            
            q = [[cx,cy]]
            while q:
                cx,cy = q.pop()
                l = [cx,cy-1]
                r = [cx,cy+1]
                t = [cx-1,cy]
                b = [cx+1,cy]
                
                for nx,ny in [l,r,t,b]:
                    if 0 <= nx < m and 0 <=ny<n and (nx,ny) not in v and grid[nx][ny]=='1':
                        v[nx,ny] = 1
                        q.append([nx,ny])
                        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]== '1' and (i,j) not in v:
                    v[i,j] = 1
                    ans+=1
                    bfs(i,j)
        return ans