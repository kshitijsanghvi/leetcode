class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}
        
        def helper(i,j):
            if i==j:
                return True
            if i > j:
                return True
            
            if (i,j) not in dp:
                if s[i] == s[j] and helper(i+1,j-1):
                    dp[i,j] = True
                    
                else:
                    dp[i,j] = False
                    
                helper(i,j-1)
                helper(i+1,j)
            
            return dp[i,j]
                            
        helper(0,len(s)-1)
        ans = 0
        for i in dp:
            if dp[i] == True:
                ans+=1
                
        return ans + len(s)