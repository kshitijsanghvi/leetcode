class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        adj = collections.defaultdict(list)
        
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        lowest_reach = [math.inf] * n
        color = [0] * n
        parent = [None] * n
        rank = [-math.inf] * n
        counter = 0
        ans = []
        def dfs(current_node):
            # print("Start : ",current_node)
            nonlocal ans, counter
            color[current_node] = 1
            rank[current_node] = lowest_reach[current_node] = counter
            counter += 1
            
            for next_node in adj[current_node]:
                if color[next_node] == 1 and next_node != parent[current_node]:
                    lowest_reach[current_node] = min(lowest_reach[current_node], lowest_reach[next_node])
                elif color[next_node] == 0:
                    parent[next_node] = current_node
                    low = dfs(next_node)
                    if low <= rank[current_node]:
                        lowest_reach[current_node] = min(lowest_reach[current_node],low)
                    else:
                        ans.append([current_node,next_node])
            color[current_node] = 2
            # print("End",current_node,lowest_reach)
            return lowest_reach[current_node]
                    
        dfs(0)
        return ans
                