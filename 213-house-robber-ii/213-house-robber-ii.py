class Solution:
    def rob(self, nums):
        # case 1
        if len(nums) == 1:
            return nums[0]
        @lru_cache(None)
        def helper(i):
            if i >= len(nums) - 1:
                return 0
          
            return max(nums[i] + helper(i+2), helper(i+1))
            
        
        a = helper(0)
        @lru_cache(None)
        def helper1(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + helper1(i+2), helper1(i+1))
            
             
        b = helper1(1)
        return max(a,b)