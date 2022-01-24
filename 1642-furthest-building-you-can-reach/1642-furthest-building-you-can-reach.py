class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        d = [0]
        h = heights
        n = len(h)
        
        for i in range(1,n):
            dif = h[i] - h[i-1]
            if dif > 0:
                d.append(dif)
            else:
                d.append(0)
                

        l = 0 
        r = n -1 
        
        while l < r-1:
            mid = l + (r - l)//2
            
            d_a = d[:mid+1]
            d_a.sort()
            if ladders!= 0:
                d_a = d_a[:-1*ladders]
            
            if bricks >= sum(d_a):
                l = mid
            else:
                r = mid - 1

        d_a = d[:r+1]
        d_a.sort()
        if ladders!= 0:
            d_a = d_a[:-1*ladders]
                
        if bricks >= sum(d_a):
            return r
        return l
            
                
        