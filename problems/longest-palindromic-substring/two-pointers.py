class Solution:
    # Two pointers approach
    # We will expand out
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = ""

        for i in range(len(s)):
            # Check odd lengths
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longestPalindrome):
                    longestPalindrome = s[left:right + 1]
                left -= 1
                right += 1

            # Check even lengths
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longestPalindrome):
                    longestPalindrome = s[left:right + 1]
                left -= 1
                right += 1

        return longestPalindrome