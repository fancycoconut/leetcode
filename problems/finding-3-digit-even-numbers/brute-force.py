class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        output = []
        map = self.getMap([str(x) for x in digits])

        for num in range(100, 1000):
            if num % 2 != 0:
                continue
            if self.isSubsetOf(num, map) == False:
                continue
            output.append(num) 

        return output

    def isSubsetOf(self, num: int, setB: Dict[str, int]) -> bool:
        digits = [x for x in str(num)]
        setA = self.getMap(digits)
        for k,v in setA.items():
                if k not in setB:
                    #print(str(num) + " - False (key don't match)")
                    return False
                if v > setB[k]:
                    #print(str(num) + " - False (val don't match)")
                    return False
        return True

    def getMap(self, digits: List[str]) -> Dict[str, int]:
        map = {}

        for digit in digits:
            key = str(digit)
            if key in map:
                map[key] += 1
            else:
                map[key] = 1

        return map
        
        