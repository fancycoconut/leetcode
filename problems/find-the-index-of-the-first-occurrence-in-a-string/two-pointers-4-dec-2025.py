class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        
        while i < len(haystack):
            letter = haystack[i]
            if letter != needle[0]:
                i += 1
                continue
            
            word = haystack[i:i + len(needle)]
            if word == needle:
                return i
            
            i += 1
        return -1