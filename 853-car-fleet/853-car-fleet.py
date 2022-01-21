class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = [[(target-i[0]), (target-i[0])/i[1]] for i in zip(position,speed)]
        t.sort(reverse=True)
        print(t)
        ans = 1
        for i in range(len(speed)-2,-1,-1):
            if t[i][1] <= t[i+1][1]:
                t[i][1] = t[i+1][1]
            else:
                ans+=1
                
        return ans
            
        
        