class Solution:
    # Two pointer solution
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        a = 0
        b = 0

        while a < len(s) and b < len(t):
            x = s[a]
            y = t[b]

            if x == y:
                a += 1
                b += 1
                continue

            b += 1

        return a == len(s)
        