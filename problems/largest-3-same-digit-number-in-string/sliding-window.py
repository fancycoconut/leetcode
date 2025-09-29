class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxGoodInteger = -1
        currentGoodInteger = ""
        output = ""

        right = 0
        while right < len(num):
            currentGoodInteger += num[right]
            right += 1

            while len(currentGoodInteger) >= 3:
                if self.onlyHas1UniqueDigit(currentGoodInteger):
                    #print("here: " + currentGoodInteger)
                    maxGoodInteger = max(maxGoodInteger, int(currentGoodInteger[0]))
                    output = f"{maxGoodInteger}{maxGoodInteger}{maxGoodInteger}"

                currentGoodInteger = currentGoodInteger[1:]
            #print(currentGoodInteger)

        return output

    def onlyHas1UniqueDigit(self, num: str) -> bool:
        #print(num)
        map = {}

        for digit in num:
            if digit in map:
                map[digit] += 1
            else:
                map[digit] = 1

        #print(len(map.keys()))
        return len(map.keys()) == 1