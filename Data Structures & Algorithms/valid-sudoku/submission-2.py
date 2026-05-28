class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for i in range(0, len(board)):
            rows[i] = set()
            cols[i] = set()

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):

                square_key = (i//3, j//3)
                if square_key not in squares:
                    squares[square_key] = set()

                curr_val = board[i][j]

                if curr_val != '.':
                    if curr_val in rows[i] or curr_val in cols[j] or curr_val in squares[square_key]:
                        return False
                    else:
                        rows[i].add(curr_val)
                        cols[j].add(curr_val)
                        squares[square_key].add(curr_val)

        return True

        