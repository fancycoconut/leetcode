class Solution:
    def maxDifference(self, s: str) -> int:
        freqMap = {}
        for letter in s:
            count = freqMap.get(letter, 0)
            freqMap[letter] = count + 1
        
        maxEvenFreq = float('inf')
        maxOddFreq = 0
        for k,v in freqMap.items():
            isEven = v % 2 == 0
            if isEven:
                maxEvenFreq = min(maxEvenFreq, v)
            else:
                maxOddFreq = max(maxOddFreq, v)

        return maxOddFreq - maxEvenFreq
        