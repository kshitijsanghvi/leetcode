class UndergroundSystem:

    def __init__(self):
        self.totaltime = defaultdict(int)
        self.count = defaultdict(int)
        self.entry = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.entry[id] = [t,stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        t_start,start_station = self.entry[id]
        self.totaltime[start_station,stationName]+= t - t_start
        self.count[start_station,stationName]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.totaltime[startStation,endStation]/self.count[startStation,endStation]

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)