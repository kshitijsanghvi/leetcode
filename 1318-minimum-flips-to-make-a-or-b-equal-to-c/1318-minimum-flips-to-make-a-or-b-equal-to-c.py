class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while c:
            if c & 1 == 1:
                if a & 1 != 1 and b & 1 != 1:
                    ans+=1
            else:
                if a & 1 == 1:
                    ans+=1
                if b & 1 == 1:
                    ans +=1
            a = a >> 1
            b = b >> 1
            c = c >> 1
        while a:
            if a & 1 == 1:
                ans +=1
            a = a >> 1
        while b:
            if b & 1 == 1:
                ans +=1
            b = b >> 1
        return ans