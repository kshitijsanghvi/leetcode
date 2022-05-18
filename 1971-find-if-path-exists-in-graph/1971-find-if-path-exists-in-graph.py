class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = collections.defaultdict(list)
        
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        parent = [None] * n
        start = [None] * n
        finish = [None] * n
        color = [0] * n
        time = 0
        
        def dfs_visit(current_node):
            nonlocal time    
            color[current_node] = 1
            time += 1
            start[current_node] = time
            
            for next_node in adj_list[current_node]:
                if color[next_node] == 0:
                    parent[next_node] = current_node 
                    dfs_visit(next_node)
            
            time += 1
            finish[current_node] = time
            color[current_node] = 2
            
        dfs_visit(source)
        return color[destination] == 2
                    