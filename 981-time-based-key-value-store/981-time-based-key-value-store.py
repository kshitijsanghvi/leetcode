class TimeMap:

    def __init__(self):
        self.dkeys = defaultdict(dict)
        self.ts = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.dkeys[key]:
            bisect.insort(self.ts[key],timestamp)
            
        self.dkeys[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.dkeys[key]:
            return self.dkeys[key][timestamp]
 
        i = bisect.bisect(self.ts[key],timestamp) - 1
        return self.dkeys[key][self.ts[key][i]] if i!= -1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)