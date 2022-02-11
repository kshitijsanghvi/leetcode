class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [1] + [0 for i in range(target)]
        
        for i in range(target+1):
            for n in nums:
                if n + i <= target:
                    dp[n + i] += dp[i]
        return dp[-1]