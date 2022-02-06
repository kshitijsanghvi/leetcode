class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        l = 0
        r = 0
        
        d = {}
        max_l = float('-inf')
        while r < n:
            if s[r] in d:
                l = max(l,d[s[r]]+1)
            
            d[s[r]] = r
            max_l = max(max_l, r - l + 1)

            r += 1
            
        return max_l