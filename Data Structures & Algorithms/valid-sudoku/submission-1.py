class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for outside in range(9):
            for inside in range(9):
                if board[outside][inside] != ".":
                    if board[outside][inside] in rows[outside]:
                        return False
                    rows[outside].add(board[outside][inside])

                if board[inside][outside] != ".":
                    if board[inside][outside] in cols[outside]:
                        return False
                    cols[outside].add(board[inside][outside])

        boxes = [set() for _ in range(9)]
        start_col = 0
        start_row = 0
        for i in range(9):
            for j in range(3):
                for k in range(3):
                    if board[start_row + j][start_col + k] != ".":
                        if board[start_row + j][start_col + k] in boxes[i]:
                            return False
                        boxes[i].add(board[start_row + j][start_col + k])

            if i == 2 or i == 5:
                start_col = 0
                start_row += 3
            else:
                start_col += 3

        return True