class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] =math.inf
                
        for i in range(n):
            x = abs(nums[i])
            if x <= n and nums[x-1] > 0:
                nums[x-1] = -nums[x-1]
            
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1