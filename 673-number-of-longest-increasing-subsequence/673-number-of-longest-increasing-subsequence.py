class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0 for i in range(n)]
        nls = [0 for i in range(n)]
        
        if n == 1:
            return 1
        
        dp[0] = 1
        nls[0] = 1
        
        for i in range(1,n):
            max_v = 0
            max_c = 0
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    if max_v == dp[j]:
                        max_c += nls[j]
                    elif max_v < dp[j]:
                        max_v = dp[j]
                        max_c = nls[j]
            dp[i] = max_v + 1
            nls[i] = max_c if max_c != 0 else 1
            
#         print(dp)
#         print(nls)
        mm = max(dp)
        ans = 0
        for i in range(n):
            if dp[i] == mm:
                ans+=nls[i]
        return ans