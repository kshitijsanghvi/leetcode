class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.arr = []
        for v in vec:
            self.arr.extend(v)
        self.arr = self.arr[::-1]

    def next(self) -> int:
        return self.arr.pop()

    def hasNext(self) -> bool:
        return len(self.arr) > 0 


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()