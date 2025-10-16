class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up = 0
        down = 1
        left = 2
        right = 3
        
        visitedLocations = set()
        visitedLocations.add((0,0))

        output = []
        m = len(matrix)
        n = len(matrix[0])

        x = 0
        y = 0
        direction = right # default to right
        while len(visitedLocations) < m * n:
            num = matrix[y][x]

            if direction == up:
                if y - 1 >= 0 and (x, y-1) not in visitedLocations:
                    y = y - 1
                else:
                    direction = right
            if direction == down:
                if y + 1 < m and (x, y+1) not in visitedLocations:
                    y = y + 1
                else:
                    direction = left
            if direction == left:
                if x - 1 >= 0 and (x-1, y) not in visitedLocations:
                    x = x - 1
                else:
                    direction = up
                    y = y - 1
            if direction == right:
                if x + 1 < n and (x+1, y) not in visitedLocations:
                    x = x + 1
                else:
                    direction = down
                    y = y + 1

            print(num)
            output.append(num)
            visitedLocations.add((x, y))
        output.append(matrix[y][x])

        return output
        