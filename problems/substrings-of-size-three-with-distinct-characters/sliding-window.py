class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        numOfGoodStrings = 0

        left = 0
        temp = ""
        for right in range(len(s)):
            temp += s[right]
            right += 1

            while len(temp) > 3:
                temp = temp[1:]
                left += 1

            uniqueStrings = set([letter for letter in temp])
            if len(uniqueStrings) == 3:
                numOfGoodStrings += 1

        return numOfGoodStrings