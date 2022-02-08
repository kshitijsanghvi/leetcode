class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        
        dp = [[(i,j) for j in range(n)] for i in range(m)]
        
        def union(nx,ny,i,j):
            ci,cj = i,j
            while dp[i][j] != (i,j):
                (i,j) = dp[i][j]
            dp[i][j] = (nx,ny)
            dp[ci][cj] = (nx,ny)
            
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    t = [i - 1, j]
                    l = [i , j - 1]
                    for nx,ny in [t,l]:
                        if 0 <= nx < m and 0<= ny< n and board[nx][ny] == 'X':
                            union(nx,ny,i,j)
        ans = 0    
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X' and dp[i][j]==(i,j):
                    ans += 1
        return ans
                            