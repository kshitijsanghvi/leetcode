class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row = copy.deepcopy(matrix)
        self.column = copy.deepcopy(matrix)
        
        self.m, self.n = len(matrix), len(matrix[0])
        for i in range(self.m):
            for j in range(1,self.n):
                self.row[i][j] += self.row[i][j-1]
        
        for j in range(self.n):
            for i in range(1,self.m):
                self.column[i][j] += self.column[i-1][j]
        
        self.sum = [[0]*self.n for i in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if 0 <= i - 1 and 0 <= j - 1:
                    self.sum[i][j] += self.sum[i-1][j-1]
                self.sum[i][j] += self.row[i][j]
                if 0 <= i - 1:
                    self.sum[i][j] += self.column[i-1][j]
        
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.sum[row2][col2]
        if 0 <= col1-1:
            ans -= self.sum[row2][col1-1]
        if 0 <= row1-1:
            ans -= self.sum[row1-1][col2]
        
        if 0 <= row1 -1 and 0 <= col1 -1:
            ans += self.sum[row1-1][col1-1]
        return ans
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)