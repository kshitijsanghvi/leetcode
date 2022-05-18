class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = collections.defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            
        color = [0] * n
        parent = [None] * n
        
        def dfs(current_node):
            color[current_node] = 1
            truth_values = []
            for next_node in adj[current_node]:
                if color[next_node] == 1:
                    truth_values.append(False)
 
                elif color[next_node] == 2:
                    truth_values.append(True)
                elif color[next_node] == 0:
                    parent[next_node] = current_node
                    truth_values.append(dfs(next_node))
                
                if truth_values[-1] == False:
                    return False
                
            color[current_node] = 2
            if truth_values:
                return True
            elif current_node != destination:
                return False
            else:
                return True
        
        return dfs(source)