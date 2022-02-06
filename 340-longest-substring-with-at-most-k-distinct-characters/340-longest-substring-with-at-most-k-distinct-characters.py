class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = Counter()
        l = 0
        res = 0
        for i in range(len(s)):
            if d[s[i]] == 0:
                k-=1
            d[s[i]] += 1
            
            while k < 0:
                d[s[l]]-=1
                if d[s[l]]==0:
                    k+=1
                l+=1
            
            res = max(res,i - l + 1)
        return res