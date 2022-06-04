class Solution:
    def totalNQueens(self, n: int) -> int:
        col = [0] * n
        diag1 = [0] * (2*n - 1)
        diag2 = [0] * (2*n - 1)
        ans = 0
        def helper(i):
            nonlocal ans
            if i == n:
                ans += 1
            else:
                for j in range(n):
                    if col[j] == diag1[i + j] == diag2[n - 1 - j + i] == 0:
                        col[j] = diag1[i + j] = diag2[n - 1 - j + i] = 1
                        helper(i+1)
                        col[j] = diag1[i + j] = diag2[n - 1 - j + i] = 0
        helper(0)
        return ans
                        