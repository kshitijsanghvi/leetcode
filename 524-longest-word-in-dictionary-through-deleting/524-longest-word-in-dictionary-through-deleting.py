class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # IOW find the longest lexi substring of s that is in dictionary
        
        h = [[-len(i),i] for i in dictionary]
        heapq.heapify(h)
        n = len(s)
        
        def check(cs):
            nonlocal n 
            i = 0 
            j = 0
            ncs = len(cs)
            
            for i in range(n):
                if s[i] == cs[j]:
                    j+=1
                    if j == ncs:
                        break
            if j == ncs:
                return True
            return False
        
        while h:
            cl,cs = heapq.heappop(h)
            if check(cs):
                return cs
        return ""