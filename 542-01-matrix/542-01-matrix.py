class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        m, n = len(mat), len(mat[0])
        
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = math.inf
                if i - 1 >= 0:
                    mat[i][j] = min(mat[i][j], 1 + mat[i-1][j])
                
                if j -1 >= 0:
                    mat[i][j] = min(mat[i][j], 1 + mat[i][j-1])
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                
                if i + 1 < m:
                    mat[i][j] = min(mat[i][j], 1 + mat[i+1][j])
                    
                if j+ 1 < n:
                    mat[i][j] = min(mat[i][j], 1 +  mat[i][j + 1])
                    
        return mat