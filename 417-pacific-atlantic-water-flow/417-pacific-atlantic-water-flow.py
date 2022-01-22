class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h = heights
        m , n = len(h), len(h[0])
        
        #check if water can flow to P
        #init
        q = []
        v = {}
        for i in range(m):
            if (i,0) not in v:
                v[i,0] = 1
                q.append((i,0))
        for j in range(n):
            if (0,j) not in v:
                v[0,j] = 1
                q.append((0,j))
        
        while q:
            cx,cy = q.pop()
            l = (cx,cy-1)
            r= (cx,cy+1)
            t= (cx-1,cy)
            b= (cx+1,cy)
            
            for (nx,ny) in [l,r,t,b]:
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in v and heights[nx][ny] >= heights[cx][cy]:
                    v[nx,ny] = 1
                    q.append((nx,ny))

        
        #check if water can flow to A
        v1 = v
        v = {}
        
        for i in range(m):
            if (i,n-1) not in v:
                v[i,n-1] = 1
                q.append((i,n-1))
        for j in range(n):
            if (m-1,j) not in v:
                v[m-1,j] = 1
                q.append((m-1,j))
                
        while q:
            cx,cy = q.pop()
            l = (cx,cy-1)
            r= (cx,cy+1)
            t= (cx-1,cy)
            b= (cx+1,cy)
            
            for (nx,ny) in [l,r,t,b]:
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in v and heights[nx][ny] >= heights[cx][cy]:
                    v[nx,ny] = 1
                    q.append((nx,ny))

        ans = []
        for i in range(m):
            for j in range(n):
                if (i,j) in v1 and (i,j) in v:
                    ans.append([i,j])
                    
        return ans