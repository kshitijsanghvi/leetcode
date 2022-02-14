class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        adj = defaultdict(list)
        nw = len(wordList[0])
        for w in wordList:
            for i in range(nw):
                t = w[:i] + '*' + w[i+1:]
                adj[t].append(w)
                
        q = [[beginWord,1,[beginWord]]]
        v = defaultdict(int)
        v[beginWord] = None
        soln = []        
        while q:
            
            new_q = []
            for ww in q:
                cw =ww[0]
                cd = ww[1]
                pref = ww[2]
                if cw == endWord:
                    soln.append(pref)
                for i in range(nw):
                    t = cw[:i] + '*' + cw[i+1:]
                    for nn in adj[t]:
                        if v[nn] == 0:
                            new_q.append([nn,cd+1,pref + [nn]])
            for n in new_q:
                v[n[0]] = 1
            q = new_q
                
        return soln