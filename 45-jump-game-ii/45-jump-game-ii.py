class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0 for i in range(n)]
        for i in range(n-2,-1,-1):
            dp[i] = 1 + min([float('inf')]+[dp[i+j] for j in range(1,min(n,nums[i]+1) ) if i + j < n])
        return dp[0]