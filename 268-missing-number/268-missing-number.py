class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        i = 0
        n = len(nums)
        zero_value = False
        while i < n:
            if abs(nums[i]) < n:
                nums[abs(nums[i])] *= -1
                if nums[abs(nums[i])] == 0:
                    zero_value = True 
            i += 1

        i = 0
        while i < n:
            if nums[i] != 0:
                if nums[i] > 0:
                    return i
            elif nums[i] == 0:
                if zero_value == False:
                    return i
            i += 1
        return n
        