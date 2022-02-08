class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        
        dp = [[(i,j) for j in range(n)] for i in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if i > 0 and board[i-1][j] == 'X':
                        continue
                
                    if j > 0 and board[i][j-1] == 'X':
                        continue
                        
                    else:
                        count+=1
        return count

                            