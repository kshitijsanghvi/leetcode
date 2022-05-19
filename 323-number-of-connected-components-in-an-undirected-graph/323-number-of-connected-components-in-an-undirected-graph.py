class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        color = [0] * n
        
        def bfs(i):
            nonlocal color
            q = deque()
            q.append(i)
            color[i] = 1
            while q:
                cn = q.popleft()
                for nn in adj[cn]:
                    if color[nn] == 0:
                        q.append(nn)
                color[cn] = 2
        ans = 0
        
        def dfs(cn):
            color[cn] = 1
            for nn in adj[cn]:
                if color[nn] == 0:
                    dfs(nn)
            color[cn] = 2
        
        for i in range(n):
            if color[i] == 0:
                ans += 1
                dfs(i)
                
        return ans