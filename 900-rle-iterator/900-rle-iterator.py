class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.l = encoding  

    def next(self, n: int) -> int:
        
        if self.l:
            acc = self.l[0]
            
            while self.l and acc < n:
                self.l = self.l[2:]
                if self.l:
                    acc += self.l[0]
                else:
                    return -1
                
            if self.l:
                ret = self.l[1]
                if acc == n:
                    self.l = self.l[2:]
                else:
                    self.l[0] = acc - n
                return ret
        return -1
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)