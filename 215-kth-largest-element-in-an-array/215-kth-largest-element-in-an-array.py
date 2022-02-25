class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        def findKsmallest(nums,k):
            if len(nums) == 1:
                return nums[0]
            
            pivot = nums[0]
            l = 1
            r = len(nums)-1
            
            while l <= r:
                while l < len(nums) and nums[l] < pivot:
                    l+=1
                while nums[r] > pivot:
                    r-=1
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l+=1
                    r-=1
            
            nums[0], nums[r] = nums[r], nums[0]
            
            kk = r + 1
            if kk == k:
                return nums[r]
            elif kk > k:
                return findKsmallest(nums[:r],k)
            else:
                return findKsmallest(nums[r+1:],k - kk)
            
        return findKsmallest(nums,len(nums)-k+1)
            
            