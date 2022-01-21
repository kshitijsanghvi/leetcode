class Solution:
    def differByOne(self, dicts: List[str]) -> bool:
        seen = {}
        nw = len(dicts[0])
        for w in dicts:
            for i in range(nw):
                t = w[:i] + '*' +w[i+1:]
                if t in seen:
                    return True
                else:
                    seen[t] = 1
        return False