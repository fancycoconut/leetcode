class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swaps = 0
        t1 = []
        t2 = []

        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                swaps += 1
                t1.append(s1[i])
                t2.append(s2[i])
        
        if swaps > 2:
            return False

        t1.sort()
        t2.sort()

        #print(t1)
        #print(t2)
        return ''.join(str(x) for x in t1) == ''.join(str(x) for x in t2)
