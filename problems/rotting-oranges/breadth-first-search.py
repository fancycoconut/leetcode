class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numOfMins = 0
        rows = len(grid)
        cols = len(grid[0])
        if not self.hasFreshOranges(grid):
            return 0

        rottenOrangePositions = self.findRottenOranges(grid)

        queue = [[pos for pos in rottenOrangePositions]]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        visited = set()
        while len(queue) > 0:
            positions = queue.pop(0)
            if len(positions) == 0:
                continue
            #print(positions)

            nextPositionSet = []
            for pos in positions:
                if pos in visited:
                    continue
                row = pos[0]
                col = pos[1]
                visited.add(pos)

                
                for direction in directions:
                    r = row + direction[0]
                    c = col + direction[1]
                    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2

                    nextPositionSet.append((r, c))
            queue.append(nextPositionSet)
            #self.printGrid(grid)
            numOfMins += 1

        # check if there are any fresh oranges left
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return numOfMins - 1

    def hasFreshOranges(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        output = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return True
        return False

    def findRottenOranges(self, grid: List[List[int]]) -> List[tuple[int, int]]:
        rows = len(grid)
        cols = len(grid[0])

        output = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    output.append((row, col))
        return output

    def printGrid(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            output = ""
            for col in range(cols):
                output += str(grid[row][col])
            print(output)
        print()