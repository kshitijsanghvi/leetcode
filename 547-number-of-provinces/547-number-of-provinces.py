class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Approach 1: Disjoint set

        """
        
        
        def find(cn):
            cp = cn
            while parent[cn]!= cn:
                cn = parent[cn]
            parent[cp] = cn
            return cn
        
        def union(node1, node2):
            find1 = find(node1)
            find2 = find(node2)
            parent[find2] = find1
            parent[node1] = find1
            parent[node2] = find1
            
        
        n = len(isConnected)
        parent = [i for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    if find(i)!=find(j):
                        union(i,j)
                        
        count = 0
        for i in range(n):
            if parent[i] == i:
                count+=1
        return count