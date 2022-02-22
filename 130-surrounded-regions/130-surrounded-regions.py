class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        if a group is not connected to edges it is surrounded 
        edges = x == 0 or m - 1 or y == 0 and n - 1

        """
        m, n = len(board), len(board[0])
        
        start = []
        for i in range(m):
            if board[i][0] == 'O':
                start.append([i,0])
            if board[i][n-1] == 'O':
                start.append([i,n-1])
                
        for j in range(n):
            if board[0][j] == 'O':
                start.append([0,j])
            if board[m-1][j] == 'O':
                start.append([m-1,j])
        
        for i,j in start:
            if board[i][j] == 'O':
                board[i][j] = 1
                q = [[i,j]]
                while q:
                    cx,cy = q.pop(0)
                    l = [cx,cy-1]
                    r = [cx,cy+1]
                    t = [cx-1,cy]
                    b = [cx+1,cy]
                    
                    for nx,ny in [l,r,t,b]:
                        if 0<=nx<m and 0 <= ny < n and board[nx][ny]=='O':
                            board[nx][ny] = 1
                            q.append([nx,ny])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 1:
                    board[i][j] = 'O'