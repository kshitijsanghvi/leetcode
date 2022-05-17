class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i= j = k = 0
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        while i < n1 and j < n2:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
        return nums1[:k]
                