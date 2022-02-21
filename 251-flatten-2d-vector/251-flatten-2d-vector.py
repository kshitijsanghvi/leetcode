class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.v = vec
        self.i = 0
        self.j = 0
        
    def next(self) -> int:
        ans = None
        if self.j < len(self.v[self.i]):
            ans = self.v[self.i][self.j]
            self.j += 1
        else:
            self.i +=1
            while not self.v[self.i]:
                self.i +=1
                
            self.j = 0
            ans = self.v[self.i][self.j]
            self.j+=1
        return ans
        
        
    def hasNext(self) -> bool:
        if len(self.v) == 0:
            return False
        if self.j < len(self.v[self.i]):
            return True
        else:
            temp_i = self.i + 1
            while temp_i < len(self.v) and not self.v[temp_i]:
                temp_i +=1
                
        return False if temp_i == len(self.v) else True
        

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()