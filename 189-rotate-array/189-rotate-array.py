class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reverse(s,e):
            if e > s:
                l = s 
                r = e
                while l <= s + int((e-s)/2):
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -=1 
        
        reverse(n - k,n - 1)
        reverse(0,n - 1 -k)
        reverse(0,n-1)