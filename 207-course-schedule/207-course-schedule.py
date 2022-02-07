class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        0 -> 1 <- 2
          <-
        '''

        adj = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            if a == b:
                return False
            adj[b].append(a)

        
        v = [0 for i in range(numCourses)]

        def dfs(cn,adj,v):
            for nn in adj[cn]:
                if v[nn] == 1:
                    return False
                elif v[nn]==0:
                    v[nn] = 1
                    res = dfs(nn,adj,v)
                    if not res:
                        return False
            v[cn] = 2
            return True

        for r in range(numCourses):
            if v[r]==0:
                v[r] = 1
                res = dfs(r,adj,v)
                if not res:
                    return False
                v[r] = 2

        return True 