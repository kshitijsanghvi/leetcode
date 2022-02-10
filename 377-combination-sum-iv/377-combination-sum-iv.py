class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = {}
        n = len(nums)
        def helper(target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            
            if target not in dp:
                
                dp[target] = sum([helper(target-i) for i in nums])
                
            return dp[target]
        
        return helper(target)
