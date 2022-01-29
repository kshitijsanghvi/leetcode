class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # K stops -> path length : k + 1
        # Create a min heap based on price
        # Prune node that have reached the stop limit
        # Heapify on sum of cost
        
        h = [[0,-1,src]]
        v = {}
        v[src] = [0,-1]
        d = defaultdict(list)

        for i in flights:
            d[i[0]].append([i[1],i[2]])
        
        while h:
            cp,cs,cn = heapq.heappop(h)
            if cn == dst:
                return cp
            # check dest before
            if cs >= k:
                continue
                

            
            else:
                for nn,p in d[cn]:
                    if nn not in v or v[nn][0] > cp + p or v[nn][1] > cs+1:

                        v[nn] = [cp + p,cs+1]
                        heapq.heappush(h,[cp+p,cs+1,nn])

        return -1
                
                