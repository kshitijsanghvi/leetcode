class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        ans = 0
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[m-1][n-1] = 1 if text1[-1] == text2[-1] else 0
        ans = max(ans,dp[m-1][n-1])
        for j in range(n-2,-1,-1):
            if text1[m-1] == text2[j]:
                dp[m-1][j] = 1
            else:
                dp[m-1][j] = max(dp[m-1][j],dp[m-1][j+1])
            ans = max(ans,dp[m-1][j])
                
        for i in range(m-2,-1,-1):
            if text1[i] == text2[n-1]:
                dp[i][n-1] = 1
            else:
                dp[i][n-1] = max(dp[i][n-1],dp[i+1][n-1])
            ans = max(ans,dp[i][n-1])
      
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
                ans = max(ans,dp[i][j])
        return ans