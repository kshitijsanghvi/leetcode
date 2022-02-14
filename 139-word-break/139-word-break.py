class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n)] + [True]
        wordDict = Counter(wordDict)
        for i in range(n-1,-1,-1):
            dp[i] = max([False]+[dp[j] for j in range(i+1,n+1) if s[i:j] in wordDict])
        return dp[0]