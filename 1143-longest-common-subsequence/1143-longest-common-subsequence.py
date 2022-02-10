class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        
        def helper(i,j):
            if i >= len(text1):
                return 0
            
            if j >= len(text2):
                return  0 
            
            if (i,j) not in dp:
                
                if text1[i] == text2[j]:
                    dp[i,j] = 1 + helper(i + 1,j+1)
                    
                else:
                    dp[i,j] = max(helper(i,j+1),helper(i+1,j))
            return dp[i,j]
        
        return helper(0,0)