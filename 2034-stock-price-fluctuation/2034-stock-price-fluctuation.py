class StockPrice:

    def __init__(self):
        self.d ={}
        self.maxts = float('-inf')
        self.sortedvalue = []
        
    def update(self, timestamp: int, price: int) -> None:
        self.maxts = max(self.maxts,timestamp)
        if timestamp in self.d:
            idx = bisect.bisect_left(self.sortedvalue,[self.d[timestamp],])
            if self.sortedvalue[idx][1]==1:
                del(self.sortedvalue[idx])
            else:
                self.sortedvalue[idx][1]-=1
        self.d[timestamp] = price
        idx = bisect.bisect_left(self.sortedvalue,[price,])
        
        if idx < len(self.sortedvalue) and self.sortedvalue[idx][0] == price:
            self.sortedvalue[idx][1]+=1
        else:
            self.sortedvalue.insert(idx,[price,1])
        
        
    def current(self) -> int:
        return self.d[self.maxts]
        

    def maximum(self) -> int:
        return self.sortedvalue[-1][0]

    def minimum(self) -> int:
        return self.sortedvalue[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()