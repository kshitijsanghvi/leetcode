class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = mid = 0
        r = len(nums)
        
        while l < r:
            if nums[l] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                mid += 1
                l += 1
            elif nums[l] == 2:
                r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            else:
                l += 1
        return 