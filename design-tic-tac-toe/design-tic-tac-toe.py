class TicTacToe:

    def __init__(self, n: int):
        self.board = [[None for _ in range(n)] for _ in range(n)]
        self.n = n
    def check_col(self,col,player):
        for i in range(self.n):
            if self.board[i][col] != player:
                return False
        return True
    def check_row(self,row,player):
        for i in range(self.n):
            if self.board[row][i] != player:
                return False
        return True
    
    def check_ld(self,player):
        for i in range(self.n):
            if self.board[i][i] != player:
                return False
        return True
    def check_rd(self,player):
        for i in range(self.n):
            if self.board[i][self.n - i -1] != player:
                return False
        return True
    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        #check col
        if self.check_col(col,player):
            return player
        #check row
        if self.check_row(row,player):
            return player
        
        #check l d
        if row == col:
            if self.check_ld(player):
                return player
        #check r d
        if row + col == self.n - 1:
            if self.check_rd(player):
                return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)