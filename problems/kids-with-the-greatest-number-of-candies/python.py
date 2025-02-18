class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = 0
        for candy in candies:
            maxCandy = max(maxCandy, candy)
        
        output = []
        for candy in candies:
            if candy + extraCandies >= maxCandy:
                output.append(True)
            else:
                output.append(False)
        
        return output
        