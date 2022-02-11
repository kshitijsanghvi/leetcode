class Solution:
    def numDecodings(self, s: str) -> int:
        d = {str(i) : 1 for i in range(1,27)}
        
        
        dp = {}
        n = len(s)
        
        def helper(i):
            if i == n:
                return 1
            if i >= n:
                return 0 
            if i not in dp:
                
                
                dp[i] = sum([0]+[helper(j) for j in range(i+1,n+1) if s[i:j] in d])
                
                
            return dp[i]
        
        return helper(0)