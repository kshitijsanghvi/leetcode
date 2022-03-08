class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num == 1:
            return 1
        ans = 0
        mul = 1
        for i in range(9,1,-1):
            while num % i == 0:
                num = num // i
                ans = mul * i + ans
                mul = mul * 10
        return ans if num == 1 and ans < 2**31 else 0     
            
        