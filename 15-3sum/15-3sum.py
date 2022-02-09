class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        nums.sort()
        ans =set()
        res = []
        for i in range(n):
            if i == 0 or  nums[i]!= nums[i-1]:
                find = -nums[i]
                d = {}
                for j in range(i+1,n):
                    if find - nums[j] in d:
                        a = (nums[i],nums[d[find - nums[j]]],nums[j])
                        if a not in ans:
                            res.append(list(a))
                            ans.add(a)

                    d[nums[j]] = j
        return res