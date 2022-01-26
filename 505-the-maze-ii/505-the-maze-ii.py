class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        v = {}
        q = [start+[0]]
        v[start[0],start[1]] = 0
        ans = []
        while q:
            cx,cy,cd = q.pop(0)
            if [cx,cy] == destination:
                ans.append(cd)
            else:
                
                #Go left
                nx = cx
                ny = cy
                nd = cd
                
                while ny - 1 >= 0 and maze[nx][ny-1]!=1:
                    ny -= 1
                    nd += 1
                
                if (nx,ny) not in v or v[nx,ny] > nd:
                    v[nx,ny] = nd
                    q.append([nx,ny,nd])
                
                
                    
                #Go Right
                nx = cx
                ny = cy
                nd = cd
                
                while ny + 1 < n and maze[nx][ny+1]!=1:
                    ny += 1
                    nd += 1
                
                if (nx,ny) not in v or v[nx,ny] > nd:
                    v[nx,ny] = nd
                    q.append([nx,ny,nd])
                    
                #Go Up
                nx = cx
                ny = cy
                nd = cd
                
                while nx - 1 >= 0 and maze[nx-1][ny]!=1:
                    nx -= 1
                    nd += 1
                
                if (nx,ny) not in v or v[nx,ny] > nd:
                    v[nx,ny] = nd
                    q.append([nx,ny,nd])
                    
                #Go down
                nx = cx
                ny = cy
                nd = cd
                
                while nx + 1 < m and maze[nx+1][ny]!=1:
                    nx += 1
                    nd += 1
                
                if (nx,ny) not in v or v[nx,ny] > nd:
                    v[nx,ny] = nd
                    q.append([nx,ny,nd])
                    
        return -1 if len(ans) == 0 else min(ans)