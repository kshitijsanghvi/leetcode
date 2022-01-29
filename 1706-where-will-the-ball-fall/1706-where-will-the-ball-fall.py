class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp.append([i for i in range(n)])
        
        for i in range(m-1,-1,-1):
            for j in range(n):
                if grid[i][j] == 1:
                    if j + 1 < n and grid[i][j+1] == 1:
                        dp[i][j] = dp[i+1][j+1]
                    else:
                        dp[i][j] = -1
                elif grid[i][j] == -1:
                    if j - 1 >= 0 and grid[i][j-1] == -1:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = -1
                else:
                    dp[i][j] = -1
            
        return dp[0]