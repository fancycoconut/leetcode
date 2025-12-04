class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestCommonPrefix = ""
        
        temp = strs[0]
        
        i = 0
        for letter in temp:
            for str in strs:
                if i >= len(str) or letter != str[i]:
                    return longestCommonPrefix
            
            longestCommonPrefix += str[i]
            i += 1
        return longestCommonPrefix