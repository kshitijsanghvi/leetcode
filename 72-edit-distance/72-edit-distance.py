class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        
        """
        Word1 tp Word2
        """
        # dp = {}
        # def helper(i,j):
        #     if i == m:
        #         return n - j
        #     if j == n:
        #         return m - i
        #     # Insert Delete Substitute
        #     if (i,j) not in dp:
        #         dp[i,j]=min(1 + helper(i,j+1),1 + helper(i+1,j),helper(i+1,j+1)+int(word1[i]!=word2[j]))
        #     return dp[i,j]
        # return helper(0,0)
    
    
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        for j in range(n+1):
            dp[m][j] = n - j
        for i in range(m + 1):
            dp[i][n] = m - i
            
        for j in range(n-1,-1,-1):
            for i in range(m - 1, -1, - 1):
                dp[i][j] = min(1 + dp[i][j+1], 1 + dp[i+1][j], dp[i+1][j+1]+int(word1[i]!=word2[j]))
                
        return dp[0][0]