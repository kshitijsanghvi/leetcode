class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        d = Counter()
        max_f = 0
        for i in range(len(s)):
            d[s[i]]+=1
            max_f = max(max_f,d[s[i]])
            
            while i - l + 1 - max_f > k:
                d[s[l]]-=1
                l+=1
            res = max(res,i - l +1)
        return res
        