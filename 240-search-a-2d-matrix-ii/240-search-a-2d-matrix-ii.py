class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        
        i,j = m-1,0
        
        while 0 <= i < m and 0 <= j < n and matrix[i][j] != target :
            if target > matrix[i][j]:
                j +=1
            else:
                i-=1
        if 0 <= i < m and 0 <= j < n and matrix[i][j] == target:
            return True
        else:
            return False
        