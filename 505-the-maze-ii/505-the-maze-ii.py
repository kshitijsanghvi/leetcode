class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        v = {}
        h = []
        heapq.heappush(h,[0,start[0],start[1]])
        v[start[0],start[1]] = 0
        ans = []
        while h:
            cd,cx,cy = heapq.heappop(h)
            if [cx,cy] == destination:
                return cd
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
                    heapq.heappush(h,[nd,nx,ny])

                
                
                    
                #Go Right
                nx = cx
                ny = cy
                nd = cd
                
                while ny + 1 < n and maze[nx][ny+1]!=1:
                    ny += 1
                    nd += 1
                
                if (nx,ny) not in v or v[nx,ny] > nd:
                    v[nx,ny] = nd
                    heapq.heappush(h,[nd,nx,ny])
                    
                #Go Up
                nx = cx
                ny = cy
                nd = cd
                
                while nx - 1 >= 0 and maze[nx-1][ny]!=1:
                    nx -= 1
                    nd += 1
                
                if (nx,ny) not in v or v[nx,ny] > nd:
                    v[nx,ny] = nd
                    heapq.heappush(h,[nd,nx,ny])
                    
                #Go down
                nx = cx
                ny = cy
                nd = cd
                
                while nx + 1 < m and maze[nx+1][ny]!=1:
                    nx += 1
                    nd += 1
                
                if (nx,ny) not in v or v[nx,ny] > nd:
                    v[nx,ny] = nd
                    heapq.heappush(h,[nd,nx,ny])
                    
        return -1 if len(ans) == 0 else min(ans)