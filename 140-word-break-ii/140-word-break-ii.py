
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        d = Counter(wordDict)
        dp = {}
        n = len(s)

        def helper(i):
            if i == n:
                return ["", ]
            # base case

            if i not in dp:
                sol = []

                for j in range(i + 1, n + 1):
                    if s[i:j] in d:
                        temp = helper(j)
                        for suf in temp:
                            sol.append(s[i:j] + (' ' + suf if suf !="" else ""))
                dp[i] = sol
            return dp[i]

        return helper(0)
