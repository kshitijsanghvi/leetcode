class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        dp = {}
        n = len(workers)
        
        def helper(i, avail):
            if i == n:
                return 0
            
            if (i,avail) not in dp:
                a = list(avail)
                nl = len(a)
                ans = float('inf')
                for idx in range(nl):
                    d = abs(workers[i][0] - bikes[a[idx]][0]) +abs(workers[i][1] - bikes[a[idx]][1])
                    ans = min(ans, d+ helper(i+1,tuple(a[:idx]+a[idx+1:])) )
                dp[i,avail] = ans
            return dp[i,avail]
        
        avail = tuple(i for i in range(len(bikes)))
        return helper(0,avail)