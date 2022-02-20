class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = [math.inf]
        n = len(nums)
        min_a = [math.inf] * n
        max_a = [-math.inf] * n
        
        for i in range(1,n):
            min_a[i] = min(min_a[i-1],nums[i-1])
        
        for i in range(n-2,-1,-1):
            max_a[i] = max(max_a[i+1],nums[i+1])
            if min_a[i] < nums[i] < max_a[i]:
                return True
            
        return False