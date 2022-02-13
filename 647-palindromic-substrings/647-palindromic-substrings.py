class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}
        ans = 0        
        def helper(i,j):
            nonlocal ans
            if (i,j) not in dp:
                if i==j:
                    ans+=1
                    dp[i,j] = True
                    return True
                if i > j:
                    dp[i,j] = True
                    return True
            
                if s[i] == s[j] and helper(i+1,j-1):
                    dp[i,j] = True
                    ans+=1
                else:
                    dp[i,j] = False
                    
                helper(i,j-1)
                helper(i+1,j)
            
            return dp[i,j]
                            
        helper(0,len(s)-1)
        return ans 