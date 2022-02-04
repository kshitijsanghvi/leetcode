class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        csum = 0
        min_length = float('inf')
        while r  < n:
            csum += nums[r]
            
            while csum >= target:
                min_length = min(min_length, r - l + 1)
                csum -= nums[l]
                l +=1
            r+=1
        return min_length if min_length != math.inf else 0
            
            