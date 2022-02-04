class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        m = len(maze)
        n = len(maze[0])
        
        q = [start]
        v = {}
        v[start[0],start[1]] = 1
        while q:
            cx,cy = q.pop()
            if cx == destination[0] and cy == destination[1]:
                return True
            lx,ly = cx,cy
            while 0<=lx < m and 0<=ly-1<n and maze[lx][ly-1] == 0:
                ly-=1
            rx,ry = cx,cy
            while 0<=rx < m and 0<=ry+1<n and maze[rx][ry+1] == 0:
                ry+=1
                
            tx,ty = cx,cy
            while 0<=tx - 1< m and 0<=ty<n and maze[tx-1][ty] == 0:
                tx-=1
                
            bx,by = cx,cy
            while 0<=bx + 1< m and 0<=by<n and maze[bx+1][by] == 0:
                bx+=1
                
            for nx,ny in [[lx,ly],[rx,ry],[tx,ty],[bx,by]]:
                if (nx,ny) not in v:
                    v[nx,ny] = 1
                    q.append([nx,ny])
            
        return False