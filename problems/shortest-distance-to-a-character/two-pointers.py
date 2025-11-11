class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        output = []

        for i in range(len(s)):
            char = s[i]
            if char == c:
                output.append(0)
                continue

            j = i - 1
            leftIndex = float('inf')
            while j >= 0:
                if s[j] == c:
                    leftIndex = j
                    break
                j -= 1

            k = i + 1
            rightIndex = float('inf')
            while k < len(s):
                if s[k] == c:
                    rightIndex = k
                    break
                k += 1

            #print(str(i) + ": " + char + " l: " + str(leftIndex) + " r: " + str(rightIndex))
            shortest = min(abs(i - leftIndex), abs(rightIndex - i))
            output.append(shortest)
        return output
