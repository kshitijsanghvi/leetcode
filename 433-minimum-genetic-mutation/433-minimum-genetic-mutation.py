class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        d = {}
        bank.append(start)
        for i,v in enumerate(bank):
            d[v] = i
            
        adj = defaultdict(list)
        n = len(bank)
        
        def check(i,j):
            s1 = bank[i]
            s2 = bank[j]
            d =  0
            for i in range(8):
                if s1[i]!=s2[i]:
                    d+=1
            return True if d == 1 else False
        
        for i in range(n):
            for j in range(i+1,n):
                if check(i,j):
                    adj[i].append(j)
                    adj[j].append(i)
        
        
        start = d[start]
        #Edge Case
        if end not in d:
            return -1    
        end = d[end]
        v = {}
        v[start] = 1
        q = deque()
        q.append([start,0])
        
        
        
        while q:
            [cn,cd] = q.popleft()
            if cn == end:
                return cd
            else:
                for nn in adj[cn]:
                    if nn not in v:
                        v[nn] = 1
                        q.append([nn,cd+1])
        
        return -1