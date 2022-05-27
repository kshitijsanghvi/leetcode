class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        n = num
        while n:
            count += 1
            if n % 2 == 0:
                
                n = n // 2
            else:
                n = n - 1
        return count