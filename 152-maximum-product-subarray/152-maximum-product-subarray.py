class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        min_v = nums[0]
        max_v = nums[0]
        ans = max_v
        for i in range(1,len(nums)):
            if nums[i] < 0:
                max_v, min_v = max(nums[i],min_v*nums[i]), min(max_v*nums[i],nums[i])
            else:
                max_v = max(nums[i],max_v * nums[i])
                min_v = min(nums[i],min_v * nums[i])
            ans = max(ans, max_v) 
        return ans