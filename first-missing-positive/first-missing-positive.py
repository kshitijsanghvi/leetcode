class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = math.inf
                
        for i in range(n):
            if nums[i] != math.inf and nums[i]!=-math.inf and nums[i] <= n:
                if nums[abs(nums[i])-1] > 0:
                    nums[abs(nums[i])-1]*=-1
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n+1