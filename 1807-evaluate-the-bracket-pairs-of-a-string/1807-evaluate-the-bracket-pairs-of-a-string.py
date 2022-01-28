class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        ans = ""
        d = {}
        for i in knowledge:
            d[i[0]]=i[1]
            
        while '(' in s:
            
            idx1 = s.index('(')
            idx2 = s.index(')')

            ans += s[:idx1]
            
            key = s[idx1+1:idx2]
            value = '?'
            
            if key in d:
                value = d[key]
            
            ans += value
            s = s[idx2+1:]
            
        ans += s
        return ans