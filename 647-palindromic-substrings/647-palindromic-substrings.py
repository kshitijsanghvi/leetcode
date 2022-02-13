class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False if j > i else True for j in range(n)] for i in range(n)]
        
        
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if i != j:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
        
        ans = 0
        for i in range(n):
            for j in range(i,n):
                if dp[i][j]:
                    ans+=1
        return ans
                
                    
        # Recurrence Relation dp[i,j] = True if dp[i+1,j-1] else False
        