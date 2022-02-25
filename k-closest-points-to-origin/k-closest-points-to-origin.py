class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def compute_dist(i):
            x,y=i
            return sqrt(x**2 + y**2)
        d = list(map(compute_dist,points))
        d = [[v,i] for i,v in enumerate(d)]
        return [points[i[1]] for i in heapq.nsmallest(k,d)]
        
        
            
            