class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]      
        l = 0
        r = len(nums) - 1
        
        while l +1 < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid
        if l == r:
            return nums[l]
        return nums[r]

                
                
                
