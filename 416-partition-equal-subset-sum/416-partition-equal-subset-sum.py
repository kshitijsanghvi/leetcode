class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s//2
        
        dp = {}
        
        def helper(s,i):
            if s == target:
                return True
            if i == len(nums):
                return False
            
            if (s,i) not in dp:
                dp[s,i] = helper(s,i+1) or helper(s+nums[i],i+1)
            
            return dp[s,i]
        return helper(0,0)
                