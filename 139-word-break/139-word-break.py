class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        d = Counter(wordDict)
        dp = {}
        def helper(i):
            if i == n:
                return True
            
            if i not in dp:
                dp[i] = max([0] + [helper(j) for j in range(i+1,n+1) if s[i:j] in d])
            
            return dp[i]
        
        return helper(0)