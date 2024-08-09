class Solution(object):
    def solveNQueens(self, n):
        def solve(col, board, ans, leftRow, upperDiagonal, lowerDiagonal):
            if col == n:
                ans.append(["".join(row) for row in board])
                return
            for row in range(n):
                if leftRow[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[n - 1 + col - row] == 0:
                    board[row][col] = 'Q'
                    leftRow[row] = 1
                    lowerDiagonal[row + col] = 1
                    upperDiagonal[n - 1 + col - row] = 1
                    solve(col + 1, board, ans, leftRow, upperDiagonal, lowerDiagonal)
                    board[row][col] = '.'
                    leftRow[row] = 0
                    lowerDiagonal[row + col] = 0
                    upperDiagonal[n - 1 + col - row] = 0

        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]
        leftRow = [0] * n
        upperDiagonal = [0] * (2 * n - 1)
        lowerDiagonal = [0] * (2 * n - 1)
        solve(0, board, ans, leftRow, upperDiagonal, lowerDiagonal)
        return ans

        