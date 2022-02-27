class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)
        for i,[x,y] in enumerate(equations):
            d[x].append([y,values[i]])
            d[y].append([x,1/values[i]])
        
        ans = []            
        for num,den in queries:
            if num not in d or den not in d:
                ans.append(-1)
                continue
            if num == den:
                ans.append(1)
                continue

            q = deque()
            q.append([num,1])
            seen = set()
            seen.add(num)
            flag = True
            while q:
                cn,cans = q.popleft()
                if cn == den:
                    flag = False
                    ans.append(cans)
                    break
                for nn,nval in d[cn]:
                    if nn not in seen:
                        seen.add(nn)
                        q.append([nn,nval*cans])
            if flag:
                ans.append(-1) 
        return ans