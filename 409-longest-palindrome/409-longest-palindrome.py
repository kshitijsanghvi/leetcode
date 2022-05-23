class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        
        ans = 0
        odd = 0
        
        for i in d:
            if d[i] % 2 == 1:
                if not odd:
                    odd = 1
                ans += d[i] - 1
            else:
                ans += d[i]
                
        return ans + odd