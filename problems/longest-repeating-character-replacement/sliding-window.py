class Solution:
    # Sliding window
    def characterReplacement(self, s: str, k: int) -> int:
        longestSubstring = 0
        charMap = [0 for _ in range(0, 26)]
        left = 0
        right = 0
        maxFrequentChar = 0

        while right < len(s):
            letter = s[right]
            right += 1
            charMap[ord(letter) - ord('A')] += 1
            maxFrequentChar = max(charMap[ord(letter) - ord('A')], maxFrequentChar)

            if right - left - maxFrequentChar > k:
                charMap[ord(s[left]) - ord('A')] -= 1
                left += 1
            longestSubstring = max(longestSubstring, right - left)

        return longestSubstring
