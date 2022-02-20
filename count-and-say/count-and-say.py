class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        else:
            prev = self.countAndSay(n - 1)
            
            i = prev[0]
            c = 1
            cans = ""
            for v in prev[1:]:
                if i == v:
                    c +=1
                else:
                    cans = cans + str(c) + i
                    c = 1
                    i = v
            cans += str(c) + i
                
            return cans