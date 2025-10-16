class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        results = []
        results.append([1])
        results.append([1, 1])

        for i in range(2, numRows):
            row = [0] * (len(results[i - 1]) + 1)
            row[0] = 1
            row[-1] = 1

            for j in range(1, len(row) - 1):
                prevRow = results[i - 1]
                row[j] = prevRow[j] + prevRow[j - 1]
            #print(row)
            results.append(row)


        return results
