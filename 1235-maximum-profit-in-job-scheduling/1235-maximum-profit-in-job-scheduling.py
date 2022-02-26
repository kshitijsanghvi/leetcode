class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        startTime = [[startTime[i],i] for i in range(n)]
        startTime.sort()
        dp = {}
        def helper(i):
            if i >= n:
                return 0
            
            if i not in dp:
                idx = startTime[i][1]
                dp[i] = max(profit[idx] + helper(bisect.bisect_left(startTime,[endTime[idx],],lo = i + 1)), helper(i+1))
            
            return dp[i]
    
        return helper(0)