class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        
        for i in range(1,amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        return dp[-1] if dp[-1] != math.inf else -1