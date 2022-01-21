class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        ans = 0
        
        for i in range(n):
            if matrix[m-1][i] == 1:
                ans += 1
        
        for i in range(m-1):
            if matrix[i][n-1] == 1:
                ans += 1
                
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(matrix[i+1][j],matrix[i+1][j+1],matrix[i][j+1])  
                    ans += matrix[i][j]
        return ans