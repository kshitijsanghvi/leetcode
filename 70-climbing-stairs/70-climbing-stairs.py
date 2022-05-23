class Solution:
    def climbStairs(self, n: int) -> int:
        """
        RR
        base case: 
        dp[1] = 1
        dp[2] = 2
        
        dp[x] = dp[x-1] + dp[x-2]
        
        """
        l1 = 1
        l2 = 2
        if n == 1:
            return l1
        if n == 2:
            return l2
        
        for i in range(3,n+1):
            l2, l1 = l1 + l2, l2
        
        return l2