class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        
        flag = False
        
        d = defaultdict(list)
        nw = len(beginWord)
        for idx,w in enumerate(wordList):
            if w == endWord:
                flag = True
            for i in range(nw):
                d[w[:i] + '*' + w[i+1:]].append(idx)
        
        if flag:
            v = {}
            q = []
            for i in range(nw):
                for j in d[beginWord[:i] + '*' + beginWord[i+1:]]:
                    if j not in v:
                        v[j] = 1
                        q.append([j,2])
            while q:
                cn,cd = q.pop(0)
                if wordList[cn] == endWord:
                    return cd
                else:
                    cw = wordList[cn]
                    for i in range(nw):
                        for nn in d[cw[:i] + '*' + cw[i+1:]]:
                            if nn not in v:
                                v[nn] = 1
                                q.append([nn,cd+1])
                    

            return 0
        
        return 0