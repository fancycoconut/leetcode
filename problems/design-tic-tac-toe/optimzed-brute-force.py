class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[]] * n
        self.rows = [[]] * n
        self.cols = [[]] * n
        for i in range(n):
            self.rows[i] = [0] * n
            self.cols[i] = [0] * n

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[row][col] = player
        self.cols[col][row] = player

        if self.checkRow(row, player) or \
            self.checkCol(col, player) or \
            self.checkDiagonal(row, col, player) or \
            self.checkAntiDiagonal(row, col, player):
            return player

        return 0         
            
    def checkRow(self, row: int, player: int) -> bool:
        for col in self.rows[row]:
            if col != player:
                return False
        return True

    def checkCol(self, col: int, player: int) -> bool:
        for row in self.cols[col]:
            if row != player:
                return False
        return True

    def checkDiagonal(self, row: int, col: int, player: int) -> bool:
        if row != col:
            return False
        for i in range(self.n):
            if self.rows[i][i] != player:
                return False
        return True

    def checkAntiDiagonal(self, row: int, col: int, player: int) -> bool:
        if col != self.n - row - 1:
            return False
        for i in range(self.n):
            if self.rows[i][self.n - i - 1] != player:
                return False

        return True

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)