class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gatePositions = self.findGates(rooms)

        visited = set()
        queue = [pos for pos in gatePositions]
        
        while len(queue) > 0:
            pos = queue.pop(0)
            #print(pos)

            row = pos[0]
            col = pos[1]
            distance = pos[2]

            if (row, col) in visited:
                continue

            # set the distance
            if not self.positionHasObstacle(row, col, rooms):
                rooms[row][col] = min(distance, rooms[row][col])

            visited.add((row, col))

            newDistance = distance + 1
            if self.canGoUp(row, col, rooms):
                queue.append((row - 1, col, newDistance))
            if self.canGoDown(row, col, rooms):
                queue.append((row + 1, col, newDistance))
            if self.canGoLeft(row, col, rooms):
                queue.append((row, col - 1, newDistance))
            if self.canGoRight(row, col, rooms):
                queue.append((row, col + 1, newDistance))

    def canGoUp(self, row, col, rooms) -> bool:
        if row - 1 < 0:
            return False

        if self.positionHasObstacle(row - 1, col, rooms):
            return False
        
        return True

    def canGoDown(self, row, col, rooms) -> bool:
        if row + 1 >= len(rooms):
            return False

        if self.positionHasObstacle(row + 1, col, rooms):
            return False
        
        return True

    def canGoLeft(self, row, col, rooms) -> bool:
        if col - 1 < 0:
            return False

        if self.positionHasObstacle(row, col - 1, rooms):
            return False
        
        return True

    def canGoRight(self, row, col, rooms) -> bool:
        if col + 1 >= len(rooms[0]):
            return False

        if self.positionHasObstacle(row, col + 1, rooms):
            return False
        
        return True

    def positionHasObstacle(self, row, col, rooms) -> bool:
        return rooms[row][col] in [-1, 0]
        
    def findGates(self, rooms: List[List[int]]) -> List[tuple[int, int]]:
        rows = len(rooms)
        cols = len(rooms[0])

        output = []
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    output.append((row, col, 0))
        
        return output
