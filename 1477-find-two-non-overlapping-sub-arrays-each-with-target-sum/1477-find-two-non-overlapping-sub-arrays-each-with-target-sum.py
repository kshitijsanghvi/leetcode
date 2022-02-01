class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        dp = [float('inf') for _ in range(n + 1)]

        r = 0
        l = 0
        s = 0
        ans = float('inf')
        while r < n:
            s = s +  arr[r]
            if s < target:
                dp[r + 1] = dp[r]
                r += 1

            else:

                while s >= target and l <= r:
                    if s == target:
                        ans = min(ans, dp[l] + r - l + 1)
                        dp[r + 1] = min(dp[r],r - l + 1)

                    else:
                        dp[r+1] = dp[r]
                    s -= arr[l]
                    l += 1
                r += 1

        return -1 if ans == float('inf') else ans
