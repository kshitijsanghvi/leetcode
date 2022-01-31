class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if stones[1] - stones[0] > 1:
            return False
        d = Counter(stones)
        dp = {}

        def helper(i, p):
            if i == stones[-1]:
                return True
            if i > stones[-1]:
                return False

            elif (i, p) not in dp:
                for j in range(max(i + p - 1,i+1), i + p + 2):
                    if j in d:
                        if helper(j, j - i):
                            return True

                dp[i, p] = False

            return dp[i, p]

        return helper(stones[1], 1)

