class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}
        
        def helper(i):
            if i >= len(nums):
                return 0
            
            
            if i  not in dp:
                
                dp[i] = max( nums[i] + helper(i + 2), helper(i + 1))
                
            return dp[i]
        
        return helper(0)