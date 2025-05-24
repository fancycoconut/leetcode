class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        i = 0
        for word in words:
            if x in word:
                output.append(i)
            i += 1

        return output