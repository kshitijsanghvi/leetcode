class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in columnTitle:
            i = ord(c) - ord('A') + 1
            ans*=26
            ans+=i
        return ans