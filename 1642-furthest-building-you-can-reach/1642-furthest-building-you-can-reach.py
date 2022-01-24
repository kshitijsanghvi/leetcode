class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        n = len(heights)
        if n == 1:
            return 0
        
        for i in range(1,n):
            d = heights[i] - heights[i-1]
            if d > 0:
                if ladders > 0:
                    ladders-=1
                    heapq.heappush(h,d)
                else:
                    if h and d > h[0]:
                        
                        if bricks >= h[0]:
                            bricks = bricks - h[0]
                            heapq.heappop(h)
                            heapq.heappush(h,d)
                            
                        else:
                            return i-1
                    
                    else:
                        if bricks < d:
                            return i - 1
                        else:
                            bricks = bricks - d
        return n-1
            