class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        p = {}
        child = defaultdict(list)
        
        for i,v in enumerate(ppid):
            p[pid[i]] = v
            child[v].append(pid[i])
        
        if p[kill] == 0:
            return pid
        
        v = {}
        
        v[kill] = 1
        q = [kill]
        ans = []
        while q:
            cn = q.pop()
            ans.append(cn)
            for nn in child[cn]:
                if nn not in v:
                    v[nn] = 1
                    q.append(nn)
                    
        return ans