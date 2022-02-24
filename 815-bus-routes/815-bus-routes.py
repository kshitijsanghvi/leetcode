class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        Approach:
        1. Compute the avaible buses at each stop
        2. Start from source and use bfs
        3. Return the min stops
        
        """
        if source == target:
            return 0
        routes = [set(i) for i in routes]
        start_bus = set([i for i,v in enumerate(routes) if source in v])
        end_bus = set([i for i,v in enumerate(routes) if target in v])        
        adj = defaultdict(list)
        
        n = len(routes)
        for i in range(n):
            for j in range(i+1,n):
                if routes[i].intersection(routes[j]):
                    adj[i].append(j)
                    adj[j].append(i)

        q = [[i,0] for i in start_bus]
        v = {}
        
        for b,_ in q:
            v[b] = 0
        
        while q:
            cn,cd = q.pop(0)
            if cn in end_bus:
                return cd + 1
            
            nd = cd + 1
            for nn in adj[cn]:
                if nn not in v:
                    v[nn] = 1
                    q.append([nn,nd])
        return -1
        