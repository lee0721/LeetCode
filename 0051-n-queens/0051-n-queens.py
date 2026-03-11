class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        empty_board = [["."] * n for _ in range(n)]
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board
        def backtrack(row, diagonals, anti_diagoanals, cols, state):
            if row == n:
                ans.append(create_board(state))
                return
            for col in range(n):
                cur_diagonal = row - col
                cur_anti_diagonal = row + col
                if (
                    col in cols or
                    cur_diagonal in diagonals or
                    cur_anti_diagonal in anti_diagoanals
                ): continue
                cols.add(col)
                diagonals.add(cur_diagonal)
                anti_diagoanals.add(cur_anti_diagonal)
                state[row][col] = "Q"

                backtrack(row+1, diagonals, anti_diagoanals, cols, state)

                cols.remove(col)
                diagonals.remove(cur_diagonal)
                anti_diagoanals.remove(cur_anti_diagonal)
                state[row][col] = "."
        backtrack(0, set(), set(), set(), empty_board)
        return ans