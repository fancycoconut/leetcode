class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # if even, (high - low + 1) will have the same num of even / odd numbers
        n = (high - low + 1)
        if n % 2 == 0:
            return n // 2
        
        if low % 2 == 1 or high % 2 == 1:
            return (n // 2) + 1
        return n // 2
