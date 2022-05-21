class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def cd(x,y):
            return math.sqrt(x**2 + y ** 2)
        
        h = []
        
        for i,p in enumerate(points):
            heapq.heappush(h,[-cd(p[0],p[1]),i])
            if len(h) > k:
                heapq.heappop(h)
                
        return [points[i[1]] for i in h]    
                