class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Runtime = O(mn)
        Space = O(1)
        
        Approach:
        1. As we cannot use extra space the most straightforward approach is reusing available space 
        2. The underpinning of the same is that we need to extract the information from the reusing memory space first before overwriting the space
        3. The overwriting here is to differentiate if the row0 or col0 has a 0 before
        4. We use the row0 and col0 to flag if that row and col needs to be assigned Zero
        5. Thus we keep two spaces to indicate if the row0 needs to be turned to 0 or not and similarly for col0
        6. Then run the algo
        7. Post processing of 0ing the row0 and col0
        
        """
        m, n = len(matrix), len(matrix[0])

        row0 = False
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True
                break

        col0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
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

        if col0:
            for i in range(m):
                matrix[i][0] = 0

            
        
        
        
                
        