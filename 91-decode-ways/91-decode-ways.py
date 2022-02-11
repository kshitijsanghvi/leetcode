class Solution:
    def numDecodings(self, s: str) -> int:
        d = {str(i) : 1 for i in range(1,27)}
        d[""] = 1
        n = len(s)
        dp = [0 for i in range(n)] + [1]
        for i in range(n-1,-1,-1):
            for j in range(i+1,i+3):
                if s[i:j] in d:
                    dp[i]+=(dp[j] if j <= n else 0)
                    
        return dp[0]