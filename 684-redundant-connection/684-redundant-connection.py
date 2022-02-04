class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = 1000
        parent = [i for i in range(n+1)]
    
        
        def union(n1,n2):
            rep1 = find(n1)
            rep2 = find(n2)
            if rep1 != rep2:
                parent[rep1] = rep2
                return True
            else:
                return False
            
        def find(n):
            while parent[n] != n:
                n = parent[n]
            return n
        
        for e in edges:
            if union(e[0],e[1]):
                continue
            else:
                return e
        return []