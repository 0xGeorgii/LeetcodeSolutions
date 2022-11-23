class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def is_line_valid(arr):
            s = "".join(arr).replace(".", "")
            return len(set(s)) == len(s)

        for i in range(9):
            row = board[i]
            if not is_line_valid(row):
                return False
            col = []
            for j in range(9):
                col.append(
                    board[j][i]
                )
            if not is_line_valid(col):
                return False
        
        
        blocks = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not is_line_valid(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]):
                    return False

        return True
