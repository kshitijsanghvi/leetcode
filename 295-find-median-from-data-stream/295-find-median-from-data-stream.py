class MedianFinder:

    def __init__(self):
        self.counter = 0
        self.h1 = []
        self.h2 = []
        self.median = math.inf
    def addNum(self, num: int) -> None:
        if self.h2 and num < self.h2[0]:
            heapq.heappush(self.h1,-num)
        else:
            heapq.heappush(self.h2,num)
        
        if len(self.h1) > len(self.h2) + 1:
            temp = -1 * heapq.heappop(self.h1)
            heapq.heappush(self.h2,temp)
        elif len(self.h2) > len(self.h1) + 1:
            temp = heapq.heappop(self.h2)
            heapq.heappush(self.h1,-temp)

    def findMedian(self) -> float:
        if len(self.h1) == len(self.h2):
            return (-self.h1[0] + self.h2[0])/2
        elif len(self.h1) > len(self.h2):
            return -self.h1[0]
        return self.h2[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()