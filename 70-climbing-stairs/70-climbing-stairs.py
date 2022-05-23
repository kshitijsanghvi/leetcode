class Solution:
    def climbStairs(self, n: int) -> int:
        """
        RR
        base case: 
        dp[1] = 1
        dp[2] = 2
        
        dp[x] = dp[x-1] + dp[x-2]
        
        """
        dp = {}
        def helper(x):
            if x <= 0:
                return 0
            if x == 1:
                return 1
            if x == 2:
                return 2
            
            if x not in dp:
                dp[x] = helper(x-1) + helper(x-2)
            
            return dp[x]
        
        return helper(n)