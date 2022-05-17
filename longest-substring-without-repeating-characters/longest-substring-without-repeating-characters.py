class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        d = {}
        ans = 0
        while r < n:
            if s[r] in d:
                l = max(l,d[s[r]] + 1)
            d[s[r]] = r
            ans = max(ans, r - l + 1)
            r +=1
        return ans
                