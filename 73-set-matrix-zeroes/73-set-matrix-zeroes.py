class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Approach:
        1. Mark inner matrix
        2. Deal with the 4 corner cases
        """
        m, n = len(matrix), len(matrix[0])
        
        row0 = False
        
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True
                break
        rowM = False
        
        for j in range(n):
            if matrix[m-1][j] == 0:
                rowM = True
                break
        col0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
                break
        colN = False
        
        for i in range(m):
            if matrix[i][n-1] == 0:
                colN = True
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
                    
        if row0:
            for j in range(n):
                matrix[0][j] = 0
        if rowM:
            for j in range(n):
                matrix[m-1][j] = 0
                
        if col0:
            for i in range(m):
                matrix[i][0] = 0
        if colN:
            for i in range(m):
                matrix[i][n-1] = 0
            
        
        
        
                
        