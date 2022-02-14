
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = set(wordDict)
        n = len(s)
        dp = [[] for i in range(n)] + [[""]]
        
        for i in range(n-1,-1,-1):
            for j in range(i+1,n+1):
                if s[i:j] in d:
                    for l in dp[j]:
                        dp[i].append(s[i:j]+(' '+l if l != "" else ""))
        return dp[0]
