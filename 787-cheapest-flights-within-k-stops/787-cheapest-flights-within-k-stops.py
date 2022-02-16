class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for frm,to,price in flights:
            adj[frm].append([to,price])
            
        v = {}
        h = [[0,src,0]]
        v[src] = [0,0]
        ans = []
        while h:
            cprice, cn, cstops = heapq.heappop(h)
            if cn == dst:
                 ans.append(cprice)
            else:
                nstops = cstops + 1
                if nstops <= k + 1:
                    for nn,nprice in adj[cn]:
                        if nn not in v or v[nn][0] > cprice + nprice or v[nn][1] > nstops:
                            v[nn] = [cprice + nprice,nstops]
                            heapq.heappush(h,[cprice + nprice, nn, nstops])
        return -1 if not ans else min(ans)