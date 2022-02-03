class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        

        uwl = [1]
        h = []
        for i, v in enumerate(primes):
            heapq.heappush(h, [v, i, 0])

        count = 1
        seen = set([])
        seen.add(1)
        while len(uwl) < n:
            flag = 0
            cn = None

            while flag == 0:
                cn = heapq.heappop(h)
                if cn[0] != uwl[-1]:
                    flag = 1
                else:
                    heapq.heappush(h, [primes[cn[1]] * uwl[cn[2] + 1], cn[1], cn[2] + 1])

            uwl.append(cn[0])
            heapq.heappush(h, [primes[cn[1]] * uwl[cn[2] + 1], cn[1],cn[2] + 1])

        return uwl[-1]
