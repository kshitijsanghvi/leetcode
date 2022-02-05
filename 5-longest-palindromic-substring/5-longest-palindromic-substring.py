class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        max_v = 1
        ans = (0,1)
        for ii in range(n-1,-1,-1):
            for j in range(ii,n):
                if s[ii] == s[j]:
                    if j-ii <= 1 or (ii+1 < n and j-1>=0 and dp[ii+1][j-1]):
                        dp[ii][j] = 1
                    if dp[ii][j]:
                        if max_v < j - ii +1:
                            max_v = j - ii + 1
                            ans = (ii,j+1)
        return s[ans[0]:ans[1]]