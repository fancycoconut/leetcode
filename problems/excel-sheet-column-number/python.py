class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0

        pos = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            letter = columnTitle[i]
            num = ord(letter) - 64

            res = num * pow(26, pos)
            #print(f"{letter} => {num}, pos = {pos} res={res}")

            output += res
            pos += 1

        return output
