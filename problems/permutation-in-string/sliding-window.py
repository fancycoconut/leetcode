class Solution:
    # Sliding Window
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = [ 0 for _ in range(0, 26) ]
        windowMap = [ 0 for _ in range(0, 26) ]

        for i in range(0, len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1
            #windowMap[ord(s2[i]) - ord('a')] += 1

        left = 0
        right = 0

        while right < len(s2):
            if right - left < len(s1):
                letterIndex = ord(s2[right]) - ord('a')
                windowMap[letterIndex] += 1
                right += 1
            else:
                letterIndex = ord(s2[left]) - ord('a')
                windowMap[letterIndex] -= 1
                left += 1
            if self.letterFrequenciesMatch(s1Map, windowMap):
                    return True
        return False

    def letterFrequenciesMatch(self, a: List[int], b: List[int]) -> bool:
        for i in range(0, 26):
            if a[i] != b[i]:
                return False
        return True