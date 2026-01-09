class Solution:
    # A building (x, y) is covered if it has at least one building on the left, right, above, and below.
    # To check this quickly, for every row x keep the minimum and maximum y values, and for every column y keep the minimum and maximum x values.
    # Then a building is covered only if:
    # minY[x] < y < maxY[x] → means there is a building on both left and right
    # minX[y] < x < maxX[y] → means there is a building above and below
    # Count how many buildings satisfy both conditions.
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rowMap = {}
        colMap = {}
        for building in buildings:
            col = building[0]
            row = building[1]
            
            minColForRow, maxColForRow = rowMap.get(row, (float("inf"), 0))
            minRowForCol, maxRowForCol = colMap.get(col, (float("inf"), 0))

            minColForRow = min(minColForRow, col)
            maxColForRow = max(maxColForRow, col)
            minRowForCol = min(minRowForCol, row)
            maxRowForCol = max(maxRowForCol, row)

            rowMap[row] = (minColForRow, maxColForRow)
            colMap[col] = (minRowForCol, maxRowForCol)

        #print(rowMap)
        #print(colMap)
        coveredBuildings = 0
        for building in buildings:
            col = building[0]
            row = building[1]

            minColForRow, maxColForRow = rowMap[row]
            minRowForCol, maxRowForCol = colMap[col]

            if not ((minRowForCol < row) and (row < maxRowForCol)):
                continue
            if not ((minColForRow < col) and (col < maxColForRow)):
                continue

            #print(f"({row}, {col})")
            coveredBuildings += 1


        return coveredBuildings
