class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        adj = defaultdict(list)
        for i in range(n):
            adj[tuple(sorted(strs[i]))].append(i)
        
        final_ans = []
        for i in adj:
            ans = []
            for j in adj[i]:
                ans.append(strs[j])
            final_ans.append(ans)
        return final_ans

#         n = len(d)
#         v = [None for i in range(n)]
#         keys = [i for in d]
#         final_ans = []
#         for i in range(n):
#             if v[i] == None:
#                 v[i] = 1
#                 q = [i]
#                 ans = []
#                 while q:
#                     cn = q.pop()
#                     ans.append(strs[cn])
#                     for nn in adj[cn]:
#                         if v[nn] == None:
#                             v[nn] = 1
#                             q.append(nn)
#                 final_ans.append(ans)
        
#         return final_ans