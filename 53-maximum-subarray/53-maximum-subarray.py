class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_v = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i],nums[i-1] + nums[i])
            max_v = max(max_v,nums[i])
        return max_v
            
            