class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        output = [0] * (rowIndex + 1)
        output[0] = 1
        output[-1] = 1
        prevRow = self.getRow(rowIndex - 1)

        for i in range(1, len(output) - 1):
            val = prevRow[i] + prevRow[i - 1]
            output[i] = val
        #print(output)

        return output