class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(list) # Use Counter only for deafultdict(int)
        s = ''.join(words)
        d = Counter(s)
        n = len(words)
        
        for i in range(1,n):
            j = 0
            while j < min(len(words[i-1]),len(words[i])) and words[i-1][j] == words[i][j]:
                j+=1
                
            if j == len(words[i]) and len(words[i-1]) > j:
                return ""
            
            if j < min(len(words[i-1]),len(words[i])):
                adj[words[i-1][j]].append(words[i][j])
                
            
                       
        v = {}
        
        def toposort(cn):
            for nn in adj[cn]:
                if nn in v and v[nn] == 1:
                    return True
                elif nn not in v:
                    v[nn] = 1
                    if toposort(nn):
                        return True
            v[cn] = 2
            ans.append(cn)
            
        if len(d) == 1:
            return words[0]
        # if not adj:
        #     return ""
        ans = []
        for r in d.keys():
            if r not in v:
                v[r] = 1
                if toposort(r):
                    return ""
        return ''.join(ans[::-1])