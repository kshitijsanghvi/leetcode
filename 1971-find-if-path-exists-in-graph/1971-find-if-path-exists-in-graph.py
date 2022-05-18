class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        distance = {}
        parent = {}
        color = defaultdict(int)
        
        q = deque()
        distance[source] = 0
        parent[source] = None
        color[source] = 1
        q.append(source)
        
        while q:
            current_node = q.popleft()
            for next_node in adj_list[current_node]:
                if color[next_node] == 0:
                    color[next_node] = 1
                    parent[next_node] = current_node
                    distance[next_node] = distance[current_node] + 1
                    q.append(next_node)
            color[current_node] =2
        
        if color[destination] == 2:
            return True
        return False
        
        
        