class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr.sort()
        n = len(arr)
        dp = {i:1 for i in arr}
        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i]/arr[j] in dp:
                    dp[arr[i]] += dp[arr[j]] * dp[arr[i]/arr[j]]
                    dp[arr[i]] = dp[arr[i]] % mod
        
        return sum(dp.values()) % mod