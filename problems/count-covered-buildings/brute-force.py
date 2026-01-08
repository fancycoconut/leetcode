class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        maxRows = 0
        maxCols = 0
        buildingsSet = set()
        for building in buildings:
            location = (building[0], building[1])
            buildingsSet.add(location)
            maxRows = max(maxRows, building[0])
            maxCols = max(maxCols, building[1])

        # print(buildingsSet)
        # print(maxRows)
        # print(maxCols)
        coveredBuildings = 0
        for building in buildings:
            location = (building[0], building[1])
            topIsCovered = self.scanTop(location, buildingsSet)
            bottomIsCovered = self.scanBottom(location, maxRows, buildingsSet)
            leftIsCovered = self.scanLeft(location, buildingsSet)
            rightIsCovered = self.scanRight(location, maxCols, buildingsSet)

            if topIsCovered and bottomIsCovered and leftIsCovered and rightIsCovered:
                coveredBuildings += 1

        return coveredBuildings

    def scanTop(self, location: Tuple[int, int], buildingsSet: set) -> bool:
        col = location[1]

        for row in range(location[0] - 1, -1, -1):
            if (row, col) in buildingsSet:
                return True

        return False

    def scanBottom(self, location: Tuple[int, int], maxRows: int, buildingsSet: set) -> bool:
        col = location[1]

        for row in range(location[0] + 1, maxRows + 1):
            if (row, col) in buildingsSet:
                return True

        return False

    def scanLeft(self, location: Tuple[int, int], buildingsSet: set) -> bool:
        row = location[0]

        for col in range(location[1] - 1, -1, -1):
            if (row, col) in buildingsSet:
                return True

        return False

    def scanRight(self, location: Tuple[int, int], maxCols: int, buildingsSet: set) -> bool:
        row = location[0]

        for col in range(location[1] + 1, maxCols + 1):
            if (row, col) in buildingsSet:
                return True

        return False
