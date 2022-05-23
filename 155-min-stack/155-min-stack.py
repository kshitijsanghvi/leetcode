class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min.append([val,1])
        else:
            self.stack.append(val)
            if val >= self.min[-1][0]:
                self.min[-1][1] += 1
            else:
                self.min.append([val,1])
            
    def pop(self) -> None:
        self.stack.pop()
        self.min[-1][1] -= 1
        if self.min[-1][1] == 0:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()