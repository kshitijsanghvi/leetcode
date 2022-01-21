class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        h = [[0 for i in range(n)] for i in range(m)]
        v = [[0 for i in range(n)] for i in range(m)]
        d = [[0 for i in range(n)] for i in range(m)]
        ad = [[0 for i in range(n)] for i in range(m)]
        
        ad[m-1][n-1] = h[m-1][n-1] =v[m-1][n-1]=d[m-1][n-1]= mat[m-1][n-1]
        ans = mat[m-1][n-1]
        for j in range(n-2,-1,-1):
            if mat[m-1][j] == 1:
                h[m-1][j] = 1 + h[m-1][j+1]
                v[m-1][j] = 1
                d[m-1][j] = 1
                ad[m-1][j] = 1
                ans = max(ans,h[m-1][j],v[m-1][j],d[m-1][j],ad[m-1][j])
                
        for i in range(m-2,-1,-1):
            if mat[i][n-1] == 1:
                v[i][n-1] = 1 + v[i+1][n-1]
                h[i][n-1] = 1
                d[i][n-1] = 1
                ans = max(ans,h[i][n-1],v[i][n-1],d[i][n-1],ad[i][n-1])
                
                
        
        for i in range(m-2,-1,-1):
            for j in range(n-2, - 1, -1):
                if mat[i][j] == 1:
                    h[i][j] = 1 + h[i][j+1]
                    v[i][j] = 1 + v[i+1][j]
                    d[i][j] = 1 + d[i+1][j+1]
                    if j - 1 >= 0:
                        ad[i][j] = 1 + ad[i+1][j-1]
                    else:
                        ad[i][j] = 1
                        
                    ans = max(ans,h[i][j],v[i][j],d[i][j],ad[i][j])
                    
                    
        for i in range(m-2,-1,-1):
            if mat[i][n-1] == 1:
                ad[i][n-1] = 1 + ad[i+1][n-2]
                ans = max(ans,ad[i][n-1])
                
        return ans
                
                