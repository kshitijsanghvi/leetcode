class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n <= 1:
            return 0
        termination_state = 2 ** n - 1
        queue = deque()
        v = {}
        for i in range(n):
            queue.append([i,1<<i,0])
            v[i,1<<i] = 1
        min_ans = math.inf
        while queue:
            cn,cs,cd = queue.popleft()
            if cs == termination_state:
                min_ans = min(min_ans,cd)
                continue
            for nn in graph[cn]:
                ns = cs | 1 << nn
                if (nn,ns) not in v:
                    v[nn,ns] = 1
                    queue.append([nn,ns,cd+1])
                    
        return min_ans