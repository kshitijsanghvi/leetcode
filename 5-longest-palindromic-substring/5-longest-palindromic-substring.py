class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = defaultdict(bool)
        max_v = 1
        l = 0
        r = 1
        for ii in range(n-1,-1,-1):
            for j in range(ii,n):
                if s[ii] == s[j]:
                    if j-ii <= 1 or (ii+1 < n and j-1>=0 and dp[ii+1,j-1]):
                        dp[ii,j] = True
                    if dp[ii,j]:
                        if max_v < j - ii +1:
                            max_v = j - ii + 1
                            l =ii
                            r =j+1
        return s[l:r]
    
    # When not itiialising include diagonal in iterations