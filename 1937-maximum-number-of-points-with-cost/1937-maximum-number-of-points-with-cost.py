class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = list(points[0])
        m, n = len(points), len(points[0])
        
        for i in range(1,m):
            
            for j in range(1,n):
                dp[j] = max(dp[j-1]-1,dp[j])
                
            for j in range(n-2,-1,-1):
                dp[j] = max(dp[j+1]-1,dp[j])
                
            for j in range(n):
                dp[j] += points[i][j]
                
        return max(dp)