class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [ 0 for i in range(len(nums))]
        n = len(nums)
        for i in range(n-1,-1,-1):
            
            dp[i] = max(nums[i] + (dp[i+2] if i + 2 < n else 0), (dp[i+1] if i + 1 < n else 0))
            
        return dp[0]