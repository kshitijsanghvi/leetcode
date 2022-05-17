class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        count = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i] == prev:
                continue
            else:
                nums[count] = nums[i]
                count+=1
                prev = nums[i]
                
        return count