class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def reduce(s):
            l = []
            for i in s:
                if i == '#':
                    if l:
                        l.pop()
                else:
                    l.append(i)
                    
            return l 
        
        return reduce(s) == reduce(t) 
                