class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        Approach : 
        Trim
        Binary search, take max
        """
        nums = arr
        n = len(arr)
        l = 1
        while l < n and nums[l] >= nums[l-1]:
            l +=1
            
        if l == n:
            return 0
        
        r = n - 2
        
        while r >= 0 and nums[r] <= nums[r+1]:
            r -= 1

        l = l - 1
        r = r + 1
        ans = min(r,n - l - 1)
        while l >= 0:
            if nums[l] <= nums[r]:
                ans = min(ans,r - l - 1)
            idx = bisect.bisect_left(nums, nums[l],lo = r)
            ans = min(ans,idx - l - 1)
            l-=1
        return ans