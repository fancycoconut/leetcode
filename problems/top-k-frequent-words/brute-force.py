class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:        
        wordMap = {}
        for word in words:
            count = wordMap.get(word, 0)
            wordMap[word] = count + 1

        #print(wordMap)
        orderedWords = sorted(wordMap.keys(), key=lambda word:(-wordMap[word], word))
        #print(orderedWords)

        return orderedWords[:k]
