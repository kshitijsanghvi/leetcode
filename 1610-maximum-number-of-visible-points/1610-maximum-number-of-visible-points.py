class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        ans = 0
        def compute_slope(p):
            angle =  math.atan2(p[1] - location[1], p[0]-location[0])
            if angle < 0:
                angle = math.pi*2 + angle
            return angle * 180/math.pi
            
        angles = [compute_slope(p) for p in points if p != location]
        extras = len(points) - len(angles)
        angles.sort()
        ans = 0
        angles += [a + 360 for a in angles if a + 360 <= angles[-1] + angle]
        if not angles:
            return extras
        print(angles)
        start = 0
        end = 0
        cutoff = angles[0] + angle
        count = 0
        max_count = 0
        while end < len(angles):
            
            while end < len(angles) and angles[end] <= cutoff:
                count += 1
                end+=1
            
        
            max_count = max(max_count,count)
            count -= 1
            start += 1 
            if start >= len(angles) or end == len(angles):
                break
            cutoff = angles[start] + angle
        print(extras)
        return max_count + extras   
        
        