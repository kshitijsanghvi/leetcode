class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        dp = [0 for _ in range(n)]
        
        for w in words:
            nw = len(w)
            for i in range(n):
                if s[i:i + nw] == w:
                    dp[i:i+nw] = [1 for i in range(nw)]
        
        bold_state = 0
        
        ans = []
        for i,v in enumerate(dp):
            if v == 1 and bold_state == 0:
                ans.append('<b>')
                bold_state = 1
            if v == 0 and bold_state == 1:
                ans.append('</b>')
                bold_state = 0
            ans.append(s[i])
        if bold_state:
            ans.append('</b>')
        return ''.join(ans)