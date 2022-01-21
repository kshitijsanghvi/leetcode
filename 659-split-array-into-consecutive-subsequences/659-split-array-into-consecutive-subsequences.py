class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dp = []
        for i in nums:
            if not dp:
                bisect.insort(dp,[i,1])
                continue
            idx = bisect.bisect(dp,[i-1,0])
            if idx< len(dp) and dp[idx][0] == i - 1:
                cn = dp.pop(idx)
                cn[0] = i
                cn[1]+=1
                bisect.insort(dp,cn)
            else:
                bisect.insort(dp,[i,1])
        # print(dp)
        for i in dp:
            if i[1]<3:
                return False
        return True