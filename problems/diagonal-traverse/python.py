class Solution:
    # Hint: If you do a standard traversal of the array, you can group the elements in each diagonal by the sum of their indices
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        diagonalGroups = {}
        for row in range(m):
            for col in range(n):
                #print(mat[row][col])
                sumOfIndicies = row + col
                group = diagonalGroups.get(sumOfIndicies, [])
                group.append(mat[row][col])
                diagonalGroups[sumOfIndicies] = group

        #print(diagonalGroups)
        output = []
        directionIsUp = True
        for k,group in diagonalGroups.items():
            if directionIsUp == False:
                for item in group:
                    output.append(item)
            else:
                for i in range(len(group) - 1, -1, -1):
                    output.append(group[i])

            directionIsUp = not directionIsUp
        #print(output)

        return output
