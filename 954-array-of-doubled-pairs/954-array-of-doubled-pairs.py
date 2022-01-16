class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        d = Counter(arr)
        
        for i in sorted(arr):
            if i in d and 2 * i in d:
                d[2*i] -= 1
                d[i]-=1
                
                if d[i] == 0:
                    del(d[i])
                
                if d[i*2] == 0:
                    del(d[i*2])
            
            
        print(d)
        return False if d else True