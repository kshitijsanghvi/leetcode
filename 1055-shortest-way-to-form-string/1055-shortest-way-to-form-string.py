class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n = len(source)
        m = len(target)
        
        i = 0 
        j = 0
        count = 1
        d = Counter(source)
        
        while j < m:
            if target[j] not in d:
                return -1
            if i >= n:
                count+=1
                i = 0
                
            while i < n and source[i]!=target[j]:
                i+=1
            
            if i < n:
                j+=1
                
            i+=1
            
        return count