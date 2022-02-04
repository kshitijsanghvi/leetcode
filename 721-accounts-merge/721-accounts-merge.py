class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = {}
        adj = defaultdict(list)
        
        for i,record in enumerate(accounts):
            for em in record[1:]:
                if em in d:
                    adj[d[em]].append(i)
                    adj[i].append(d[em])
                else:
                    d[em] = i
                    
        v = [None for i in range(len(accounts))]
        final_ans = []
        for i in range(len(accounts)):
            if v[i] == None:
                v[i] = 1
                q = [i]
                ans = []
                while q:
                    cn = q.pop(0)
                    ans.extend(accounts[cn][1:])
                    for nn in adj[cn]:
                        if v[nn] == None:
                            v[nn] = 1
                            q.append(nn)
                ans = list(set(ans))
                ans.sort()
                ans = [accounts[i][0]] + ans
                final_ans.append(ans)
                
        return final_ans

