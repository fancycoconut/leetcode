class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        output = []

        prevWord = words[0]
        for i in range(1, len(words)):
            word = words[i]

            if ''.join(sorted(prevWord)) == ''.join(sorted(word)):
                continue

            output.append(prevWord)
            prevWord = word
        output.append(prevWord)

        return output
