class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1

        lower = 0
        upper = x

        while lower < upper:
            mid = (lower + upper) // 2
            result = mid * mid
            print('r  = ' + str(mid) + ' total = ' + str(result))
            if result == x:
                return mid

            if result > x:
                upper = mid
            else:
                lower = mid + 1

        return lower - 1