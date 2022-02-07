class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        
        def helper(i):
            if i >= n-1:
                return 0
            
            if i not in dp:
                dp[i] = 1 + min([float('inf')] + [helper(i+j) for j in range(1,nums[i]+1)])
            
            return dp[i]
        
        return helper(0)