class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        # Num + 1
        r = int(math.sqrt(num + 1))
        if r * r == num + 1:
            return [r,r]
        ans1 = math.inf
        ans2 = math.inf
        a1 = []
        a2 = []
        while r > 0:
            if (num + 1)//r * r == num + 1:
                a1 = [r, (num + 1)//r]
                ans1 = (num + 1)//r - r
                  
                break
            r -=1
        
        # Num + 2
        r = int(math.sqrt(num + 2))
        if r * r == num + 2:
            return [r,r]
        while r > 0:
            if (num + 2)//r * r == num + 2:
                a2 = [r, (num + 2)//r]
                ans2 = (num + 2)//r - r
                break
            r -=1
        
        return a1 if ans1 < ans2 else a2
        