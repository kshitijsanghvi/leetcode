class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        def d(p1,p2):
            return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        ans = 0
        for p0 in points:
            dist = [d(p0,p1) for p1 in points]
            
            c = Counter(dist)
            for pd in c :
                if pd != 0 and c[pd]>1:
                    ans+=math.factorial(c[pd])/math.factorial(c[pd]-2)
                    
        return int(ans) 
        