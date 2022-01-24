class Solution:
    def rotatedDigits(self, n: int) -> int:
        d = {}
        d[0] = 0
        d[1] = 1
        d[8] = 8
        d[2] = 5
        d[5] = 2
        d[6] = 9
        d[9] = 6
        
        def can_convert(a):
            a = list(str(a))
            a = [int(i) for i in a]
            for i in a:
                if i not in d:
                    return False
            return True
        
        def convert(a):
            a = list(str(a))
            a = [int(i) for i in a]
            for i,v in enumerate(a):
                a[i] = str(d[v])
                
            a = ''.join(a)
            return int(a)
        ans = 0
        for i in range(1,n+1):
            if can_convert(i):
                if i != convert(i):
                    ans+=1
                    
        return ans