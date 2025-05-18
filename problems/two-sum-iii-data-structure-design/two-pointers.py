class TwoSum:

    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        left = 0
        right = len(self.nums) - 1

        self.nums.sort()
        while left < len(self.nums) and right > 0 and left != right:
            a = self.nums[left]
            b = self.nums[right]
            if a + b == value:
                return True
            if a + b < value:
                left += 1
            else:
                right -= 1

        return False
