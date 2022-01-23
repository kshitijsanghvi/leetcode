class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 24 hour clock
        # return minimum minutes difference 
        def compute_min(t):
            h,m = t.split(':')
            return int(h)*60 + int(m)
        
        timePoints = list(map(compute_min,timePoints))
        timePoints.sort()
        min_v = (1440-timePoints[-1]) + timePoints[0]
        n = len(timePoints)
        for i in range(n-1):
            min_v = min(timePoints[i+1]-timePoints[i],min_v)
        return min_v
            