class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        d = {}
        d[0] = 1
        d[1] = 2
        d[2] = 4
        d[3] = 7
        
        for i in range(4,n+1):
            d[i] = (d[i - 1] + d[i -2] + d[i - 3])%mod
        
        with_a = 0
        for i in range(0,n):
            with_a += (d[i]*d[n-i-1])%mod
        
        return (with_a + d[n])%mod