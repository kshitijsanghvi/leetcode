class Solution:
    def subarraySum(self, nums, k):
        d = defaultdict(int)
        cum = 0
        ans = 0
        d[0] = 1
        for i,v in enumerate(nums):
            cum+=v
            if ( cum - k) in d:
                ans += d[cum - k]
            d[cum]+=1
        return ans
