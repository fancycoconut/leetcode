class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if self.isValidTriangle(nums) == False:
            return 'none'

        sides = set()
        for num in nums:
            sides.add(num)

        match len(sides):
            case 1:
                return 'equilateral'
            case 2:
                return 'isosceles'
            case 3:
                return 'scalene'
            case _:
                return 'none'

    # Hint: The condition for a valid triangle is that for any two sides, the sum of their lengths must be greater than the third side.
    def isValidTriangle(self, sides: List[int]) -> bool:
        if sides[0] + sides[1] > sides[2] and \
            sides[1] + sides[2] > sides[0] and \
            sides[2] + sides[0] > sides[1]:
            return True
        return False