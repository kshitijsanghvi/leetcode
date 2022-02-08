class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        ind = [0 for i in range(numCourses)]
        v = [0 for i in range(numCourses)]
        
        for a,b in prerequisites:
            adj[b].append(a)
            ind[a]+=1
            
        roots = []
        for i,a in enumerate(ind):
            if a == 0:
                roots.append(i)
        
        if not roots:
            return []
        
        ans = []
        
        def topologicalsort(r):
            for nn in adj[r]:
                if v[nn] == 1:
                    return True
                elif v[nn] == 0:
                    v[nn] = 1
                    if topologicalsort(nn):
                        return True
                    
            v[r] = 2
            ans.append(r)
                    
        
        for r in roots:
            v[r] = 1
            if topologicalsort(r):
                return []
        
        return ans[::-1] if min(v) == 2 else []
        