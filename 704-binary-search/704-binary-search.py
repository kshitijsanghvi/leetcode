class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(l,r):
            while l <= r:
                mid = l + (r-l)//2
                
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return -1
        
        return binary_search(0,len(nums)-1
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            )