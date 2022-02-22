# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        isCelebrity = [i for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                if isCelebrity[i]!=-1 and i != j:
                    if knows(i,j):
                        isCelebrity[i] = -1
                    else:
                        isCelebrity[j] = -1
        
        def check(i):
            for j in range(n):
                if j != i:
                    if not knows(j,i):
                        return False
            return True
        
        for i in isCelebrity:
            if i != -1:
                if check(i):
                    return i
                
        return -1
                        
        
                