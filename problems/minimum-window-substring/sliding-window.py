class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if s == t:
            return t

        tMap = {}
        sMap = {}

        for letter in t:
            tMap[letter] = tMap.get(letter, 0) + 1
        
        left = 0
        right = 0
        minimumWindowLength = float('inf')
        minLeft = 0
        minRight = 0

        while right < len(s) or left < len(s):
            # Grow window until I have substring
            if right < len(s) and self.aContainsSubstringOfB(sMap, tMap) == False:
                a = s[right]
                right += 1
                sMap[a] = sMap.get(a, 0) + 1
            else:
                if self.aContainsSubstringOfB(sMap, tMap) and right - left < minimumWindowLength:
                    minimumWindowLength = right - left
                    minLeft = left
                    minRight = right
                    #print(s[minLeft:minRight])
                b = s[left]
                left += 1
                sMap[b] = sMap.get(b, 0) - 1

        return s[minLeft:minRight]
        
    def aContainsSubstringOfB(self, a: Dict[str, int], b: Dict[str, int]) -> bool:
        for key, value in b.items():
            aValue = a.get(key, 0)
            if (aValue < value):
                return False

        return True