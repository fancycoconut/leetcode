class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowersRemaining = n
        length = len(flowerbed)
        for i in range(length):
            if i == 0 and i + 1 < length and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowersRemaining -= 1
                flowerbed[i] = 1
                continue
            if i == length - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowersRemaining -= 1
                flowerbed[i] = 1
                continue
            
            if i - 1 < 0 or i + 1 >= length or flowerbed[i] == 1:
                continue
            
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowersRemaining -= 1
                flowerbed[i] = 1
        #print(flowerbed)
        return flowersRemaining <= 0
