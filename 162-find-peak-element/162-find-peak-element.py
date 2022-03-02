class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-math.inf] + nums + [-math.inf]
        
        l = 1
        r = len(nums) - 2
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid - 1
            elif nums[mid-1] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
                