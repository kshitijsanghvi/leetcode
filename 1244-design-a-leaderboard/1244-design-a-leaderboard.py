class Leaderboard:

    def __init__(self):
        self.h = []
        self.d = {}
    def addScore(self, playerId: int, score: int) -> None:
        h = self.h
        d = self.d
        
        if playerId in d:
            for i,v in enumerate(h):
                if h[i][1] == playerId:
                    h[i][0] -= score
                
                parent = (i-1)//2
                while i!= 0 and h[parent][0] > h[i][0]:
                    h[parent],h[i] = h[i], h[parent]
                    i = parent
                    parent = (i-1)//2
        else:
            heapq.heappush(h,[-score, playerId])
            d[playerId] = 1

        self.h = h
        self.d = d
        
    def top(self, K: int) -> int:
        print(self.h)
        return -1 * sum(i[0] for i in heapq.nsmallest(K,self.h))

    def reset(self, playerId: int) -> None:
        for idx,i in enumerate(self.h):
            if i[1] == playerId:
                i[0] = 0
                
        heapq.heapify(self.h)
            


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)