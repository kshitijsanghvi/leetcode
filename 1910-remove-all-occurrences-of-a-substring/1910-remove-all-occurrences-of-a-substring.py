class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = []
        
        i = 0
        n = len(s)
        
        prev = None
        while prev != len(ans):
            prev = len(ans)
            ans = []
            n = len(s)
            i = 0
            while i < len(s):
                if s[i] == part[0]:
                    if s[i:i + len(part)] == part:
                        i += len(part)
                        break

                ans.append(s[i])
                i+=1
            while i < n:
                ans.append(s[i])
                i+=1
            s = ''.join(ans)
                     
        return s