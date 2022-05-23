class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) //2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]:
                # if inflection point is on the right then it contains values > mid and < nums[l]
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # if inflection point is on the left then it contains vales < nums[id] and values greater than nums[r]
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                
                    
        return -1  
                    