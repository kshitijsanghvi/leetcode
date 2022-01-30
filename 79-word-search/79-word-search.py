class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        nw = len(word)
        
        
        def dfs(cx,cy,ci):
            nonlocal nw
            nonlocal v
            if ci == (nw - 1):
                return True
            else:
                l = (cx,cy-1)
                r = (cx,cy+1)
                t = (cx-1,cy)
                b = (cx+1,cy)

                ni = ci + 1
                for nx,ny in [l,r,t,b]:
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[ni] and (nx,ny) not in v:
                        v[nx,ny] = 1                     
                        r = dfs(nx,ny,ni)
                        del(v[nx,ny])
                        if r:
                            return True
                return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    
                    v = {}
                    v[i,j] = 1
                    if dfs(i,j,0):
                        return True
                    
                    
        return False