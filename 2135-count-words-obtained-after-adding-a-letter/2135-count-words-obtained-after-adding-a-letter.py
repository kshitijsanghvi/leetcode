class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        d = {}
        for w in startWords:
            w=''.join(sorted(w))
            d[w] = 1
        
        count = 0
        for t in targetWords:
            t = ''.join(sorted(t))
            for i in range(len(t)):
                if t[:i] + t[i+1:] in d:
                    count+=1
                    break
        return count