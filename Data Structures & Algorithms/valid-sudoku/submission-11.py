class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for i in range(0, rows):
            board_check = set()
            for j in range(0, cols):
                val = board[i][j]

                if val == '.':
                    continue

                if val in board_check:
                    return False
                else:
                    board_check.add(val)

        for j in range(0, cols):
            board_check = set()
            for i in range(0, rows):
                val = board[i][j]

                if val == '.':
                    continue

                if val in board_check:
                    return False
                else:
                    board_check.add(val)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                board_check = set()
                
                for r in range(3):
                    for c in range(3):
                        val = board[i + r][j + c]

                        if val == '.':
                            continue

                        if val in board_check:
                            return False
                        else:
                            board_check.add(val)

        

        return True



                

