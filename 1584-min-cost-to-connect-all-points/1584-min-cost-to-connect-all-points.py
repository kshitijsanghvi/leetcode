class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        def compute_dist(p1,p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        h = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                heapq.heappush(h,[compute_dist(points[i],points[j]),[i,j]])
          
        n = len(points)
        parent = [i for i in range(n)]
        count = [1 for i in range(n)]
        
        def find(p):
            cpy = p
            while p != parent[p]:
                p= parent[p]
            parent[cpy] = p
            return p
        max_count = 0
        def union(p1,p2):
            nonlocal max_count
            cp1 = find(p1)
            cp2 = find(p2)
            parent[cp2] = cp1
            count[cp1]+=count[cp2]
            count[cp2] = 0
            parent[p1] = parent[p2] = cp1
            max_count = max(max_count,count[cp1])
        seen = set()
        ans = 0
        while max_count != len(points):
            d,[p1,p2] = heapq.heappop(h)
            if find(p1)!=find(p2):
                union(p1,p2)
                ans+=d
        return ans