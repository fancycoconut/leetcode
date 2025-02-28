class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        sum = 0
        for i in range(0, len(nums)):
            num = nums[i]
            leftIndexExists = i - k >= 0
            rightIndexExists = i + k < len(nums)
            bothIndicesExist = leftIndexExists and rightIndexExists
            if bothIndicesExist and num > nums[i-k] and num > nums[i+k]:
                print(num)
                sum += num
                continue
            if leftIndexExists and rightIndexExists == False and num > nums[i-k]:
                print(num)
                sum += num
                continue
            if leftIndexExists == False and rightIndexExists and num > nums[i+k]:
                print(num)
                sum += num
                continue

        return sum