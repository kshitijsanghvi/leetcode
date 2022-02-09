class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        dp = [0]
        for a in arr:
            dp.append(dp[-1]^a)
            
        res= []
        for q in queries:
            l = q[0]+1
            r = q[1]+1
            
            res.append(dp[l-1] ^dp[r])
            
        return res