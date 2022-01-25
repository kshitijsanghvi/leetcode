class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dr = {}
        ds = {}
        n = len(recipes)
        adj = defaultdict(list)
        
        c = 0
        for r in recipes:
            dr[r] = c
            c += 1
        for s in supplies:
            ds[s] = 1
            
        for i ,v in enumerate(ingredients):
            for j in v:
                if j in dr:
                    adj[dr[j]].append(i)
        
        
        def dfs(cn):
            nonlocal v
            nonlocal adj
            nonlocal ca
            v[cn] = 1
            for nn in adj[cn]:
                if nn not in v:
                    dfs(nn)
            ca.append(cn)
        
        ans = []
        v = {}
        for i in range(n):
            if i not in v:
                ca = []
                dfs(i)
                ans += ca
        
        # Important
        # Do not reverese this 
        
        ans = ans[::-1]
        canmake = defaultdict(bool)
        
        for i in ans:
            flag = True
            for j in ingredients[i]:
                if j in dr:
                    if canmake[dr[j]] == False:
                        canmake[i] = False
                        flag = False
                        break
                else:
                    if j not in ds:
                        canmake[i] = False
                        flag = False
                        break
            if flag:
                canmake[i] = True
        
        return [v for i,v in enumerate(recipes) if canmake[i] ==  True]
            
        