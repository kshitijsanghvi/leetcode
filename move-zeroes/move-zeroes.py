class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = f = 0
        n = len(nums)
        
        while f < n:
            if nums[f] != 0:
                nums[s], nums[f] = nums[f], nums[s]
                s += 1
            f += 1
        
                
        