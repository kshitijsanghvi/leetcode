class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        color = [None for _ in range(n+1)]
        
        if n <= 4:
            return [i+1 for i in range(n)]
        
        adj = defaultdict(list)
        for i in paths:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
            
        for i in range(1,n+1):
            if color[i] == None:
                color[i] = 1
                
                q = deque(adj[i])      
                while q:
                    cn = q.popleft()
                    if color[cn] == None:
                        l = [1,2,3,4]
                        for nn in adj[cn]:
                            # Trying to remove color again
                            if color[nn] != None and color[nn] in l:
                                l.remove(color[nn])
                            else:
                                q.append(nn)
                        color[cn] = l[0]
        
        return color[1:]