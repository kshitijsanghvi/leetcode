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
                while s[r] in d:
                    del(d[s[l]])
                    l+=1
            
            d[s[r]] = 1
            max_l = max(max_l, r - l + 1)

            r += 1
            
        return max_l