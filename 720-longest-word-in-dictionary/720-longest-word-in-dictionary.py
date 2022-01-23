class Solution:
    def longestWord(self, words: List[str]) -> str:
        d = Counter(words)
        max_l = float('-inf')
        
        def check(w,d):
            nw = len(w)
            for i in range(1,nw):
                if w[0:i] not in d:
                    return False
            return True
                
        ans = []
        for w in words:
            nw = len(w)
            if nw >= max_l:
                if check(w,d):
                    if nw > max_l:
                        max_l = nw
                        ans = [w]
                    else:
                        ans.append(w)
        
        if ans:
            ans.sort()
            return ans[0]
        else:
            return ""
                