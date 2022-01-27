class MyCalendar:

    def __init__(self):
        self.l = []
        
    def book(self, start: int, end: int) -> bool:
        if len(self.l)==0:
            self.l.append([start,end])
            return True
        else:
            idx = bisect.bisect(self.l,[start,])
            if idx == 0:
                if end > self.l[idx][0]:
                    return False
                else:
                    self.l.insert(idx,[start,end])
                    return True
            if idx == len(self.l):
                if start >= self.l[idx-1][1]:
                    self.l.append([start,end])
                    return True
                else:
                    return False
            else:
                if end <= self.l[idx][0] and start >= self.l[idx-1][1]:
                    self.l.insert(idx,[start,end])
                    return True
                else:
                    return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)