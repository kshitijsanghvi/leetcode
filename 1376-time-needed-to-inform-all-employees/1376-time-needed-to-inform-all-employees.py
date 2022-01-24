class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        root = None
        
        for i,v in enumerate(manager):
            if v == -1:
                root = i
            adj[v].append(i)
            
        time = [0 for i in range(n)]
        q = [root]
        while q:
            cn = q.pop()
            
            for nn in adj[cn]:
                
                time[nn] = time[cn] + informTime[cn]
                q.append(nn)
        return max(time)