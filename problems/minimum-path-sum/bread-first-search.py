class Solution:
    # Results in Time Limit
    def minPathSum(self, grid: List[List[int]]) -> int:
        pathSums = []

        queue = []
        visitedLocations = set()
        startingPoint = (0, 0, 0)
        queue.append(startingPoint)

        width = len(grid[0])
        height = len(grid)
        minSum = float('inf')

        while len(queue) > 0:
            location = queue.pop(0)
            x = location[0]
            y = location[1]
            currentSum = location[2]
            if location in visitedLocations:
                continue

            #print(location)
            visitedLocations.add(location)
            newCurrentSum = currentSum + grid[y][x]

            # Can move right
            if x + 1 < width:
                queue.append((x + 1, y, newCurrentSum))
            # Can move down
            if y + 1 < height:
                queue.append((x, y + 1, newCurrentSum))

            if x == width - 1 and y == height - 1:
                minSum = min(minSum, newCurrentSum)
                #pathSums.append(newCurrentSum)

        return minSum