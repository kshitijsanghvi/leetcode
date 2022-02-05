class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        
        for e in times:
            adj[e[0]].append([e[1],e[2]])
            
        v = [-1 for i in range(n+1)]
        v[0] = 0
        ans = -1
        q = [[0,k]]
        v[k] = 0
        while q:
            ct,cn = heapq.heappop(q)
            ans = max(ans,ct)
            
            for nn,nt in adj[cn]:
                if v[nn] == -1 or v[nn] > ct+nt:
                    v[nn] = ct + nt
                    heapq.heappush(q,[ct+nt,nn])
            
        return -1 if min(v) == -1 else max(v) 
                        
        