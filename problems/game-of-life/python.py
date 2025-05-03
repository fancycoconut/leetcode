class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        output = []
        for row in range(rows):
            output.append([0] * cols)
        print(output)

        for row in range(rows):
            for col in range(cols):
                cell = board[row][col]
                numOfNeighbours = self.getNeighbourCount(row, col, board)
                print("(" + str(row) + "," + str(col) + ") - " + str(cell) + " - " + str(numOfNeighbours))
                isAlive = cell == 1
                if isAlive and numOfNeighbours < 2:
                    output[row][col] = 0
                elif isAlive and (numOfNeighbours == 2 or numOfNeighbours ==  3):
                    output[row][col] = 1
                elif isAlive and numOfNeighbours >= 3:
                    output[row][col] = 0
                elif isAlive == False and numOfNeighbours == 3:
                    output[row][col] = 1

        for row in range(rows):
            for col in range(cols):
                board[row][col] = output[row][col]

    def getNeighbourCount(self, row: int, col: int, board: List[List[int]]) -> int:
        numOfNeighbours = 0

        rows = len(board)
        cols = len(board[0])
        # N
        if row - 1 >= 0 and board[row - 1][col] == 1:
            numOfNeighbours += 1
        # S
        if row + 1 < rows and board[row + 1][col] == 1:
            numOfNeighbours += 1
        # W
        if col - 1 >= 0 and board[row][col - 1] == 1:
            numOfNeighbours += 1
        # E
        if col + 1 < cols and board[row][col + 1] == 1:
            numOfNeighbours += 1
        # NW
        if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] == 1:
            numOfNeighbours += 1
        # NE
        if row - 1 >= 0 and col + 1 < cols and board[row - 1][col + 1] == 1:
            numOfNeighbours += 1
        # SW
        if row + 1 < rows and col - 1 >= 0 and board[row + 1][col - 1] == 1:
            numOfNeighbours += 1
        # SE
        if row + 1 < rows and col + 1 < cols and board[row + 1][col + 1] == 1:
            numOfNeighbours += 1
        return numOfNeighbours
