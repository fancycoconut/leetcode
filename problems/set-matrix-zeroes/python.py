class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        targets = []

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    targets.append((row, col))

        #print(targets)

        for target in targets:
            # Update columns
            for row in range(rows):
                matrix[row][target[1]] = 0

            # update rows
            for col in range(cols):
                matrix[target[0]][col] = 0
