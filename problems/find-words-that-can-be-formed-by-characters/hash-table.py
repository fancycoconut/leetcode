class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charMap = {}
        for letter in chars:
            charMap[letter] = charMap.get(letter, 0) + 1

        length = 0
        for word in words:

            wordMap = {}
            for letter in word:
                wordMap[letter] = wordMap.get(letter, 0) + 1

            if self.frequenciesMatch(wordMap, charMap) == False:
                continue
            
            length += len(word)

        return length

    def frequenciesMatch(self, wordMap: Dict[str, int], charMap: Dict[str, int]) -> bool:
        for key, value in wordMap.items():
            if key not in charMap:
                return False

            if value > charMap[key]:
                return False
        return True

                