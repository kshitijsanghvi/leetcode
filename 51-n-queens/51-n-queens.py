class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [0] * n
        diag1 = [0] * (2*n - 1)
        diag2 = [0] * (2*n - 1)
        current_state = []
        ans = []
        
        def helper(row):
            if row == n:
                ans.append(current_state[:]) 
            else:
                for col in range(n):
                    if cols[col] == diag1[row + col] == diag2[n - row + col - 1] == 0:
                        cols[col] = diag1[row + col] = diag2[n - row + col -1 ] = 1
                        current_string = "."*col + "Q" + "."*(n - 1 - col)
                        current_state.append(current_string)
                        helper(row + 1)
                        current_state.pop()
                        cols[col] = diag1[row + col]  = diag2[n - row + col -1 ] = 0
        helper(0)
        return ans