class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        if self.stack_1:
            self.stack_1.append(x)
        elif self.stack_2:
            while self.stack_2:
                self.stack_1.append(self.stack_2.pop())
            self.stack_1.append(x)
        else:
            self.stack_1.append(x)
        
    def pop(self) -> int:
        if self.stack_2:
            return self.stack_2.pop()
        elif self.stack_1:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()
        else:
            return None

    def peek(self) -> int:
        if self.stack_2:
            return self.stack_2[-1]
        elif self.stack_1:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2[-1]
        else:
            return None
        

    def empty(self) -> bool:
        if not self.stack_1 and not self.stack_2:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()