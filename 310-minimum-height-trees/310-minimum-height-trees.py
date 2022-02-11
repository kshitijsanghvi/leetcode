class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        leaves = None
        while n > 2:
            # print(adj)
            leaves = []
            for i in adj:
                if len(adj[i]) == 1:
                    leaves.append(i)
            
            n = n - len(leaves)
            
            for leaf in leaves:
                for p in adj[leaf]:
                    adj[p].remove(leaf)
                    del(adj[leaf])
            
        return [i for i in adj]