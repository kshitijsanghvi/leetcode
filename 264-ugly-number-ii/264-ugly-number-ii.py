class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uwl = [1]
        h = []
        primes = [2,3,5]
        for i,v in enumerate(primes):
            heapq.heappush(h,[v,i,0])
        
        
        while len(uwl) < n:
            cn = None
            while True:
                cn = heapq.heappop(h)
                cn[2]+=1
                if cn[0] != uwl[-1]:
                    uwl.append(cn[0])
                    heapq.heappush(h,[primes[cn[1]]*uwl[cn[2]],cn[1],cn[2]])
                    break
                heapq.heappush(h,[primes[cn[1]]*uwl[cn[2]],cn[1],cn[2]])
                
                    
                    
        return uwl[-1]