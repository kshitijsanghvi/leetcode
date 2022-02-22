class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        d = Counter()
        n = len(s)
        max_l = -math.inf
        
        for i in range(n):
            for j in range(i+1,n+1):
                t = s[i:j]
                d[t]+=1
                if d[t] > 1:
                    max_l = max(max_l,j - i)
                
        return max_l if max_l!=-math.inf else 0