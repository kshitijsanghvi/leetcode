class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[-1] > nums2[0]:
            return 0
        n2 = len(nums2)
        def bs(s):
            if s > n2 - 1:
                return s
            l = s
            r = n2 - 1
            
            while l + 1 < r:
                mid = l + (r- l)//2
                if nums2[mid] >= nums1[s]:
                    l = mid
                else:
                    r = mid - 1
                    
            if nums2[r] >= nums1[s]:
                return r
            if nums2[l] >= nums1[s]:
                return l
            return s
        
        
        
        
        max_d = 0
        for i,v in enumerate(nums1):
            idx = bs(i)
            max_d = max(max_d, idx - i)
            
            
        return max_d