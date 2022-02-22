class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        
        for i in range(m):
            for j in range(n):
                
                l = [i,j-1]
                r = [i,j+1]
                t = [i-1,j]
                b = [i+1,j]
                tl = [i-1,j-1]
                tr = [i-1,j+1]
                bl = [i+1,j-1]
                br = [i+1,j+1]
                
                valid = 0
                alive = 0
                for ni,nj in[l,r,t,b,tl,tr,bl,br]:
                    if 0 <= ni < m and 0<=nj<n:
                        valid+=1
                        if abs(board[ni][nj]) == 1:
                            alive +=1
                dead = valid - alive
                if board[i][j] == 1:
                    if alive != 2 and alive != 3:
                        board[i][j] = -1
                else:
                    if alive == 3:
                        board[i][j] = 2
                        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
                        
        
                        
                    
                