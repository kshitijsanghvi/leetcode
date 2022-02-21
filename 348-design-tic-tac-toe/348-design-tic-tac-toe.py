class TicTacToe:

    def __init__(self, n: int):
        self.row_count = [0 for i in range(n)]
        self.col_count = [0 for i in range(n)]
        self.diag1 = 0
        self.diag2 = 0
        self.n = n
    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        row_count = self.row_count
        col_count = self.col_count

        
        
        d = 1 if player==1 else -1
        row_count[row] += d
        if row_count[row] == n:
            return 1
        if row_count[row] == -n:
            return 2
        col_count[col]+=d
        if col_count[col] == n:
            return 1
        if col_count[col] == -n:
            return 2
        
        if row == col:
            self.diag1 +=d
        if self.diag1 == n:
            return 1
        if self.diag1 == -n:
            return 2
        
        if row + col == n - 1:
            self.diag2+=d
        if self.diag2 == n:
            return 1
        if self.diag2 == -n:
            return 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)