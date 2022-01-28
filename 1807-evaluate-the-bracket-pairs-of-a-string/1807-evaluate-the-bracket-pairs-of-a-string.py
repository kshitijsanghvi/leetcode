class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {}
        for i in knowledge:
            d[i[0]] = i[1]
            
        i = 0
        n = len(s)
        ans = ""
        while i < n:
            if s[i] != '(':
                ans+=s[i]
                i+=1
            else:
                j = i + 1
                key = ""
                while j < n and s[j] != ')':
                    key+=s[j]
                    j+=1
                
                value = '?' if key not in d else d[key]
                ans += value
                i = j +1
        return ans