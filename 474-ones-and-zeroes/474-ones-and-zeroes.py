class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        cs = []
        ans = 0
        dp = {}
        
        def helper(i,m,n):
            nonlocal ans
            if i == len(strs):
                return 0
            else:
                if (i,m,n) not in dp:
                    dp[i,m,n] = helper(i+1,m,n)
                    d = Counter(strs[i])
                    if m - d['0'] >= 0 and n - d['1'] >= 0:
                        dp[i,m,n] = max(dp[i,m,n], 1 + helper(i+1, m - d['0'], n - d['1']))
                        
                ans = max(ans, dp[i,m,n])
                return dp[i,m,n]
            
        return helper(0,m,n)