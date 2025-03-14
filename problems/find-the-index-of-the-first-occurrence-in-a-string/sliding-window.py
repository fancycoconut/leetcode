class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        end = 0

        word = ''
        while start < len(haystack) and end < len(haystack):
            letter = haystack[end]
            word += letter
            print(word)

            if word == needle:
                return start

            if len(word) == len(needle):
                start += 1
                word = word[1:]
                end += 1
                continue

            end += 1

        return -1