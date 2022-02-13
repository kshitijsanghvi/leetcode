class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        nw = len(wordList[0])
        if endWord not in wordList:
            return 0
        
        for w in wordList:
            for i in range(nw):
                temp = w[:i] + '*' + w[i+1:]
                adj[temp].append(w)
                
        v = {}
        start = beginWord
        v[start] = 1
        q = [[start,1]]
        ans = []
        while q:
            cw,cd = q.pop(0)
            if cw == endWord:
                ans.append(cd)
                
            else:
                for i in range(nw):
                    for nn in adj[cw[:i]+'*'+cw[i+1:]]:
                        if nn not in v:
                            v[nn] = 1
                            q.append([nn,cd+1])
        return min(ans) if ans else 0
            