class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [[v,i] for i,v in enumerate(nums)]
        nums.sort()
        l = 0
        r = len(nums) - 1
        
        while l < r:
            if nums[l][0] + nums[r][0] == target:
                return [nums[l][1],nums[r][1]]
            if nums[l][0] + nums[r][0] > target:
                r-=1
            else:
                l+=1