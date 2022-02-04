class Solution:
    def rob(self, nums):
        # case 1
        if len(nums) == 1:
            return nums[0]
        dp = {}
        def helper(i):
            if i >= len(nums) - 1:
                return 0
            if i not in dp:
                dp[i] = max(nums[i] + helper(i+2), helper(i+1))
            
            return dp[i]
        
        a = helper(0)
        
        dp = {}
        def helper1(i):
            if i >= len(nums):
                return 0
            if i not in dp:
                dp[i] = max(nums[i] + helper1(i+2), helper1(i+1))
            
            return dp[i]
        b = helper1(1)
        return max(a,b)