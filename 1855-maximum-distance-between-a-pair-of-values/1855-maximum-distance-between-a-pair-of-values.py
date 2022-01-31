class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[-1] > nums2[0]:
            return 0
        n2 = len(nums2)
        n1 = len(nums1)

        i = 0
        j =0
        n = min(n1,n2)
        res = 0
        while i < n1 and j < n2:
            
            while j < n2 and nums2[j] >= nums1[i]:
                j +=1

            if j == n2:
                if nums2[j-1] >= nums1[i]:
                    return max(res,j -1 - i)    

            res = max(res,j -1 - i)
            i += 1
        return res
            
                