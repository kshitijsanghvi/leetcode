class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat), len(mat[0])
        
        l = 0
        r = n - 1
        
        while l<=r:
            mid = l + (r-l)//2
            
            max_v = -math.inf
            rowNumber = None
            for i in range(m):
                if mat[i][mid] > max_v:
                    max_v = mat[i][mid]
                    rowNumber = i
                    
            isLeftBig = mid - 1 >= l  and mat[rowNumber][mid] < mat[rowNumber][mid - 1]
            isRightBig = mid + 1 <= r and mat[rowNumber][mid] < mat[rowNumber][mid + 1] 
            
            if not isLeftBig and not isRightBig:
                return [rowNumber,mid]
            elif isLeftBig:
                r = mid - 1
            else:
                l = mid + 1