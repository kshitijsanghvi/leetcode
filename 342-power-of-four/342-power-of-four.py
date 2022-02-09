class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0 and n & (n-1) == 0:
            count = 0
            while n != 1:
                count+=1
                n = n >> 1
            
            if count & 1 != 1:
                return True