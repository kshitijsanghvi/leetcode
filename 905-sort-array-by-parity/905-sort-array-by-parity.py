class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0 
        r = n - 1
        while l < r:
            while l < n and nums[l]%2 == 0:
                l += 1
            while r >= 0 and nums[r]%2 == 1:
                r -= 1
                
            if l < r and l < n and r >= 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r -= 1
        return nums
        