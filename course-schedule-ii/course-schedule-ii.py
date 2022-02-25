class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        indegree = [0 for _ in range(n)]
        adj = defaultdict(list)
        
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
            
        root = [i for i,v in enumerate(indegree) if v == 0]
        v = [0 for i in range(n)]
        ans = []
        
        
        def ts(cn):
            for nn in adj[cn]:
                if v[nn] == 1:
                    return True
                elif v[nn] == 0:
                    v[nn] = 1
                    if ts(nn):
                        return True
            ans.append(cn)
            v[cn] = 2
            return False
                
        
        for r in root:
            v[r] = 1
            if ts(r):
                return []
            
        return ans[::-1] if min(v) == 2 else []