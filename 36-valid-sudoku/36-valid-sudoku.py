class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for i in range(9)]
        col = [{} for i in range(9)]
        box = [{} for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row[i]:
                        return False
                    else:
                        row[i][board[i][j]] = 1
                    if board[i][j] in col[j]:
                        return False
                    else:
                        col[j][board[i][j]] = 1
                    if board[i][j] in box[(i//3)*3 + (j//3)]:
                        # print(box[(i//3)*3 + (j//3)],board[i][j])
                        return False
                    else:
                        box[(i//3)*3 + (j//3)][board[i][j]] = 1

        return True
                