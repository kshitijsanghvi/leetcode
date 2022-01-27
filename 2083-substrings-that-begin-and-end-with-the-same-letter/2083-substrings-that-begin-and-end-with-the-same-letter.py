class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        d={}
        for i in c.values():
            if i not in d:
                d[i] = i*(i+1)//2
            ans+=d[i]
        
        return ans