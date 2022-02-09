class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        ans = []
        for i in range(n):
            find = -nums[i]
            d = {}
            for j in range(i+1,n):
                if find - nums[j] in d:
                    ans.append(tuple(sorted([nums[i],nums[d[find - nums[j]]],nums[j]])))
                
                d[nums[j]] = j
        return list(set(ans))