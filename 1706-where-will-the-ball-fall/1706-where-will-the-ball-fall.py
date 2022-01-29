class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        dp = {}
        m = len(grid)
        n = len(grid[0])
        def helper(i,j):
            if i == m:
                return j
            
            if (i,j) not in dp:
                
                if grid[i][j] == 1 and j + 1 < n and grid[i][j+1] == 1:
                    dp[i,j] = helper(i+1,j+1)
                elif grid[i][j] == -1 and j - 1 >= 0 and grid[i][j-1] == -1:
                    dp[i,j] = helper(i+1,j-1)
                else:
                    dp[i,j] = -1
                    
            return dp[i,j]
        
        return [helper(0,j) for j in range(n)]