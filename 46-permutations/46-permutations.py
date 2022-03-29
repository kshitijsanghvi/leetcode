class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        temp = []
        d = Counter()
        def make_permutations():
            if len(temp) == n:
                ans.append(temp[:])
            else:
                for i in range(n):
                    if not d[i]:
                        d[i] = 1
                        temp.append(nums[i])
                        make_permutations()
                        d[i] = 0
                        temp.pop()
        make_permutations()
        return ans