class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        output = ""
        for word in words:
            totalWeight = 0
            for letter in word:
                index = int(ord(letter)) - 97
                #print(index)
                totalWeight += weights[index]
            res = totalWeight % 26
            # Find index of lowercase alphabet in reverse
            reverseAlphabetIndex = 122 - res
            output += chr(reverseAlphabetIndex)
        return output
