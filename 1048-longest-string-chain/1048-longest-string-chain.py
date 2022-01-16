class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        adj = {}
        n = len(words)
        v = [0 for i in range(n)]
        dp = {}
        for i in words:
            adj[i] = []
        
        for iw,w in enumerate(words):
            nw = len(w)
            for i in range(0,nw):
                ss = w[:i]+w[i+1:]
                if ss in adj:
                    adj[ss].append(iw)
        
        chain = float('-inf')
        
        def helper(i,adj,v):
            
            if i not in dp:
                v[i] = 1
                dp[i] = 1 + max([0]+[helper(j,adj,v) for j in adj[words[i]]])
            
            return dp[i]      
        
        for i,vi in enumerate(v):
            if vi == 0:
                chain = max(chain,helper(i,adj,v))
        
        return chain