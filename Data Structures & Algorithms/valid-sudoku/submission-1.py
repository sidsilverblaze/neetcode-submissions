from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_d = defaultdict(set)
        column_d = defaultdict(set)
        square_d = defaultdict(set)
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                if ((board[i][j] in row_d[i]) or (board[i][j] in column_d[j]) or (board[i][j] in square_d[(i//3,j//3)])):
                    return False
                else:
                   row_d[i].add(board[i][j])
                   column_d[j].add(board[i][j])
                   square_d[(i//3,j//3)].add(board[i][j])
                   
        return True


        