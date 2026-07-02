class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

        # check columns
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

        # check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != ".":
                            if board[i][j] in seen:
                                return False
                            seen.add(board[i][j])

        return True