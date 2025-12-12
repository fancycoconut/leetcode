class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Prepopulate matrix
        output = []
        for i in range(n):
            row = [0] * n
            output.append(row)

        j = 1
        row = 0
        col = 0
        # 1 up, 2 down, 3 left, 4 right
        direction = 4
        for i in range(n*n):        
            output[row][col] = j
            j += 1

            # Change direction
            if direction == 1 and (row - 1 < 0 or output[row-1][col] != 0):
                direction = 4
            elif direction == 2 and (row + 1 >= n or output[row+1][col] != 0):
                direction = 3
            elif direction == 3 and (col - 1 < 0 or output[row][col - 1] != 0):
                direction = 1
            elif direction == 4 and (col + 1 >= n or output[row][col + 1] != 0):
                direction = 2

            # Move
            if direction == 1 and row - 1 >= 0:
                row -= 1
            elif direction == 2 and row + 1 < n:
                row += 1
            elif direction == 3 and col - 1 >= 0:
                col -= 1
            elif direction == 4 and col + 1 < n:
                col += 1
        print(output)
        return output
        