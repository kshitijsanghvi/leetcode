class Solution:
    def strangePrinter(self, s: str) -> int:
        
        dp = {}
        
        def helper(i,j):
            if i == j:
                return 1
            
            if (i,j) not in dp:
                idx = i + s[i:j+1].rindex(s[i])

                
                dp[i,j] = min([1 + helper(i+1,j)]+[(helper(i,k-1) + (helper(k+1,j) if k + 1 <= j else 0) ) for k in range(i+1,idx+1) if s[k] == s[i]])
                
                
            return dp[i,j]
        return helper(0,len(s)-1)
            