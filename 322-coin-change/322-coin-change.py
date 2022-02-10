class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        
        def helper(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            
            
            if amount not in dp:
                dp[amount] = 1 + min([helper(amount - c) for c in coins])
                
            return dp[amount]
        
        v = helper(amount)
        return v if v != float('inf') else -1