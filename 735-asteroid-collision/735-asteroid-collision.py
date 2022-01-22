class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a = asteroids
        prev = [a[0]]
        n = len(a)
        
        def rev(p,a):
            while p and p[-1]*a < 0:
                if abs(a) == abs(p[-1]):
                    p.pop()
                    return 
                elif abs(a) > abs(p[-1]):
                    p.pop()
                else:
                    return
           
            prev.append(a)
                
        for i in range(1,n):
            if prev:
                if prev[-1] < 0 or prev[-1]*a[i] > 0:
                    prev.append(a[i])
                
                elif abs(prev[-1]) <= abs(a[i]):
                    rev(prev,a[i])
            
            else:
                prev.append(a[i])
        
        return prev