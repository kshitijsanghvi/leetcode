class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = set()
        n = len(graph)
        color = [None] * n
        
    
        def dfs(n):
            nonlocal seen
            seen.add(n)
            for nn in graph[n]:
                if nn in seen:
                    if color[nn] == color[n]:
                        return False
                else:
                    color[nn] = (color[n] + 1) % 2
                    if not dfs(nn):
                        return False
            return True
        
        
        for i in range(n):
            if i not in seen:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
        