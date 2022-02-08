class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l = [1 for i in range(len(nums))]
        r =  [1 for i in range(len(nums))]
        
        for i in range(1,len(nums)):
            l[i] = l[i-1] * nums[i-1]
        mul = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            l[i] = l[i] * mul
            mul *= nums[i]
        return l