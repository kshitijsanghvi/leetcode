class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        
        def dfs(ci,cj,word,i,v):
            if i == len(word):
                return True
            else:
                l = [ci,cj-1]
                r = [ci,cj+1]
                t = [ci-1,cj]
                b = [ci+1,cj]
                for ni,nj in [l,r,t,b]:
                    if 0 <= ni < m and 0<= nj < n and v[ni,nj] == 0 and board[ni][nj]==word[i]:
                        v[ni,nj] = 1
                        if dfs(ni,nj,word,i+1,v):
                            return True
            v[ci,cj] = 0
            return False
                        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    v = defaultdict(int)
                    v[i,j] = 1
                    if dfs(i,j,word,1,v):
                        return True
                    v[i,j] = 0
        return False