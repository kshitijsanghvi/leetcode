class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def di(p0,p1):
            return math.sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)
        
        def precision(v):
            return int(v * 10000)
        
        points = [p1,p2,p3,p4]
        
        dist = [di(p1,p) for p in points]
        points = list(zip(dist,points))
        points.sort()
        d = [i[0] for i in points]
        points = [i[1] for i in points]
        
        # check for side length
        
        
        if d[1]== 0.0 or precision(d[1]) != precision(d[2]) or precision(di(points[1],points[-1])) != precision(d[1]) or precision(di(points[2],points[-1])) != precision(d[1]) :
            return False
        if precision(math.sqrt(2)*d[1]) != precision(d[-1]):
            return False
        
        if precision(di(points[1],points[2])) != precision(d[-1]):
            return False
        
        return True