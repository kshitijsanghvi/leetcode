class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        @lru_cache(None)
        def helper(i):
            if i >= n-1:
                return 0
            

            return 1 + min([float('inf')] + [helper(i+j) for j in range(1,nums[i]+1)])
            
        return helper(0)