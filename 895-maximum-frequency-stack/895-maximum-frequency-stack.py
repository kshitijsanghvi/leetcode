class FreqStack:

    def __init__(self):
        self.register = defaultdict(list)
        self.max_f = -math.inf
        self.counter = Counter()
        self.max_stack = []
    def push(self, val: int) -> None:
        
        self.counter[val]+=1
        self.register[self.counter[val]].append(val)
        if self.counter[val] > self.max_f:
            self.max_f = self.counter[val]
            self.max_stack.append(self.max_f)
            
    def pop(self) -> int:
        
        while not self.register[self.max_f]:
            self.max_f -=1
            
        element = self.register[self.max_f].pop()
        self.counter[element] -=1
        return element


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()