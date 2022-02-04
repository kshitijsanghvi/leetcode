class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        d = defaultdict(int)
        dp = Counter(p)
        
        l = 0
        r = 0
        while r < len(p):
            d[s[r]]+=1
            r+=1
        
        ans = []
        if d == dp:
            ans.append(l)
        r-=1
        while r < len(s)-1:
            r+=1
            d[s[r]]+=1
            d[s[l]]-=1
            if d[s[l]] == 0:
                del(d[s[l]])
            l+=1
            if d == dp:
                ans.append(l)
            
        return ans