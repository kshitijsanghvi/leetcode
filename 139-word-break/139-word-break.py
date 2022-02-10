class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = Counter(wordDict)
        n = len(s)
        
        
        dp = [False for i in range(n)] + [True]
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i:j+1] in d:
                    dp[i] = dp[i] or dp[j+1]
        return dp[0]              