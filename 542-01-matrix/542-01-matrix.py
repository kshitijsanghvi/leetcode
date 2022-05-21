class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        m, n = len(mat), len(mat[0])
        color = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i,j,0])
        
        while q:
            ci,cj,cd = q.popleft()
            l = [ci,cj-1]
            r = [ci,cj + 1]
            t = [ci-1,cj]
            b = [ci+1,cj]
            
            for ni,nj in [l,r,t,b]:
                if 0 <= ni <m and 0<=nj<n:
                    if mat[ni][nj]!= 0 and color[ni,nj] == 0:
                        color[ni,nj] = 1
                        mat[ni][nj] = cd + 1
                        q.append([ni,nj,cd+1])
        return mat
        