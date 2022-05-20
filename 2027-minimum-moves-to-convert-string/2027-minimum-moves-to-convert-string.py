class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] != 'X':
                i += 1
                continue
            else:
                i += 3
                ans += 1
        return ans