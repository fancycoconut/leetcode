class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.food = deque(food)
        self.width = width
        self.height = height
        self.snake = deque([(0, 0)])
        self.snakeBodyLookup = set()
        self.snakeBodyLookup.add((0,0))

    def move(self, direction: str) -> int:
        directionVector = self.getDirectionVector(direction)
        row = self.snake[0][0] + directionVector[0]
        col = self.snake[0][1] + directionVector[1]

        if not self.isInBounds(row, col): return -1
        if self.hitsItself(row, col): return -1

        ateFood = self.tryEatFood(row, col)
        if ateFood == False:
            # Delete tail - we don't keep the tail because it didn't grow
            tail = self.snake.pop()
            self.snakeBodyLookup.remove(tail)

        # A new head is always added as we are moving
        self.snake.appendleft((row, col))
        self.snakeBodyLookup.add((row, col))
        
        #print(f"{self.snake[0]} - {direction}")
        return len(self.snake) - 1

    def tryEatFood(self, row: int, col: int) -> bool:
        # Exit if no more food to eat
        if len(self.food) == 0:
            return False

        foodPos = self.food[0]
        if row != foodPos[0] or col != foodPos[1]:
            return False

        self.food.popleft()
        return True

    def hitsItself(self, row: int, col: int) -> bool:
        # The new head can be equal to snake[-1]
        return (row, col) in self.snakeBodyLookup and (row, col) != self.snake[-1]

    def isInBounds(self, row: int, col: int) -> bool:
        return row >= 0 and row < self.height and col >= 0 and col < self.width

    def getDirectionVector(self, direction: str) -> tuple(int, int):
        match direction:
            case "U":
                return (-1, 0)
            case "D":
                return (1, 0)
            case "L":
                return (0, -1)
            case "R":
                return (0, 1)
            case _:
                raise Exception("Invalid direction provided")


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)