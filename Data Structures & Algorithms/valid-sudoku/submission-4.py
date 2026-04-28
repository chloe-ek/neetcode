class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num != '.':
                    row_check = (num, i, 'row')
                    col_check = (num, j, 'col')
                    box_check = (num, i // 3, j // 3, 'box')

                    if row_check in seen or col_check in seen or box_check in seen:
                        return False
                
                    seen.add(row_check)
                    seen.add(col_check)
                    seen.add(box_check)

        return True
