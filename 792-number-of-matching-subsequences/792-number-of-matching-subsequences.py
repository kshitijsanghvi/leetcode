class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(list)
        for w in words:
            d[w[0]].append(w)
        ans = 0
        for c in s:
            temp = []
            for w in d[c]:
                if len(w) == 1:
                    ans += 1
                else:
                    nw = w[1:]
                    if nw[0] == c:
                        temp.append(nw)
                    else:
                        d[nw[0]].append(nw)
            d[c] = temp
        return ans