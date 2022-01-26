class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        p = prob
        dp = {}
        n = len(p)
        def helper(i,t):
            nonlocal p
            if t > n - i:
                return 0
            if i == n - 1:
                if t == 1:
                    return p[i]
                if t == 0:
                    return 1 - p[i]
                
            if (i,t) not in dp:
                if t > 0:
                    dp[i,t] = p[i] * helper(i+1,t-1) + (1-p[i])*helper(i+1,t)
                else:
                    dp[i,t] = (1-p[i])*helper(i+1,t)
                    
            return dp[i,t]
        
        return helper(0,target)