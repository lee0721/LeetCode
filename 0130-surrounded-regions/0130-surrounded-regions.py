from itertools import product
class Solution:
    def dfs(self, board, row, col):
        if board[row][col] != "O":
            return
        board[row][col] = "E"
        if col < self.COLS - 1:
            self.dfs(board, row, col + 1)
        if row < self.ROWS - 1:
            self.dfs(board, row + 1, col)
        if col > 0:
            self.dfs(board, row, col - 1)
        if row > 0:
            self.dfs(board, row - 1, col)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        self.ROWS = len(board)
        self.COLS = len(board[0])

        borders = list(product(range(self.ROWS), [0, self.COLS - 1])) + list(
            product([0, self.ROWS - 1], range(self.COLS))
        )

        for row, col in borders:
            self.dfs(board, row, col)

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "E":
                    board[r][c] = "O"