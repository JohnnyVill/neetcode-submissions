class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = rows = len(board)
        ROWS = defaultdict(list)
        COLS = defaultdict(list)
        boardDict = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in ROWS[i]:
                    return False
                elif board[i][j] != '.':
                    ROWS[i].append(board[i][j])
                
                if board[j][i] in COLS[i]:
                    return False
                elif board[j][i] != '.':
                    COLS[i].append(board[j][i])
                
                if board[i][j] in boardDict[(i//3,j//3)]:
                    return False
                elif board[i][j] != '.':
                    boardDict[(i//3,j//3)].append(board[i][j])                    
    
        return True
                
        