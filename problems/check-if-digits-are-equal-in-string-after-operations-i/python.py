class Solution:
    def hasSameDigits(self, s: str) -> bool:
        current = s
        while len(current) != 2:
            temp = ""
            for i in range(1, len(current)):
                output = (int(current[i - 1]) + int(current[i])) % 10
                temp += str(output)
            current = temp
            print(current)

        return current[0] == current[1]
