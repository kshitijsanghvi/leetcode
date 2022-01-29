class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = defaultdict(list)
        
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
            
        v = {}
        v[0] = None
        
        q = deque()
        
        q.append(0)
        
        while q:
            cn =q.popleft()
            
            for nn in d[cn]:
                if nn in v and v[cn]!=nn:
                    return False
                else:
                    if nn not in v:
                        v[nn] = cn
                        q.append(nn)
        return True if len(v) == n else False