class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)

            print('k = ' + str(mid) + ' time = ' + str(time))

            if time <= h:
                right = mid
            elif time > h:
                left = mid + 1
        return right
