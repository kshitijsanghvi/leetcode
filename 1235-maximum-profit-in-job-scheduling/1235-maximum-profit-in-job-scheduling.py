class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        startTime = [[startTime[i],i] for i in range(n)]
        startTime.sort()
        dp = [0 for i in range(n+1)]
#         def helper(i):
#             if i >= n:
#                 return 0
            
#             if i not in dp:
#                 idx = startTime[i][1]
#                 dp[i] = max(profit[idx] + helper(bisect.bisect_left(startTime,[endTime[idx],],lo = i + 1)), helper(i+1))
            
#             return dp[i]
    
#         return helper(0)

        for i in range(n-1,-1,-1):
            dp[i] = max(profit[startTime[i][1]] + dp[bisect.bisect_left(startTime, [endTime[startTime[i][1]],])], dp[i+1])
        
        return dp[0]

        