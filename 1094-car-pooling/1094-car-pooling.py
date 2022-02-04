class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips = [[pickup,+1,nop] for nop,pickup,_ in trips] + [[drop,-1,nop] for nop,_,drop in trips]
        
        trips.sort()
        
        
        pass_count = 0
        for _, s, n in trips:
            if s == 1:
                pass_count+=n
                if pass_count > capacity:
                    return False
            else:
                pass_count -= n
        
        return True
                