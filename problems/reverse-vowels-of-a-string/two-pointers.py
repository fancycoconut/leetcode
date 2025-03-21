class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        vowels = ["a", "e", "i", "o", "u"]

        output = [c for c in s]
        while left < len(s) and right > 0 and left < right:
            a = s[left]
            b = s[right]

            if a.lower() not in vowels:
                left += 1
                continue
            if b.lower() not in vowels:
                right -= 1
                continue

            temp = output[right]
            output[right] = output[left]
            output[left] = temp
            left += 1
            right -= 1

        print(''.join(output))
        return ''.join(output)
