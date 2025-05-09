class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[]] * n
        for i in range(n):
            self.board[i] = [0] * n        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        rowResult = self.scanRows()
        colResult = self.scanCols()
        diagonalResult = self.scanDiagonal()
        antiDiagonalRsult = self.scanAntiDiagonal()

        if rowResult > 0:
            return rowResult
        if colResult > 0:
            return colResult
        if diagonalResult > 0:
            return diagonalResult
        if antiDiagonalRsult > 0:
            return antiDiagonalRsult

        return 0         
            
    def scanRows(self) -> int:
        for row in self.board:
            if "".join(str(x) for x in row) == "1" * self.n:
                return 1
            if "".join(str(y) for y in row) == "2" * self.n:
                return 2
        return 0

    def scanCols(self) -> int:
        for col in range(self.n):
            colValues = ""
            for row in self.board:
                colValues += str(row[col])
            if colValues == "1" * self.n:
                return 1
            if colValues == "2" * self.n:
                return 2
        return 0

    def scanDiagonal(self) -> str:
        diagonalValue = ""
        for i in range(self.n):
            diagonalValue += str(self.board[i][i])
        if diagonalValue == "1" * self.n:
                return 1
        if diagonalValue == "2" * self.n:
            return 2
        return 0

    def scanAntiDiagonal(self) -> str:
        diagonalValue = ""
        row = 0
        for col in range(self.n - 1, -1, -1):
            diagonalValue += str(self.board[row][col])
            row += 1
        if diagonalValue == "1" * self.n:
                return 1
        if diagonalValue == "2" * self.n:
            return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)