class DetectSquares:

    def __init__(self):
        self.xy = defaultdict(int)
    def add(self, point: List[int]) -> None:
        self.xy[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        px,py = tuple(point)
        ans = 0
        k = list(self.xy.keys())
        for (x,y) in k:
            if (x,y) != (px,py) and abs(px-x) == abs(py-y):
                ans += self.xy[(x,y)]*self.xy[(x,py)]*self.xy[(px,y)]
        return ans
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)