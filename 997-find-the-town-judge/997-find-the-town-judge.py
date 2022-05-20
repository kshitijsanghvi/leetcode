class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        out degree = 0
        in degree = n - 1
        exactly one 
        
        """
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        
        for u,v in trust:
            outdegree[u] += 1
            indegree[v] += 1
            
            
        count = 0
        ii = None
        for i in range(1, n+1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                count += 1
                if count == 1:
                    ii = i
        return ii if count == 1 else -1