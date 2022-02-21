class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        [1]
        [2,1],[1,2]
        [3,2,1],[2,3,1],[2,1,3],[3,1,2],[1,3,2],[1,2,3]
        """
        n = len(nums)
        ans = [[nums[0]]]
        for i in range(1,n):
            temp = []
            for a in ans:
                nw = len(a)
                for j in range(nw+1):
                    t = a[:j] + [nums[i]] + a[j:]
                    temp.append(t)
            ans = temp
        return ans