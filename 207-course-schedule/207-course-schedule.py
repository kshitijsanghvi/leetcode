class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        v = [0 for i in range(numCourses)]
        adj = defaultdict(list)
        
        for a,b in prerequisites:
            if a == b:
                return False
            adj[b].append(a)
            
            
        def ts(cn):
            for nn in adj[cn]:
                if v[nn] == 1:
                    return True
                elif v[nn] == 0:
                    v[nn] = 1
                    if ts(nn):
                        return True
            v[cn] = 2
            
                
        for i in range(numCourses):
            if v[i] == 0:
                v[i] = 1
                if ts(i):
                    return False
                v[i] = 2
                
        return True