class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0

        output = ""
        while i < len(word1) and j < len(word2):
            a = word1[i]
            b = word2[j]

            output += a
            output += b

            i += 1
            j += 1

        while i < len(word1):
            output += word1[i]
            i += 1

        while j < len(word2):
            output += word2[j]
            j += 1

        return output
