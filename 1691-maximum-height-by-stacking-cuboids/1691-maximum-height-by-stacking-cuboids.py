class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        cuboids = [sorted(i) for i in cuboids]
        cuboids.sort(reverse=True)
        dp = [0 for i in range(n)]
        dp[-1] = cuboids[-1][-1]
        def check(i,j):
            for k in range(3):
                if cuboids[i][k] < cuboids[j][k]:
                    return False
            return True
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if check(i,j):
                    dp[i] = max(dp[i],cuboids[i][-1] + dp[j])
                dp[i] = max(dp[i],cuboids[i][-1])
        return max(dp)