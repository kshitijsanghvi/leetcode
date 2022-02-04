class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        l = 0
        r = m * n - 1
        
        def find(i):
            m1 = i//n
            n1 = i - m1*n
            return matrix[m1][n1]
        
        while l < r:
            
            mid = l + (r-l)//2
            
            v = find(mid)
            # print(l,r,mid,v)
            if v == target:
                return True
            elif v > target:
                r = mid - 1
            else:
                l = mid + 1
        return True if l==r and matrix[l//n][l - l//n*n]== target else False
                
        