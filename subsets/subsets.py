class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            temp = []
            for s in ans:
                temp.append(s + [i])
            ans.extend(temp)
        return ans