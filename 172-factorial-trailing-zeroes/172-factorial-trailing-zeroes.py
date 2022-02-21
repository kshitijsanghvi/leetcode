class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        
        power = 5
        while n >= power:
            ans += n//power
            power *= 5
        return ans
            