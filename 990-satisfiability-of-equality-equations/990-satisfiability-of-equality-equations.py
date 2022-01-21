class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        adj = defaultdict(list)
        
        
        def con(s):
            return ord(s)-ord('a')
        
        #steps
        #1 create connected componenets
        for eq in equations:
            if eq[1]=='=':
                a = con(eq[0])
                b = con(eq[-1])
                adj[a].append(b)
                adj[b].append(a)

        #2 assign values to components
        val = [None for i in range(26)]
        count = 0
        
        for i,v in enumerate(val):
            if v == None:
                q = [i]
                while q:
                    cn = q.pop()
                    if val[cn] == None:
                        val[cn] = count
                        q.extend(adj[cn])
        
            count += 1
            

        #3 check 
        for eq in equations:
            if eq[1]=='!':
                a = con(eq[0])
                b = con(eq[-1])
                if val[a] == val[b]:
                    return False
                
        return True