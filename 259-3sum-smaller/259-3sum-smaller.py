class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums = [[v,i] for i,v in enumerate(nums)]
        nums.sort()
        n = len(nums)
        ans = 0
        print(nums)
        for i in range(n - 2):
            a = nums[i][0]
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i][0] + nums[l][0] + nums[r][0]
                if s < target:
                    ans+= r - l
                    l +=1
                else:
                    r -=1 
        return ans
                