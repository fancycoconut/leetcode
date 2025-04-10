class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]

        j = 0
        # 0 means down and 1 means up
        zigZagDirection = 0
        for i in range(len(s)):
            letter = s[i]
            rows[j].append(letter)

            if zigZagDirection == 0:
                j += 1
            else:
                j -= 1

            if j == numRows - 1:
                zigZagDirection = 1
            if j == 0:
                zigZagDirection = 0

        output = ""
        for row in rows:
            output += "".join(row)
        return output
        