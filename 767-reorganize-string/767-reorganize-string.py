class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(s)
        dl = [[d[i],i] for i in d]
        dl.sort(reverse=True)
   
        max_c = dl.pop(0)
        
        ans = [[max_c[1]] for _ in range(max_c[0]) ]
        
        r = sum(d.values()) - max_c[0]
        
        if r < max_c[0] - 1:
            return ""
        
        del(d[max_c[1]])
        
        keys = [i[1] for i in dl]
        i = 0
        j = 0
        print(keys)
        while r > 0:
            if d[keys[i]] == 0:
                i = (i + 1)%len(keys)
                continue
            else:
                d[keys[i]]-=1
                ans[j].append(keys[i])
                r-=1
                j = (j+1)%len(ans)
        ans_l = []
        for i in ans:
            ans_l.extend(i)
            
        return ''.join(ans_l)
                