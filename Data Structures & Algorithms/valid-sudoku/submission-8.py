class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            row_check_box = set()
            for col in range(cols):
                val = board[row][col]
                if val == '.':
                    continue
                if val in row_check_box:
                    return False
                row_check_box.add(val)

        for col in range(cols):
            col_check_box = set()
            for row in range(rows):
                val = board[row][col]
                if val == '.':
                    continue
                if val in col_check_box:
                    return False
                col_check_box.add(val)

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_check = set()

                for r in range(3):
                    for c in range(3):
                        val = board[box_row + r][box_col + c]

                        if val == '.':
                            continue

                        if val in box_check:
                            return False

                        box_check.add(val)

        return True
        

