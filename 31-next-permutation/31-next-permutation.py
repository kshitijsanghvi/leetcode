class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(nums,l,r):
            while l < r:
                nums[l],nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        n = len(nums)
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
                
        if i == -1:
            return reverse(nums,0,n-1)
            
        else:
            j = i + 1
            while j < n - 1:
                if nums[j + 1] <= nums[i]:
                    break
                j += 1
            nums[j], nums[i] = nums[i], nums[j]
            reverse(nums,i+1,n-1)
            
        return nums
        
        